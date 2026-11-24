# Service-date redistribution (2026-11-23)

All data here is synthetic.

## Why

Daily batches stamped every claim with the batch's run date, so most of the store sat in
the latest service month (4,701 of 5,180 claims in 2026-11 before this change). Every
monthly view (financials, trend, plan x month outliers, leading denial reason) then
reflected the generator, not anything about utilization.

## What changed

- New batches: `ClaimGenerator.claims(..., spread_days=90)` (used by `scripts/daily_update.py`)
  spreads service dates over the 90 days ending on the run date. Repeat claims keep their
  original's date.
- Existing history: each legacy batch (every row stamped with the single date its claim-id
  prefix names) had its claims moved 0 to 89 days earlier, by a hash of
  (member, procedure, service date). Claims sharing those three fields keep sharing a date,
  so duplicate-claim support is unchanged and the duplicate-denial gate still passes.
- Only `service_date` moved. Amounts, status, denial reasons, members, plan and age band did
  not change in this step.
- Provenance: moved rows got a `+2026-11-23` suffix in `data_origin` (for example
  `regenerated-2026-11-21+2026-11-23`; a former `generated` row becomes
  `regenerated-2026-11-23`). Rows whose hash offset was 0 did not move and were not tagged.
  The older sparse backfill (service months 2025-11 to 2026-07) was not touched.
- New quality gate: no service month may hold more than 50% of claims (stores under 200
  claims are skipped).
- Reports now say monthly figures are generator-shaped, not evidence of utilization trends.

## Metrics before and after

"After" also includes new batches B09 to B11 (180 claims) ingested while this was built, so totals
differ by those 180 claims. The older months in the first rows are identical because they were
not touched.

| Month | Claims before | Claims after | Paid before | Paid after | Denial rate before | Denial rate after |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2025-11 | 18 | 18 | $4,019 | $4,019 | 11.1% | 11.1% |
| 2025-12 | 44 | 44 | $31,423 | $31,423 | 9.1% | 9.1% |
| 2026-01 | 31 | 31 | $43,702 | $43,702 | 0.0% | 0.0% |
| 2026-02 | 32 | 32 | $26,265 | $26,265 | 12.5% | 12.5% |
| 2026-03 | 45 | 45 | $90,177 | $90,177 | 11.1% | 11.1% |
| 2026-04 | 48 | 48 | $76,083 | $76,083 | 8.3% | 8.3% |
| 2026-05 | 43 | 43 | $113,180 | $113,180 | 11.6% | 11.6% |
| 2026-06 | 46 | 46 | $122,054 | $122,054 | 15.2% | 15.2% |
| 2026-07 | 47 | 47 | $71,460 | $71,460 | 8.5% | 8.5% |
| 2026-08 | 50 | 554 | $55,220 | $831,592 | 18.0% | 12.1% |
| 2026-09 | 28 | 1615 | $33,931 | $2,293,818 | 7.1% | 13.9% |
| 2026-10 | 47 | 1624 | $29,094 | $2,133,429 | 8.5% | 13.9% |
| 2026-11 | 4701 | 1093 | $6,569,353 | $1,577,529 | 13.4% | 12.2% |

Store totals before: 5180 claims, $12,773,619 billed,
$7,265,960 paid, 13.11% denied.
After: 5240 claims, $13,006,222 billed,
$7,414,732 paid, 13.07% denied.

## Still true

- Months before 2026-08 are a thin backfill (about 18 to 50 claims each) and are not
  comparable with the spread months.
- Monthly comparisons remain generator-shaped. Plan and age labels are labels only, with no
  plan-specific benefits or clinical realism.
