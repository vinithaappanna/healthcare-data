# healthcare-data

![tests](https://github.com/vinithaappanna/healthcare-data/actions/workflows/tests.yml/badge.svg)

A synthetic healthcare **insurance claims** data project: generator, pipeline,
quality checks, marts, visuals and a quick demo. Every record is invented by a
seeded RNG - no real member, patient, provider or plan data anywhere.

![Monthly billed vs paid](reports/monthly_financials.png)

![Denial reasons](reports/denial_reasons.png)

## What it does

- `healthdata.claims` - deterministic synthetic claims (plans, procedures,
  diagnoses, billed/allowed/paid amounts, denials with reasons)
- `healthdata.pipeline` - validate, dedupe on `claim_id`, append to a CSV
  store, and build monthly financial marts, denial-reason and plan-mix views
- `healthdata.quality` - amount-consistency, denial-reason, duplicate-grain,
  procedure-range, diagnosis, service-date, member-consistency (one plan and age band per member) and status/id checks (known statuses, no reason on non-denied claims, no negative amounts, unique ids) and data-origin tag checks (valid provenance tags) that fail loudly
- `healthdata.report` - markdown report plus charts. Sections include plan
  performance and cost sharing, denial reasons (and the procedures behind them),
  plan x month denial-rate outliers, paid-amount concentration, cost by age
  band, month-over-month trend, potential duplicate services and a per-check
  data quality gate table
- `healthdata.cli` - read-only lookups: claim, member, plan, procedure, diagnosis,
  plus whole-store `reconcile`, `origins` and `bands`
- `scripts/daily_update.py` - one update round: fresh synthetic batch, quality
  gates, regenerated report. Each run adds a new sequenced batch (claim ids
  carry a -Bnn- segment), so multiple rounds a day all bring new data;
  pipeline dedupe still prevents double-ingesting an identical batch

## Try it

```bash
pip install -r requirements.txt
python examples/quick_demo.py       # 500 synthetic claims through the pipeline
python scripts/daily_update.py      # full update round with quality gates (adds one synthetic batch per run)
python scripts/daily_update.py --report-only   # regenerate report and charts only; no new batch, safe to repeat
python scripts/query.py member MBR-0076   # claim / member / plan / procedure / diagnosis lookups
python scripts/query.py reconcile         # do all views account for the store? (exit 2 if not)
python scripts/query.py denials           # denial categories and denied dollars by plan
python scripts/query.py gates             # run every quality gate against the store (exit 2 if any fails)
python scripts/query.py origins           # claims per data_origin; also: bands, summary
python -m pytest                    # offline test suite
```

The latest generated report lives at
[reports/claims_report.md](reports/claims_report.md).

## Data

**Provenance.** The store has a `data_origin` column. On 2026-11-21 older synthetic
history was repaired in place: early batches gave one member different plans and age
bands on different claims, and some pediatric rows carried adult-only procedures.
Repaired rows are tagged `regenerated-2026-11-21` (billed re-drawn in the procedure's
range for changed procedures, allowed/paid ratios and denial status kept); claims
generated under the current rules are `generated`. Earlier per-member and per-plan
figures from before that date are superseded. The report lists the counts.
The tag is conservative, not an exact count of changed rows: the plan/age fix was
identified by diffing against the pre-fix snapshot, and all of batch B05 (ingested
just before the fix, so absent from that snapshot) is tagged, even if a few of its
rows already matched.

**Duplicate denials (2026-11-22).** "duplicate claim" used to be drawn at random, so
most such denials had no earlier matching claim. The generator now assigns it only to
deliberate repeats of an earlier claim in the same batch (about 3% of claims, ~70%
denied as duplicate, the rest paid). Older unsupported denials were reassigned another
reason (suffix `+2026-11-22` or tag `regenerated-2026-11-22` in `data_origin`), and a
new gate checks that every duplicate denial has an earlier matching claim. Older
repeats in the history are chance collisions, not designed duplicates.

**What the labels mean.** Plan type and age band are labels only. Nothing here
implements plan-specific benefits, deductibles, networks or adjudication, and the
age plausibility rule is a tiny illustrative filter, not clinical realism.

All synthetic, from `healthdata.claims.ClaimGenerator` with a fixed seed per
run. Amounts follow simple rules (paid <= allowed <= billed; denied claims pay
nothing) so the marts and quality checks have realistic invariants to enforce.
The procedure/diagnosis codes, plan types, denial reasons and payment rules are
illustrative teaching examples - they are not authoritative coding, coverage
or adjudication logic, and nothing here is medical, financial or insurance
advice.

## Service dates

Daily batches spread service dates over the trailing 90 days, and older single-date batches were
redistributed once (provenance tag `+2026-11-23`, a quality gate caps any month at 50% of claims).
Monthly figures are generator-shaped, not evidence of utilization trends. Details and before/after
metrics: [docs/service-date-redistribution.md](docs/service-date-redistribution.md).

## Committing

`scripts/safe_commit.sh "message"` runs the test suite and commits only if it passes (fail-closed: a failing test, a collection error or no passing tests blocks the commit). It does not push.
