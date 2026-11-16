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
from healthdata.claims import ClaimGenerator
from healthdata.pipeline import Pipeline
from healthdata.quality import run_all

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "data" / "claims.csv"
REPORTS = ROOT / "reports"
BATCH_SIZE = 60


def main() -> int:
    # Seed on the day so each run adds a distinct but reproducible batch.
    today = dt.date.today()
    seed = int(today.strftime("%Y%m%d"))
    batch = ClaimGenerator(seed).claims(BATCH_SIZE, service_date=today)

    pipe = Pipeline(STORE)
    stats = pipe.ingest(batch)
    print(f"ingested {stats['added']} new claims ({len(stats['rejected'])} rejected); "
          f"store holds {stats['total']}")
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
        report.render_markdown(monthly, reasons, mix, stats["total"]),
        encoding="utf-8",
    )
    if report.plot_monthly_financials(monthly, REPORTS / "monthly_financials.png"):
        print("wrote financials chart")
    if report.plot_denial_reasons(reasons, REPORTS / "denial_reasons.png"):
        print("wrote denial chart")
    print("wrote reports/claims_report.md")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
