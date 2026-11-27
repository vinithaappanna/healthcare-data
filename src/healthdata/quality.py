"""Data-quality checks over the claims store. Each returns a list of issue
strings; empty means pass. Daily runs fail loudly on any issue."""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

from .claims import PROCEDURES, DIAGNOSES

_RANGES = {code: rng for code, _d, rng in PROCEDURES}
_DX = {code for code, _d in DIAGNOSES}


def check_amount_consistency(rows: list[dict]) -> list[str]:
    """Paid must not exceed allowed, allowed must not exceed billed."""
    issues = []
    for row in rows:
        try:
            billed = float(row["billed_amount"])
            allowed = float(row["allowed_amount"] or 0)
            paid = float(row["paid_amount"] or 0)
        except (TypeError, ValueError):
            issues.append(f"{row['claim_id']}: non-numeric amounts")
            continue
        if paid > allowed + 0.01:
            issues.append(f"{row['claim_id']}: paid {paid} exceeds allowed {allowed}")
        if allowed > billed + 0.01:
            issues.append(f"{row['claim_id']}: allowed {allowed} exceeds billed {billed}")
    return issues


def check_denial_reasons(rows: list[dict]) -> list[str]:
    issues = []
    for row in rows:
        if row["status"] == "denied" and not row.get("denial_reason"):
            issues.append(f"{row['claim_id']}: denied without a reason")
        if row["status"] == "denied" and float(row["paid_amount"] or 0) != 0.0:
            issues.append(f"{row['claim_id']}: denied claim has a payment")
    return issues


def check_duplicate_members_per_claim(rows: list[dict]) -> list[str]:
    """claim_id is the grain: one row per claim."""
    seen = set()
    issues = []
    for row in rows:
        if row["claim_id"] in seen:
            issues.append(f"duplicate claim_id {row['claim_id']}")
        seen.add(row["claim_id"])
    return issues


def check_billed_in_procedure_range(rows: list[dict], slack: float = 1.01) -> list[str]:
    """Billed amount should sit inside the illustrative range for its procedure
    code, and the code itself must be a known one (illustrative reference list)."""
    issues = []
    for row in rows:
        rng = _RANGES.get(row.get("procedure_code"))
        if rng is None:
            issues.append(f"{row['claim_id']}: unknown procedure code {row.get('procedure_code')!r}")
            continue
        try:
            billed = float(row["billed_amount"])
        except (TypeError, ValueError):
            continue  # reported by the amount-consistency check
        if not rng[0] / slack <= billed <= rng[1] * slack:
            issues.append(f"{row['claim_id']}: billed {billed} outside {rng} for {row['procedure_code']}")
    return issues


def check_known_diagnosis(rows: list[dict]) -> list[str]:
    return [f"{r['claim_id']}: unknown diagnosis code {r.get('diagnosis_code')!r}"
            for r in rows if r.get("diagnosis_code") not in _DX]


def check_service_dates(rows: list[dict], today: dt.date | None = None,
                        max_age_days: int = 730) -> list[str]:
    """Service dates must parse as ISO dates, not be in the future, and not be
    older than `max_age_days` (a stale date usually means a bad extract)."""
    today = today or dt.date.today()
    issues = []
    for r in rows:
        raw = r.get("service_date") or ""
        try:
            day = dt.date.fromisoformat(raw)
        except ValueError:
            issues.append(f"{r['claim_id']}: unparseable service_date {raw!r}")
            continue
        if day > today:
            issues.append(f"{r['claim_id']}: service_date {day} is in the future")
        elif (today - day).days > max_age_days:
            issues.append(f"{r['claim_id']}: service_date {day} is over {max_age_days} days old")
    return issues


def check_member_consistency(rows: list[dict]) -> list[str]:
    """One member must keep one plan type and one age band across claims.
    Conflicts make per-member and per-plan views meaningless."""
    seen: dict[str, tuple] = {}
    issues = []
    for r in rows:
        key = (r.get("plan_type"), r.get("age_band"))
        first = seen.setdefault(r.get("member_id"), key)
        if first != key:
            issues.append(f"{r['claim_id']}: member {r.get('member_id')} has conflicting "
                          f"plan/age band {key} vs {first}")
    return issues


def check_age_plausibility(rows: list[dict]) -> list[str]:
    """Illustrative rule: some codes are not generated for some age bands
    (e.g. total knee replacement for 0-17). Not clinical guidance."""
    from .claims import age_plausible

    return [f"{r['claim_id']}: {r.get('procedure_code')}/{r.get('diagnosis_code')} implausible for age band {r.get('age_band')}"
            for r in rows
            if not age_plausible(r.get("age_band"), r.get("procedure_code"), r.get("diagnosis_code"))]


def check_duplicate_denials_supported(rows: list[dict]) -> list[str]:
    """A claim denied as "duplicate claim" needs an earlier claim (lower
    claim_id) with the same member, procedure and service date; otherwise the
    denial reason has nothing to refer to."""
    first: dict[tuple, str] = {}
    for r in rows:
        key = (r.get("member_id"), r.get("procedure_code"), r.get("service_date"))
        if key not in first or r["claim_id"] < first[key]:
            first[key] = r["claim_id"]
    return [f"{r['claim_id']}: denied as duplicate but no earlier matching claim"
            for r in rows
            if r.get("status") == "denied" and r.get("denial_reason") == "duplicate claim"
            and first[(r.get("member_id"), r.get("procedure_code"), r.get("service_date"))] == r["claim_id"]]


def check_month_concentration(rows: list[dict], max_share: float = 0.5, min_rows: int = 200) -> list[str]:
    """No single service month may hold more than max_share of the claims
    (stores under min_rows are skipped). A heavily skewed month distribution
    means the generator is stamping claims with one date, which makes every
    monthly comparison reflect the generator, not utilization."""
    if len(rows) < min_rows:
        return []
    from collections import Counter

    months = Counter((r.get("service_date") or "")[:7] for r in rows)
    month, n = months.most_common(1)[0]
    share = n / len(rows)
    return [f"service month {month} holds {share:.0%} of claims (limit {max_share:.0%})"] if share > max_share else []


KNOWN_STATUSES = {"paid", "denied", "adjusted"}


def check_status_vocabulary(rows: list[dict]) -> list[str]:
    """Status must be paid, denied or adjusted; a denial reason belongs only on
    denied claims; amounts must not be negative; claim ids must be unique."""
    issues = []
    seen: set[str] = set()
    for row in rows:
        cid = row.get("claim_id", "?")
        if cid in seen:
            issues.append(f"{cid}: duplicate claim id")
        seen.add(cid)
        if row.get("status") not in KNOWN_STATUSES:
            issues.append(f"{cid}: unknown status {row.get('status')!r}")
        elif row["status"] != "denied" and row.get("denial_reason"):
            issues.append(f"{cid}: denial reason on a {row['status']} claim")
        for field in ("billed_amount", "allowed_amount", "paid_amount"):
            try:
                if float(row.get(field) or 0) < 0:
                    issues.append(f"{cid}: negative {field}")
            except (TypeError, ValueError):
                pass        # non-numeric values are reported by the amount check
    return issues


ORIGIN_PATTERN = re.compile(r"^(generated|regenerated-\d{4}-\d{2}-\d{2}(\+\d{4}-\d{2}-\d{2})*)$")


def check_data_origin(rows: list[dict]) -> list[str]:
    """Provenance integrity: every row carries a data_origin tag that is either
    "generated" or "regenerated-YYYY-MM-DD" (composites joined with "+", dates
    valid and in ascending order). An empty or malformed tag would break the
    provenance counts silently."""
    issues = []
    for r in rows:
        tag = r.get("data_origin")
        if tag is None or tag == "":
            issues.append(f"{r.get('claim_id', '?')}: missing data_origin")
        elif not ORIGIN_PATTERN.match(tag):
            issues.append(f"{r.get('claim_id', '?')}: malformed data_origin {tag!r}")
        elif tag.startswith("regenerated-"):
            days = tag[len("regenerated-"):].split("+")
            try:
                parsed = [dt.date.fromisoformat(d) for d in days]
            except ValueError:
                issues.append(f"{r.get('claim_id', '?')}: invalid date in data_origin {tag!r}")
                continue
            if parsed != sorted(set(parsed)):
                issues.append(f"{r.get('claim_id', '?')}: data_origin dates not ascending and unique {tag!r}")
    return issues


CHECKS = [
    ("amount consistency", check_amount_consistency),
    ("denial reasons", check_denial_reasons),
    ("one member per claim", check_duplicate_members_per_claim),
    ("billed within procedure range", check_billed_in_procedure_range),
    ("known diagnosis codes", check_known_diagnosis),
    ("service dates", check_service_dates),
    ("member consistency", check_member_consistency),
    ("age plausibility", check_age_plausibility),
    ("duplicate denials supported", check_duplicate_denials_supported),
    ("service month concentration", check_month_concentration),
    ("status vocabulary and ids", check_status_vocabulary),
    ("data origin tags", check_data_origin),
]


def load_rows(store_path) -> list[dict] | None:
    import csv

    path = Path(store_path)
    if not path.exists():
        return None
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def run_checks(rows: list[dict]) -> list[tuple[str, list[str]]]:
    """Every check with its own issues, in a stable order. A check that raises
    is reported as an issue of its own rather than hiding the others."""
    out = []
    for name, check in CHECKS:
        try:
            out.append((name, check(rows)))
        except Exception as exc:
            out.append((name, [f"check crashed: {type(exc).__name__}: {exc}"]))
    return out


def run_all(store_path) -> list[str]:
    """Run every check against the claims CSV. Returns all issues found."""
    rows = load_rows(store_path)
    if rows is None:
        return [f"store not found: {store_path}"]
    return [issue for _name, issues in run_checks(rows) for issue in issues]
