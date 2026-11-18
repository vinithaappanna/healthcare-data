"""Small query CLI over the synthetic claims store.

  python scripts/query.py claim CLM-61117-B01-000003
  python scripts/query.py member MBR-0076
  python scripts/query.py plan PPO

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


def main(argv: list[str] | None = None, store: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("claim", "member", "plan"):
        sub.add_parser(name).add_argument("key")
    args = parser.parse_args(argv)
    pipe = Pipeline(store or Path(__file__).resolve().parents[2] / "data" / "claims.csv")
    handler = {"claim": lookup_claim, "member": member_summary, "plan": plan_summary}[args.cmd]
    result = handler(pipe, args.key)
    if result is None:
        print(f"no {args.cmd} found for {args.key!r}")
        return 1
    print(json.dumps(result, indent=2))
    return 0
