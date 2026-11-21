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

    def plan_cost_sharing(self) -> list[dict]:
        """Per plan type, on non-denied claims: network discount (billed to
        allowed) and member cost share (allowed minus paid, as a share of
        allowed). Illustrative synthetic metrics, not real benefit design."""
        plans: dict[str, dict] = {}
        for row in self.load_store().values():
            if row["status"] == "denied":
                continue
            p = plans.setdefault(row["plan_type"] or "Unknown",
                                 {"claims": 0, "billed": 0.0, "allowed": 0.0, "paid": 0.0})
            p["claims"] += 1
            p["billed"] += float(row["billed_amount"] or 0)
            p["allowed"] += float(row["allowed_amount"] or 0)
            p["paid"] += float(row["paid_amount"] or 0)
        out = [{"plan": name, "claims": p["claims"],
                "network_discount": round(1 - p["allowed"] / p["billed"], 4) if p["billed"] else 0.0,
                "member_cost_share": round((p["allowed"] - p["paid"]) / p["allowed"], 4)
                if p["allowed"] else 0.0}
               for name, p in plans.items()]
        return sorted(out, key=lambda r: (-r["member_cost_share"], r["plan"]))

    def denial_rate_outliers(self, z: float = 2.0, min_claims: int = 20) -> list[dict]:
        """Plan/month cells whose denial rate differs from the overall rate by
        at least `z` binomial standard errors. A statistical screen for where
        to look first, not proof of anything; synthetic data, illustrative.
        Cells with fewer than `min_claims` claims are skipped. Sorted by |z|."""
        import math

        rows = list(self.load_store().values())
        if not rows:
            return []
        overall = sum(r["status"] == "denied" for r in rows) / len(rows)
        if overall in (0.0, 1.0):
            return []
        cells: dict[tuple[str, str], list[int]] = {}
        for r in rows:
            c = cells.setdefault((r["plan_type"] or "Unknown", (r["service_date"] or "")[:7]), [0, 0])
            c[0] += 1
            c[1] += r["status"] == "denied"
        out = []
        for (plan, month), (n, d) in cells.items():
            if n < min_claims or not month:
                continue
            se = math.sqrt(overall * (1 - overall) / n)
            score = (d / n - overall) / se
            if abs(score) >= z:
                out.append({"plan": plan, "month": month, "claims": n,
                            "denial_rate": round(d / n, 4), "overall_rate": round(overall, 4),
                            "z": round(score, 2)})
        return sorted(out, key=lambda r: (-abs(r["z"]), r["plan"], r["month"]))

    def paid_concentration(self, tiers=(0.01, 0.05, 0.10)) -> dict:
        """Share of total paid dollars held by the top X% of claims (by paid).

        Classic insurance concentration view: a few large claims usually
        carry a big share of spend. Each tier takes ceil(n * pct) claims, at
        least one. Synthetic data, illustrative."""
        import math

        paid = sorted((float(r["paid_amount"] or 0) for r in self.load_store().values()), reverse=True)
        total = sum(paid)
        out = {"claims": len(paid), "total_paid": round(total, 2), "tiers": []}
        if not paid or total <= 0:
            return out
        for pct in tiers:
            k = max(1, math.ceil(len(paid) * pct))
            out["tiers"].append({"top_pct": pct, "claims": k,
                                 "share_of_paid": round(sum(paid[:k]) / total, 4)})
        return out

    def procedure_discounts(self, min_claims: int = 20, top: int = 6) -> list[dict]:
        """Allowed-to-billed ratio per procedure code (a stand-in for the
        negotiated discount), lowest ratio first. Procedures with fewer than
        min_claims claims are skipped as too noisy. Denied claims are excluded
        because their allowed amount is zero by construction. Synthetic,
        illustrative: not real contract rates."""
        agg: dict[str, list[float]] = {}
        for r in self.load_store().values():
            if r.get("status") == "denied":
                continue
            a = agg.setdefault(r["procedure_code"], [0, 0.0, 0.0])
            a[0] += 1
            a[1] += float(r["billed_amount"] or 0)
            a[2] += float(r["allowed_amount"] or 0)
        rows = [{"procedure": c, "claims": n, "billed": round(b, 2), "allowed": round(al, 2),
                 "allowed_to_billed": round(al / b, 4)}
                for c, (n, b, al) in agg.items() if n >= min_claims and b > 0]
        rows.sort(key=lambda x: (x["allowed_to_billed"], x["procedure"]))
        return rows[:top]

    def denied_dollars_by_reason(self) -> list[dict]:
        """Billed dollars on denied claims per denial reason, largest first,
        with each reason's share of all denied billed dollars. Counts alone can
        hide that a rare reason hits expensive procedures. Synthetic,
        illustrative."""
        agg: dict[str, list[float]] = {}
        for r in self.load_store().values():
            if r.get("status") != "denied":
                continue
            a = agg.setdefault(r.get("denial_reason") or "unspecified", [0, 0.0])
            a[0] += 1
            a[1] += float(r["billed_amount"] or 0)
        total = sum(v[1] for v in agg.values())
        rows = [{"reason": k, "claims": n, "billed": round(b, 2),
                 "share": round(b / total, 4) if total else 0.0,
                 "avg_billed": round(b / n, 2)} for k, (n, b) in agg.items()]
        rows.sort(key=lambda x: (-x["billed"], x["reason"]))
        return rows

    def paid_curve(self, points: int = 20) -> list[tuple[float, float]]:
        """Cumulative share of paid dollars vs share of claims, largest claims
        first, as (claims_fraction, paid_fraction) from (0, 0) to (1, 1).
        Empty when there is nothing paid. Synthetic data, illustrative."""
        import math

        paid = sorted((float(r["paid_amount"] or 0) for r in self.load_store().values()), reverse=True)
        total = sum(paid)
        if not paid or total <= 0 or points < 1:
            return []
        out = [(0.0, 0.0)]
        for i in range(1, points + 1):
            k = math.ceil(len(paid) * i / points)
            out.append((round(k / len(paid), 4), round(sum(paid[:k]) / total, 4)))
        return out

    def procedures_by_denial_reason(self, top_reasons: int = 3, top_procs: int = 3) -> list[dict]:
        """For the most common denial reasons, the procedure codes denied for
        that reason most often. Each entry also gives the code's share of that
        reason's denials. Ties break on code. Synthetic, illustrative."""
        reasons: dict[str, dict[str, int]] = {}
        for r in self.load_store().values():
            if r["status"] != "denied":
                continue
            by_proc = reasons.setdefault(r["denial_reason"] or "unspecified", {})
            code = r["procedure_code"] or "Unknown"
            by_proc[code] = by_proc.get(code, 0) + 1
        ranked = sorted(reasons.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))[:top_reasons]
        out = []
        for reason, by_proc in ranked:
            total = sum(by_proc.values())
            procs = sorted(by_proc.items(), key=lambda kv: (-kv[1], kv[0]))[:top_procs]
            out.append({"reason": reason, "denials": total,
                        "procedures": [{"code": c, "denials": n, "share": round(n / total, 4)}
                                       for c, n in procs]})
        return out

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

    def potential_duplicates(self) -> list[dict]:
        """Groups of claims with the same member, procedure and service date.

        A classic payment-integrity screen: same service billed more than
        once under different claim ids. Informational (a review queue, not a
        quality failure) - repeat services can be legitimate. Synthetic data.
        """
        groups: dict[tuple, list[dict]] = {}
        for row in self.load_store().values():
            key = (row["member_id"], row["procedure_code"], row["service_date"])
            groups.setdefault(key, []).append(row)
        out = []
        for (member, code, day), rows in groups.items():
            if len(rows) > 1:
                out.append({"member_id": member, "procedure_code": code,
                            "service_date": day,
                            "claim_ids": sorted(r["claim_id"] for r in rows),
                            "paid": round(sum(float(r["paid_amount"] or 0) for r in rows), 2)})
        return sorted(out, key=lambda g: (-g["paid"], g["member_id"], g["service_date"]))

    def monthly_trend(self) -> list[dict]:
        """Month-over-month change in claim volume, paid dollars and denial
        rate (percentage points). The first month has no prior, so its
        changes are None. Synthetic, illustrative."""
        months = self.monthly_financials()
        out = []
        prev = None
        for m in months:
            def pct(cur, old):
                return round((cur - old) / old, 4) if old else None
            out.append({
                "month": m["month"],
                "claims_change": pct(m["claims"], prev["claims"]) if prev else None,
                "paid_change": pct(m["paid"], prev["paid"]) if prev else None,
                "denial_rate_pp": round((m["denial_rate"] - prev["denial_rate"]) * 100, 2) if prev else None,
            })
            prev = m
        return out
