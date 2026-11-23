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
              "allowed_amount", "paid_amount", "status", "denial_reason", "data_origin"]

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
            store[claim["claim_id"]]["data_origin"] = claim.get("data_origin") or "generated"
            added += 1
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        with self.store_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(store.values())
        return {"added": added, "rejected": rejected, "total": len(store)}

    def harmonize_members(self) -> int:
        """Repair older synthetic history in place: one stable plan_type and
        age_band per member (claims.member_profile), and no age-implausible
        procedure/diagnosis (claims.repair_age_plausibility). Changed rows get
        data_origin = ORIGIN_REGENERATED so regenerated history stays
        distinguishable from claims generated under the current rules.
        Idempotent; returns the number of rows changed."""
        from .claims import ORIGIN_REGENERATED, member_profile, repair_age_plausibility

        store = self.load_store()
        changed = 0
        for row in store.values():
            plan, band = member_profile(row["member_id"])
            touched = False
            if row["plan_type"] != plan or row["age_band"] != band:
                row["plan_type"], row["age_band"] = plan, band
                touched = True
            if repair_age_plausibility(row):
                touched = True
            if touched:
                row["data_origin"] = ORIGIN_REGENERATED
                changed += 1
        changed += self._repair_unsupported_duplicate_denials(store)
        if changed:
            with self.store_path.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(store.values())
        return changed

    @staticmethod
    def _repair_unsupported_duplicate_denials(store: dict) -> int:
        """Older history drew "duplicate claim" at random, so many denials had no
        earlier matching claim. Reassign those to another denial reason, chosen
        by hash of claim_id (status, amounts and the denial itself are kept) and
        tag the row regenerated. Idempotent."""
        import hashlib
        from .claims import RANDOM_DENIAL_REASONS

        first: dict[tuple, str] = {}
        for r in store.values():
            key = (r["member_id"], r["procedure_code"], r["service_date"])
            if key not in first or r["claim_id"] < first[key]:
                first[key] = r["claim_id"]
        n = 0
        for r in store.values():
            key = (r["member_id"], r["procedure_code"], r["service_date"])
            if (r["status"] == "denied" and r["denial_reason"] == "duplicate claim"
                    and first[key] == r["claim_id"]):
                h = hashlib.sha256((r["claim_id"] + "r").encode()).digest()[0]
                r["denial_reason"] = RANDOM_DENIAL_REASONS[h % len(RANDOM_DENIAL_REASONS)]
                # keep earlier repair provenance: add this repair's date instead of overwriting
                prev = r.get("data_origin") or ""
                r["data_origin"] = (prev if "2026-11-22" in prev else
                                    f"{prev}+2026-11-22" if prev.startswith("regenerated") else "regenerated-2026-11-22")
                n += 1
        return n

    def origin_counts(self) -> dict[str, int]:
        """Claims per data_origin; blank legacy values count as generated."""
        return dict(sorted(Counter(r.get("data_origin") or "generated"
                                   for r in self.load_store().values()).items()))

    def reconcile(self) -> list[dict]:
        """Cross-check that each aggregate view accounts for the whole store:
        claim counts (monthly, plan mix, plan performance, age bands, per-member
        plans, procedure rows) and paid dollars (monthly vs age bands vs raw
        store). Returns one row per check with the two compared values and ok.
        Money compares to the cent (age bands within their own rounding). Views that drop rows silently (a blank
        plan, an unknown month) show up here as a mismatch."""
        store = self.load_store()
        n = len(store)
        paid = round(sum(float(r["paid_amount"] or 0) for r in store.values()), 2)
        monthly = self.monthly_financials()
        bands = self.age_band_costs()
        checks = [
            ("claims: monthly view", sum(m["claims"] for m in monthly), n),
            ("claims: plan mix", sum(c for _p, c in self.plan_mix()), n),
            ("claims: plan performance", sum(p["claims"] for p in self.plan_performance()), n),
            ("claims: age bands", sum(b["claims"] for b in bands), n),
            ("claims: cost per member", sum(p["claims"] for p in self.plan_per_member()), n),
            ("paid $: monthly view", round(sum(m["paid"] for m in monthly), 2), paid),
            # age bands store a per-claim average rounded to cents, so allow that rounding
            ("paid $: age bands", round(sum(b["avg_paid"] * b["claims"] for b in bands), 2), paid,
             0.005 * n + 0.01),
            ("denied claims: reasons", sum(c for _r, c in self.denial_reasons()),
             sum(1 for r in store.values() if r["status"] == "denied")),
        ]
        out = []
        for name, a, b, *tol in checks:
            out.append({"check": name, "view": a, "store": b, "ok": abs(a - b) <= (tol[0] if tol else 0.001)})
        return out

    SIZE_BANDS = [("under $100", 0, 100), ("$100-$999", 100, 1000), ("$1,000-$9,999", 1000, 10000),
                  ("$10,000+", 10000, float("inf"))]

    def claim_size_bands(self) -> list[dict]:
        """Claims, paid dollars and denial rate by billed-amount band, smallest
        band first, with each band's share of claims and of paid dollars. Shows
        how a few large claims dominate spend while most claims are small.
        Band edges are illustrative. Every claim lands in exactly one band."""
        agg = [{"claims": 0, "paid": 0.0, "denied": 0} for _ in self.SIZE_BANDS]
        for r in self.load_store().values():
            billed = float(r["billed_amount"] or 0)
            for i, (_n, lo, hi) in enumerate(self.SIZE_BANDS):
                if lo <= billed < hi:
                    agg[i]["claims"] += 1
                    agg[i]["paid"] += float(r["paid_amount"] or 0)
                    agg[i]["denied"] += r["status"] == "denied"
                    break
        tc = sum(a["claims"] for a in agg)
        tp = sum(a["paid"] for a in agg)
        return [{"band": name, "claims": a["claims"],
                 "claim_share": round(a["claims"] / tc, 4) if tc else 0.0,
                 "paid": round(a["paid"], 2),
                 "paid_share": round(a["paid"] / tp, 4) if tp else 0.0,
                 "denial_rate": round(a["denied"] / a["claims"], 4) if a["claims"] else 0.0}
                for (name, _lo, _hi), a in zip(self.SIZE_BANDS, agg)]

    def member_claim_distribution(self) -> list[dict]:
        """Members grouped by how many claims they have (1, 2, 3, 4+): members,
        share of members, and share of paid dollars. Shows whether spend sits
        with frequent users. Synthetic, illustrative; no enrollment data, so
        members with zero claims are not visible."""
        per: dict[str, list] = {}
        for r in self.load_store().values():
            m = per.setdefault(r["member_id"], [0, 0.0])
            m[0] += 1
            m[1] += float(r["paid_amount"] or 0)
        labels = [("1 claim", 1, 1), ("2 claims", 2, 2), ("3 claims", 3, 3), ("4+ claims", 4, 10**9)]
        agg = [[0, 0.0] for _ in labels]
        for n, paid in per.values():
            for i, (_l, lo, hi) in enumerate(labels):
                if lo <= n <= hi:
                    agg[i][0] += 1
                    agg[i][1] += paid
                    break
        tm = sum(a[0] for a in agg)
        tp = sum(a[1] for a in agg)
        return [{"bucket": l, "members": a[0], "member_share": round(a[0] / tm, 4) if tm else 0.0,
                 "paid": round(a[1], 2), "paid_share": round(a[1] / tp, 4) if tp else 0.0}
                for (l, _lo, _hi), a in zip(labels, agg)]

    def status_breakdown(self) -> list[dict]:
        """Claims, billed and paid dollars per claim status (paid, denied,
        adjusted first in that order, then any others by name). The base view
        the other sections slice; shares are of all claims in the store."""
        agg: dict[str, dict] = {}
        for r in self.load_store().values():
            a = agg.setdefault(r["status"] or "unknown", {"claims": 0, "billed": 0.0, "paid": 0.0})
            a["claims"] += 1
            a["billed"] += float(r["billed_amount"] or 0)
            a["paid"] += float(r["paid_amount"] or 0)
        total = sum(a["claims"] for a in agg.values())
        order = {"paid": 0, "adjusted": 1, "denied": 2}
        return [{"status": k, "claims": a["claims"],
                 "share": round(a["claims"] / total, 4) if total else 0.0,
                 "billed": round(a["billed"], 2), "paid": round(a["paid"], 2)}
                for k, a in sorted(agg.items(), key=lambda kv: (order.get(kv[0], 9), kv[0]))]

    def diagnosis_summary(self, top: int = 6) -> list[dict]:
        """Top diagnosis codes by total paid, with description, claim count,
        average billed and denial rate. Codes and descriptions are an
        illustrative teaching list, not authoritative coding. Synthetic data."""
        from .claims import DIAGNOSES

        desc = {code: d for code, d in DIAGNOSES}
        agg: dict[str, dict] = {}
        for row in self.load_store().values():
            a = agg.setdefault(row["diagnosis_code"] or "Unknown",
                               {"claims": 0, "denied": 0, "billed": 0.0, "paid": 0.0})
            a["claims"] += 1
            a["denied"] += row["status"] == "denied"
            a["billed"] += float(row["billed_amount"] or 0)
            a["paid"] += float(row["paid_amount"] or 0)
        out = [{"code": code, "description": desc.get(code, ""), "claims": a["claims"],
                "avg_billed": round(a["billed"] / a["claims"], 2), "paid": round(a["paid"], 2),
                "denial_rate": round(a["denied"] / a["claims"], 4)} for code, a in agg.items()]
        return sorted(out, key=lambda r: (-r["paid"], r["code"]))[:top]

    def store_summary(self) -> dict:
        """One-line facts about the whole store: claims, distinct members,
        months covered (by service date), billed/paid totals, denial rate and
        the data_origin split. Empty store returns zeros with an empty origin
        map."""
        store = self.load_store()
        n = len(store)
        denied = sum(1 for r in store.values() if r["status"] == "denied")
        months = sorted({(r["service_date"] or "")[:7] for r in store.values()} - {""})
        return {"claims": n,
                "members": len({r["member_id"] for r in store.values()}),
                "months": len(months),
                "first_month": months[0] if months else None,
                "last_month": months[-1] if months else None,
                "billed": round(sum(float(r["billed_amount"] or 0) for r in store.values()), 2),
                "paid": round(sum(float(r["paid_amount"] or 0) for r in store.values()), 2),
                "denial_rate": round(denied / n, 4) if n else 0.0,
                "origins": self.origin_counts()}

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

    def repeat_denial_members(self, min_denials: int = 3, top: int = 5) -> list[dict]:
        """Synthetic member ids with at least min_denials denied claims, most
        denials first, with their denial rate. A starting point for an
        outreach or billing-pattern review; with random synthetic data it is
        illustrative only."""
        agg: dict[str, list[int]] = {}
        for r in self.load_store().values():
            a = agg.setdefault(r["member_id"], [0, 0])
            a[0] += 1
            a[1] += r.get("status") == "denied"
        rows = [{"member": m, "claims": n, "denied": d, "denial_rate": round(d / n, 4)}
                for m, (n, d) in agg.items() if d >= min_denials]
        rows.sort(key=lambda x: (-x["denied"], -x["denial_rate"], x["member"]))
        return rows[:top]

    def plan_per_member(self) -> list[dict]:
        """Per plan: distinct synthetic members seen, claims per member and
        paid dollars per member in the store (a rough per-member-cost view; a
        real PMPM needs enrollment months, which this synthetic data lacks).
        Highest paid per member first."""
        agg: dict[str, dict] = {}
        for r in self.load_store().values():
            a = agg.setdefault(r["plan_type"], {"members": set(), "claims": 0, "paid": 0.0})
            a["members"].add(r["member_id"])
            a["claims"] += 1
            a["paid"] += float(r["paid_amount"] or 0)
        rows = [{"plan": p, "members": len(a["members"]), "claims": a["claims"],
                 "claims_per_member": round(a["claims"] / len(a["members"]), 2),
                 "paid_per_member": round(a["paid"] / len(a["members"]), 2)}
                for p, a in agg.items()]
        rows.sort(key=lambda x: (-x["paid_per_member"], x["plan"]))
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

    def duplicate_leakage(self) -> dict:
        """Payment-integrity view of same member/procedure/date groups. In each
        group the first claim by claim_id is treated as the original; later
        claims that still paid are potential leakage (dollars to review), and
        later claims denied as "duplicate claim" are catches. Also counts
        claims denied as "duplicate claim" that have no matching sibling at all
        (denials the data cannot support). A review queue, not proof: repeat
        services can be legitimate, and this synthetic data is random."""
        groups: dict[tuple, list[dict]] = {}
        for row in self.load_store().values():
            groups.setdefault((row["member_id"], row["procedure_code"], row["service_date"]), []).append(row)
        out = {"groups": 0, "later_claims": 0, "caught": 0, "leaked_claims": 0, "leaked_paid": 0.0,
               "unsupported_duplicate_denials": 0}
        for rows in groups.values():
            rows.sort(key=lambda r: r["claim_id"])
            if len(rows) == 1:
                r = rows[0]
                out["unsupported_duplicate_denials"] += (
                    r["status"] == "denied" and r["denial_reason"] == "duplicate claim")
                continue
            out["groups"] += 1
            for r in rows[1:]:
                out["later_claims"] += 1
                if r["status"] == "denied" and r["denial_reason"] == "duplicate claim":
                    out["caught"] += 1
                elif float(r["paid_amount"] or 0) > 0:
                    out["leaked_claims"] += 1
                    out["leaked_paid"] += float(r["paid_amount"])
        out["leaked_paid"] = round(out["leaked_paid"], 2)
        return out

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
