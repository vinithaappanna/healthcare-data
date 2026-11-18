#!/usr/bin/env python3
"""Update round: generate a fresh batch of synthetic claims, ingest them
(idempotently), run quality checks, and regenerate the report. Exits
non-zero if any quality check fails - a bad batch is loud, not silent."""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from healthdata import report
from healthdata.claims import ClaimGenerator, next_batch_index
from healthdata.pipeline import Pipeline
from healthdata.quality import run_all

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "data" / "claims.csv"
REPORTS = ROOT / "reports"
BATCH_SIZE = 60


def main() -> int:
    # Multiple rounds a day must each add a fresh batch, so the seed mixes
    # the day with a batch sequence number taken from the store. Same day +
    # same store state reproduces the same batch; a new round never
    # regenerates claim ids the dedupe grain would swallow.
    today = dt.date.today()
    day_seed = int(today.strftime("%Y%m%d"))
    day_prefix = f"CLM-{day_seed % 100000:05d}"

    pipe = Pipeline(STORE)
    batch_no = next_batch_index(pipe.load_store().keys(), day_prefix)
    batch = ClaimGenerator(day_seed * 1000 + batch_no, batch=batch_no,
                           id_prefix=day_prefix).claims(BATCH_SIZE, service_date=today)

    stats = pipe.ingest(batch)
    print(f"ingested {stats['added']} new claims from batch B{batch_no:02d} "
          f"({len(stats['rejected'])} rejected); store holds {stats['total']}")
    for rej in stats["rejected"]:
        print(f"REJECTED {rej['claim_id']}: {', '.join(rej['problems'])}")

    issues = run_all(STORE)
    for issue in issues:
        print(f"QUALITY ISSUE: {issue}")

    REPORTS.mkdir(exist_ok=True)
    monthly = pipe.monthly_financials()
    reasons = pipe.denial_reasons()
    mix = pipe.plan_mix()
    (REPORTS / "claims_report.md").write_text(
        report.render_markdown(monthly, reasons, mix, stats["total"],
                               plan_perf=pipe.plan_performance(),
                               procedures=pipe.procedure_summary(),
                               utilization=pipe.high_utilizers(),
                               age_bands=pipe.age_band_costs(),
                               reasons_by_plan=pipe.denial_reasons_by_plan(),
                               duplicates=pipe.potential_duplicates(),
                               trend=[t for t in pipe.monthly_trend()
                                      if t["month"] < today.strftime("%Y-%m")]),
        encoding="utf-8",
    )
    if report.plot_monthly_financials(monthly, REPORTS / "monthly_financials.png"):
        print("wrote financials chart")
    if report.plot_age_band_costs(pipe.age_band_costs(), REPORTS / "age_band_costs.png"):
        print("wrote age band chart")
    if report.plot_denial_reasons(reasons, REPORTS / "denial_reasons.png"):
        print("wrote denial chart")
    print("wrote reports/claims_report.md")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
