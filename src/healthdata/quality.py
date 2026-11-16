"""Data-quality checks over the claims store. Each returns a list of issue
strings; empty means pass. Daily runs fail loudly on any issue."""
from __future__ import annotations

from pathlib import Path


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


def run_all(store_path) -> list[str]:
    """Run every check against the claims CSV. Returns all issues found."""
    import csv

    path = Path(store_path)
    if not path.exists():
        return [f"store not found: {path}"]
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    issues: list[str] = []
    issues += check_amount_consistency(rows)
    issues += check_denial_reasons(rows)
    issues += check_duplicate_members_per_claim(rows)
    return issues
