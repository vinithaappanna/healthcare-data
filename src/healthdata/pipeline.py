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

    def high_utilizers(self, min_claims: int = 3, top: int = 5) -> dict:
        """Members with many claims: a standard utilization-management view.

        Returns {"members_total", "high_utilizers", "share_of_paid", "top"}
        where high utilizers have at least `min_claims` claims in the store.
        Synthetic data, illustrative threshold.
        """
        store = self.load_store()
        members: dict[str, dict] = {}
        for row in store.values():
            m = members.setdefault(row["member_id"], {"member_id": row["member_id"],
                                                      "claims": 0, "paid": 0.0})
            m["claims"] += 1
            m["paid"] += float(row["paid_amount"] or 0)
        heavy = [m for m in members.values() if m["claims"] >= min_claims]
        total_paid = sum(m["paid"] for m in members.values())
        heavy_paid = sum(m["paid"] for m in heavy)
        top_rows = sorted(heavy, key=lambda m: (-m["claims"], -m["paid"], m["member_id"]))[:top]
        return {
            "members_total": len(members),
            "high_utilizers": len(heavy),
            "share_of_paid": round(heavy_paid / total_paid, 4) if total_paid else 0.0,
            "top": [{"member_id": m["member_id"], "claims": m["claims"],
                     "paid": round(m["paid"], 2)} for m in top_rows],
        }

    def age_band_costs(self) -> list[dict]:
        """Claims, average paid per claim and denial rate by age band, in
        natural age order. Illustrative synthetic metrics."""
        from .claims import AGE_BANDS
        store = self.load_store()
        bands: dict[str, dict] = {}
        for row in store.values():
            b = bands.setdefault(row["age_band"] or "Unknown",
                                 {"claims": 0, "paid": 0.0, "denied": 0})
            b["claims"] += 1
            b["paid"] += float(row["paid_amount"] or 0)
            b["denied"] += row["status"] == "denied"
        order = {band: i for i, band in enumerate(AGE_BANDS)}
        return [{"age_band": name, "claims": b["claims"],
                 "avg_paid": round(b["paid"] / b["claims"], 2),
                 "denial_rate": round(b["denied"] / b["claims"], 4)}
                for name, b in sorted(bands.items(), key=lambda kv: (order.get(kv[0], 99), kv[0]))]

    def denial_reasons_by_plan(self) -> dict[str, list[tuple[str, int]]]:
        """Plan type -> denial reasons with counts, most common first.

        Shows whether a plan's denials are driven by a different reason than
        the book overall (e.g. prior authorization on one plan type).
        Synthetic, illustrative.
        """
        store = self.load_store()
        by_plan: dict[str, Counter] = {}
        for row in store.values():
            if row["status"] == "denied" and row["denial_reason"]:
                by_plan.setdefault(row["plan_type"] or "Unknown", Counter())[row["denial_reason"]] += 1
        return {plan: sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
                for plan, c in sorted(by_plan.items())}
