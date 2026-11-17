"""Claims pipeline: validate, dedupe, enrich, and aggregate to monthly marts.

Plain Python + CSV, no external services, so it runs anywhere. The pipeline
is append-only and idempotent: re-running with the same claims changes
nothing (dedupe on claim_id).
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

FIELDNAMES = ["claim_id", "member_id", "plan_type", "age_band", "service_date",
              "procedure_code", "diagnosis_code", "billed_amount",
              "allowed_amount", "paid_amount", "status", "denial_reason"]

REQUIRED = ["claim_id", "member_id", "service_date", "billed_amount", "status"]
VALID_STATUSES = {"paid", "denied", "adjusted"}


def validate(claim: dict) -> list[str]:
    """Return a list of problems with one claim; empty means clean."""
    problems = []
    for field in REQUIRED:
        if not claim.get(field):
            problems.append(f"missing {field}")
    try:
        if float(claim.get("billed_amount", 0)) < 0:
            problems.append("negative billed_amount")
    except (TypeError, ValueError):
        problems.append("billed_amount not numeric")
    if claim.get("status") and claim["status"] not in VALID_STATUSES:
        problems.append(f"unknown status {claim['status']!r}")
    if claim.get("status") == "denied" and not claim.get("denial_reason"):
        problems.append("denied without denial_reason")
    return problems


class Pipeline:
    """Append claims to a CSV store and rebuild aggregates."""

    def __init__(self, store_path):
        self.store_path = Path(store_path)

    def load_store(self) -> dict[str, dict]:
        if not self.store_path.exists():
            return {}
        with self.store_path.open(newline="", encoding="utf-8") as fh:
            return {row["claim_id"]: row for row in csv.DictReader(fh)}

    def ingest(self, claims: list[dict]) -> dict:
        """Validate and append new claims. Returns ingest stats; bad rows are
        rejected with their problems listed, never silently dropped."""
        store = self.load_store()
        rejected = []
        added = 0
        for claim in claims:
            problems = validate(claim)
            if problems:
                rejected.append({"claim_id": claim.get("claim_id", "?"),
                                 "problems": problems})
                continue
            if claim["claim_id"] in store:
                continue
            store[claim["claim_id"]] = {name: claim.get(name, "") for name in FIELDNAMES}
            added += 1
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        with self.store_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(store.values())
        return {"added": added, "rejected": rejected, "total": len(store)}

    def monthly_financials(self) -> list[dict]:
        """Billed/allowed/paid totals and denial rate per service month."""
        store = self.load_store()
        months: dict[str, dict] = {}
        for row in store.values():
            month = row["service_date"][:7]
            m = months.setdefault(month, {"month": month, "claims": 0,
                                          "billed": 0.0, "allowed": 0.0,
                                          "paid": 0.0, "denied": 0})
            m["claims"] += 1
            m["billed"] += float(row["billed_amount"] or 0)
            m["allowed"] += float(row["allowed_amount"] or 0)
            m["paid"] += float(row["paid_amount"] or 0)
            if row["status"] == "denied":
                m["denied"] += 1
        out = []
        for month in sorted(months):
            m = months[month]
            out.append({
                "month": month,
                "claims": m["claims"],
                "billed": round(m["billed"], 2),
                "allowed": round(m["allowed"], 2),
                "paid": round(m["paid"], 2),
                "denial_rate": round(m["denied"] / m["claims"], 4) if m["claims"] else 0.0,
            })
        return out

    def denial_reasons(self) -> list[tuple[str, int]]:
        store = self.load_store()
        counts = Counter(row["denial_reason"] for row in store.values()
                         if row["status"] == "denied" and row["denial_reason"])
        return counts.most_common()

    def plan_mix(self) -> list[tuple[str, int]]:
        store = self.load_store()
        counts = Counter(row["plan_type"] for row in store.values() if row["plan_type"])
        return counts.most_common()

    def plan_performance(self) -> list[dict]:
        """Per plan type: claims, denial rate, paid-to-billed ratio.

        Illustrative synthetic metrics - the kind of plan-level view a
        claims analyst starts from. Sorted by claim count, descending.
        """
        store = self.load_store()
        plans: dict[str, dict] = {}
        for row in store.values():
            plan = row["plan_type"] or "Unknown"
            p = plans.setdefault(plan, {"plan": plan, "claims": 0, "denied": 0,
                                        "billed": 0.0, "paid": 0.0})
            p["claims"] += 1
            p["denied"] += row["status"] == "denied"
            p["billed"] += float(row["billed_amount"] or 0)
            p["paid"] += float(row["paid_amount"] or 0)
        out = [{"plan": p["plan"], "claims": p["claims"],
                "denial_rate": round(p["denied"] / p["claims"], 4),
                "paid_to_billed": round(p["paid"] / p["billed"], 4) if p["billed"] else 0.0}
               for p in plans.values()]
        return sorted(out, key=lambda r: (-r["claims"], r["plan"]))

    def procedure_summary(self, top: int = 5) -> list[dict]:
        """Top procedure codes by total paid, with claim count, average billed
        and denial rate. Illustrative synthetic metrics."""
        store = self.load_store()
        procs: dict[str, dict] = {}
        for row in store.values():
            p = procs.setdefault(row["procedure_code"] or "Unknown",
                                 {"code": row["procedure_code"] or "Unknown",
                                  "claims": 0, "denied": 0, "billed": 0.0, "paid": 0.0})
            p["claims"] += 1
            p["denied"] += row["status"] == "denied"
            p["billed"] += float(row["billed_amount"] or 0)
            p["paid"] += float(row["paid_amount"] or 0)
        out = [{"code": p["code"], "claims": p["claims"],
                "avg_billed": round(p["billed"] / p["claims"], 2),
                "paid": round(p["paid"], 2),
                "denial_rate": round(p["denied"] / p["claims"], 4)}
               for p in procs.values()]
        return sorted(out, key=lambda r: (-r["paid"], r["code"]))[:top]
