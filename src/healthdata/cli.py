"""Small query CLI over the synthetic claims store.

  python scripts/query.py claim CLM-61117-B01-000003
  python scripts/query.py member MBR-0076
  python scripts/query.py plan PPO
  python scripts/query.py procedure 99213
  python scripts/query.py diagnosis I10
  python scripts/query.py batches      # claims per ingest batch
  python scripts/query.py profile      # column profile: blanks, distinct values, numeric range
  python scripts/query.py denials      # denial categories and denied dollars by plan

Read-only. All data is synthetic.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import Pipeline


def lookup_claim(pipe: Pipeline, claim_id: str) -> dict | None:
    return pipe.load_store().get(claim_id)


def member_summary(pipe: Pipeline, member_id: str) -> dict | None:
    rows = [r for r in pipe.load_store().values() if r["member_id"] == member_id]
    if not rows:
        return None
    return {
        "member_id": member_id,
        "claims": len(rows),
        "denied": sum(r["status"] == "denied" for r in rows),
        "billed": round(sum(float(r["billed_amount"] or 0) for r in rows), 2),
        "paid": round(sum(float(r["paid_amount"] or 0) for r in rows), 2),
        "claim_ids": sorted(r["claim_id"] for r in rows),
    }


def plan_summary(pipe: Pipeline, plan: str) -> dict | None:
    for row in pipe.plan_performance():
        if row["plan"].lower() == plan.lower():
            return row
    return None


def _code_summary(pipe: Pipeline, field: str, code: str) -> dict | None:
    rows = [r for r in pipe.load_store().values() if (r[field] or "").lower() == code.lower()]
    if not rows:
        return None
    paid_rows = [r for r in rows if r["status"] != "denied"]
    reasons: dict[str, int] = {}
    for r in rows:
        if r["status"] == "denied":
            reasons[r["denial_reason"] or "unspecified"] = reasons.get(r["denial_reason"] or "unspecified", 0) + 1
    return {
        field: rows[0][field],
        "claims": len(rows),
        "denial_rate": round(sum(r["status"] == "denied" for r in rows) / len(rows), 4),
        "avg_billed": round(sum(float(r["billed_amount"] or 0) for r in rows) / len(rows), 2),
        "avg_paid_non_denied": round(sum(float(r["paid_amount"] or 0) for r in paid_rows) / len(paid_rows), 2)
        if paid_rows else 0.0,
        "denial_reasons": dict(sorted(reasons.items(), key=lambda kv: (-kv[1], kv[0]))),
    }


def procedure_summary(pipe: Pipeline, code: str) -> dict | None:
    """Per procedure code: volume, denial rate, average billed/paid and denial reasons."""
    return _code_summary(pipe, "procedure_code", code)


def diagnosis_summary(pipe: Pipeline, code: str) -> dict | None:
    """Same view keyed by diagnosis code. Illustrative codes, not authoritative."""
    return _code_summary(pipe, "diagnosis_code", code)


def main(argv: list[str] | None = None, store: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("claim", "member", "plan", "procedure", "diagnosis"):
        sub.add_parser(name).add_argument("key")
    for name in ("reconcile", "origins", "bands", "summary", "months", "gates", "denials", "profile", "batches"):
        sub.add_parser(name)        # whole-store views: no key
    args = parser.parse_args(argv)
    pipe = Pipeline(store or Path(__file__).resolve().parents[2] / "data" / "claims.csv")
    if args.cmd == "gates":
        from .quality import load_rows, run_checks

        rows = load_rows(pipe.store_path)
        if rows is None:
            print(json.dumps({"error": f"store not found: {pipe.store_path}"}))
            return 2
        results = run_checks(rows)
        print(json.dumps([{"check": n, "issues": len(i), "ok": not i, "examples": i[:3]} for n, i in results], indent=2))
        return 0 if all(not i for _n, i in results) else 2      # 2: a gate failed, same as reconcile
    if args.cmd == "batches":
        print(json.dumps(pipe.batch_summary(), indent=2))
        return 0
    if args.cmd == "profile":
        print(json.dumps(pipe.profile(), indent=2))
        return 0
    if args.cmd == "denials":
        print(json.dumps({"by_category": pipe.denial_categories(),
                          "by_plan": pipe.plan_denied_dollars(),
                          "note": "synthetic data; category mapping is an illustrative taxonomy"}, indent=2))
        return 0
    if args.cmd == "months":
        print(json.dumps(pipe.month_distribution(), indent=2))
        return 0
    if args.cmd == "summary":
        print(json.dumps(pipe.store_summary(), indent=2))
        return 0
    if args.cmd in ("reconcile", "origins", "bands"):
        if args.cmd == "reconcile":
            rows = pipe.reconcile()
            print(json.dumps(rows, indent=2))
            return 0 if all(r["ok"] for r in rows) else 2     # 2: a view does not match the store
        print(json.dumps(pipe.origin_counts() if args.cmd == "origins" else pipe.claim_size_bands(), indent=2))
        return 0
    handler = {"claim": lookup_claim, "member": member_summary, "plan": plan_summary,
               "procedure": procedure_summary, "diagnosis": diagnosis_summary}[args.cmd]
    result = handler(pipe, args.key)
    if result is None:
        print(f"no {args.cmd} found for {args.key!r}")
        return 1
    print(json.dumps(result, indent=2))
    return 0
