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
from healthdata.claims import SERVICE_SPREAD_DAYS, ClaimGenerator, next_batch_index
from healthdata.pipeline import Pipeline
from healthdata.quality import load_rows, run_all, run_checks

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "data" / "claims.csv"
REPORTS = ROOT / "reports"
BATCH_SIZE = 60


def main(root: Path | None = None, report_only: bool = False) -> int:
    """Run one round. `root` redirects data/ and reports/ (used by tests).
    report_only regenerates the report and charts from the existing store: no
    new batch, no store writes, so repeat runs are safe."""
    STORE = (root / "data" / "claims.csv") if root else globals()["STORE"]
    REPORTS = (root / "reports") if root else globals()["REPORTS"]
    STORE.parent.mkdir(parents=True, exist_ok=True)
    # Multiple rounds a day must each add a fresh batch, so the seed mixes
    # the day with a batch sequence number taken from the store. Same day +
    # same store state reproduces the same batch; a new round never
    # regenerates claim ids the dedupe grain would swallow.
    today = dt.date.today()
    day_seed = int(today.strftime("%Y%m%d"))
    day_prefix = f"CLM-{day_seed % 100000:05d}"

    pipe = Pipeline(STORE)
    if report_only:
        if not STORE.exists():
            print("no store to report on; run a full round first")
            return 1
        stats = {"total": len(pipe.load_store())}
        print(f"report-only: no batch added; store holds {stats['total']}")
    else:
        batch_no = next_batch_index(pipe.load_store().keys(), day_prefix)
        batch = ClaimGenerator(day_seed * 1000 + batch_no, batch=batch_no,
                               id_prefix=day_prefix).claims(BATCH_SIZE, service_date=today,
                                                          spread_days=SERVICE_SPREAD_DAYS)

        stats = pipe.ingest(batch)
        fixed = pipe.harmonize_members()
        if fixed:
            print(f"repaired {fixed} older synthetic rows (member profile / age plausibility)")
        print(f"ingested {stats['added']} new claims from batch B{batch_no:02d} "
              f"({len(stats['rejected'])} rejected); store holds {stats['total']}")
        for rej in stats["rejected"]:
            print(f"REJECTED {rej['claim_id']}: {', '.join(rej['problems'])}")

    issues = run_all(STORE)
    for issue in issues:
        print(f"QUALITY ISSUE: {issue}")

    for r in pipe.reconcile():
        if not r["ok"]:
            issues.append(f"reconciliation: {r['check']} view {r['view']} != store {r['store']}")
            print(f"QUALITY ISSUE: {issues[-1]}")

    REPORTS.mkdir(exist_ok=True)
    monthly = pipe.monthly_financials()
    reasons = pipe.denial_reasons()
    mix = pipe.plan_mix()
    (REPORTS / "claims_report.md").write_text(
        report.render_markdown(monthly, reasons, mix, stats["total"],
                               plan_perf=pipe.plan_performance(),
                               cost_sharing=pipe.plan_cost_sharing(),
                               billed_out=pipe.billed_outliers(),
                               dispersion=pipe.member_claim_dispersion(),
                               independence=pipe.plan_denial_independence(),
                               status_ratios=pipe.status_payment_ratios(),
                               denial_cats=pipe.denial_categories(),
                               plan_denied_dollars=pipe.plan_denied_dollars(),
                               outliers=pipe.denial_rate_outliers(),
                               concentration=pipe.paid_concentration(),
                               discounts=pipe.procedure_discounts(),
                               diagnoses=pipe.diagnosis_summary(),
                               month_dist=pipe.month_distribution(),
                               age_denials=pipe.denials_by_age_band(),
                               member_denials=pipe.member_denial_experience(),
                               plan_intervals=pipe.plan_denial_intervals(),
                               plan_age=pipe.plan_age_matrix(),
                               proc_screen=pipe.procedure_denial_screen(),
                               dx_proc_pairs=pipe.diagnosis_procedure_pairs(),
                               reasons_by_month=pipe.denial_reasons_by_month(),
                               statuses=pipe.status_breakdown(),
                               member_dist=pipe.member_claim_distribution(),
                               dup_leakage=pipe.duplicate_leakage(),
                               size_bands=pipe.claim_size_bands(),
                               reconciliation=pipe.reconcile(),
                               origins=pipe.origin_counts(),
                               per_member=pipe.plan_per_member(),
                               repeat_denials=pipe.repeat_denial_members(),
                               denied_dollars=pipe.denied_dollars_by_reason(),
                               denial_procs=pipe.procedures_by_denial_reason(),
                               gates=[(n, len(i)) for n, i in run_checks(load_rows(STORE) or [])],
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
    if report.plot_paid_concentration(pipe.paid_curve(), REPORTS / "paid_concentration.png"):
        print("wrote concentration chart")
    if report.plot_plan_denial_rates(pipe.plan_performance(), REPORTS / "plan_denial_rates.png"):
        print("wrote plan denial chart")
    if report.plot_size_bands(pipe.claim_size_bands(), REPORTS / "size_bands.png"):
        print("wrote size band chart")
    if report.plot_age_band_costs(pipe.age_band_costs(), REPORTS / "age_band_costs.png"):
        print("wrote age band chart")
    if report.plot_denial_categories(pipe.denial_categories(), REPORTS / "denial_categories.png"):
        print("wrote denial category chart")
    if report.plot_denial_reasons(reasons, REPORTS / "denial_reasons.png"):
        print("wrote denial chart")
    print("wrote reports/claims_report.md")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main(report_only="--report-only" in sys.argv[1:]))
