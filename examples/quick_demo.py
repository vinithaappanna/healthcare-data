#!/usr/bin/env python3
"""Quick demo: generate synthetic claims, run the pipeline, print the marts.
Uses a temp store so it never touches the real data directory."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from healthdata.claims import ClaimGenerator
from healthdata.pipeline import Pipeline
from healthdata.quality import run_all

with tempfile.TemporaryDirectory() as tmp:
    store = Path(tmp) / "claims.csv"
    pipe = Pipeline(store)

    stats = pipe.ingest(ClaimGenerator(seed=7).claims(500))
    print(f"ingested {stats['added']} claims, {len(stats['rejected'])} rejected")

    print("\nmonthly financials (last 3 months):")
    for m in pipe.monthly_financials()[-3:]:
        print(f"  {m['month']}: {m['claims']} claims, "
              f"billed ${m['billed']:,.0f}, paid ${m['paid']:,.0f}, "
              f"denial rate {m['denial_rate']:.1%}")

    print("\ntop denial reasons:")
    for reason, count in pipe.denial_reasons()[:3]:
        print(f"  {reason}: {count}")

    print("\nplan mix:", dict(pipe.plan_mix()))
    issues = run_all(store)
    print(f"\nquality checks: {'all pass' if not issues else issues}")
