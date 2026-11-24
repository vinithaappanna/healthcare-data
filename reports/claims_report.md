# Healthcare Data - claims pipeline report

Generated 2026-11-24 00:43 UTC. All data is synthetic - no real member, patient or plan information.

**5360 claims** in store. Billed $13,383,828, paid $7,665,003, denied 701 overall.

## Monthly financials

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Billed | Allowed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2025-11 | 18 | $5,840 | $4,755 | $4,019 | 11.1% |
| 2025-12 | 44 | $45,779 | $36,033 | $31,423 | 9.1% |
| 2026-01 | 31 | $69,438 | $54,037 | $43,702 | 0.0% |
| 2026-02 | 32 | $69,848 | $53,159 | $26,265 | 12.5% |
| 2026-03 | 45 | $144,754 | $103,258 | $90,177 | 11.1% |
| 2026-04 | 48 | $109,782 | $90,132 | $76,083 | 8.3% |
| 2026-05 | 43 | $161,609 | $121,321 | $113,180 | 11.6% |
| 2026-06 | 46 | $186,994 | $150,110 | $122,054 | 15.2% |
| 2026-07 | 47 | $107,464 | $88,764 | $71,460 | 8.5% |
| 2026-08 | 562 | $1,487,927 | $1,142,634 | $835,217 | 12.1% |
| 2026-09 | 1647 | $4,015,238 | $3,098,396 | $2,357,434 | 13.8% |
| 2026-10 | 1668 | $3,896,739 | $2,965,856 | $2,205,240 | 13.9% |
| 2026-11 | 1129 | $3,082,414 | $2,331,965 | $1,688,749 | 12.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 937 | $2,684 | $1,452,793 | 12.7% |
| Z00.00 | General adult medical exam | 708 | $2,918 | $1,299,002 | 13.4% |
| R51 | Headache | 967 | $2,500 | $1,278,333 | 14.0% |
| M54.5 | Low back pain | 927 | $2,310 | $1,240,751 | 12.7% |
| J06.9 | Acute upper respiratory infection | 918 | $2,396 | $1,233,965 | 12.8% |
| E11.9 | Type 2 diabetes without complications | 903 | $2,265 | $1,160,160 | 13.0% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 116 | 8.6% | $6,634 |
| M54.5 | 99285 | 113 | 16.8% | $68,004 |
| R51 | 80053 | 110 | 12.7% | $5,218 |
| R51 | 43239 | 108 | 17.6% | $117,353 |
| J06.9 | 93000 | 107 | 15.9% | $5,990 |
| M54.5 | 80053 | 106 | 12.3% | $4,759 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4126 | 77.0% | $10,040,365 | $6,613,224 |
| adjusted | 532 | 9.9% | $1,646,930 | $1,051,779 |
| denied | 702 | 13.1% | $1,696,533 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 68 | not medically necessary | 27.9% |
| 2026-09 | 228 | missing prior authorization | 27.6% |
| 2026-10 | 231 | missing prior authorization | 26.4% |
| 2026-11 | 140 | not medically necessary | 25.0% |

## Denial reasons

- not medically necessary (171)
- out-of-network provider (170)
- missing prior authorization (168)
- timely filing exceeded (166)
- duplicate claim (27)

## Plan mix

- EPO: 1354
- PPO: 1346
- HMO: 1336
- HDHP: 1324

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1354 | 13.4% | 56.2% |
| PPO | 1346 | 12.0% | 54.6% |
| HMO | 1336 | 14.7% | 56.4% |
| HDHP | 1324 | 12.2% | 61.4% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1140 | 22.4% | 15.6% |
| PPO | 1184 | 24.0% | 15.4% |
| HDHP | 1162 | 22.0% | 14.7% |
| EPO | 1172 | 23.3% | 14.0% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 168 | $495,781 | 29.2% | $2,951 |
| not medically necessary | 171 | $446,925 | 26.3% | $2,614 |
| timely filing exceeded | 166 | $395,613 | 23.3% | $2,383 |
| out-of-network provider | 170 | $270,458 | 15.9% | $1,591 |
| duplicate claim | 27 | $87,756 | 5.2% | $3,250 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 120 (129 later claims)
- Later claims denied as duplicate: 27
- Later claims still paid: 92 ($208,044 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 384 | 20.8% | $354,627 | 4.6% |
| 2 claims | 461 | 25.0% | $1,284,880 | 16.8% |
| 3 claims | 411 | 22.3% | $1,858,066 | 24.2% |
| 4+ claims | 590 | 32.0% | $4,167,431 | 54.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1559 | 29.1% | $61,195 | 0.8% | 12.8% |
| $100-$999 | 2494 | 46.5% | $452,670 | 5.9% | 13.2% |
| $1,000-$9,999 | 865 | 16.1% | $854,672 | 11.2% | 13.5% |
| $10,000+ | 442 | 8.2% | $6,296,466 | 82.2% | 12.4% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,360 | 5,360 | yes |
| claims: plan mix | 5,360 | 5,360 | yes |
| claims: plan performance | 5,360 | 5,360 | yes |
| claims: age bands | 5,360 | 5,360 | yes |
| claims: cost per member | 5,360 | 5,360 | yes |
| paid $: monthly view | 7,665,003.37 | 7,665,003.37 | yes |
| paid $: age bands | 7,665,002.21 | 7,665,003.37 | yes |
| denied claims: reasons | 702 | 702 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 223 |
| regenerated-2026-11-21 | 553 |
| regenerated-2026-11-21+2026-11-22 | 12 |
| regenerated-2026-11-21+2026-11-22+2026-11-23 | 71 |
| regenerated-2026-11-21+2026-11-23 | 2667 |
| regenerated-2026-11-22 | 1 |
| regenerated-2026-11-22+2026-11-23 | 33 |
| regenerated-2026-11-23 | 1800 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 447 | 1324 | 2.96 | $5,145 |
| PPO | 465 | 1346 | 2.89 | $4,299 |
| EPO | 472 | 1354 | 2.87 | $3,812 |
| HMO | 462 | 1336 | 2.89 | $3,392 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0825 | 4 | 3 | 75.0% |
| MBR-0912 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 43239 | 471 | $964,365 | $740,685 | 76.8% |
| 27447 | 387 | $9,590,267 | $7,391,280 | 77.1% |
| 85025 | 462 | $24,590 | $18,993 | 77.2% |
| 99213 | 485 | $58,300 | $45,109 | 77.4% |
| 93000 | 495 | $49,409 | $38,258 | 77.4% |
| 99285 | 496 | $528,444 | $409,225 | 77.4% |

## Paid-amount concentration

Share of total paid (5360 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 54 | 16.9% |
| top 5% | 268 | 64.7% |
| top 10% | 536 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| not medically necessary | 171 | 43239 (14%), 99285 (13%), 93000 (12%) |
| out-of-network provider | 170 | 99285 (14%), 80053 (13%), 93000 (12%) |
| missing prior authorization | 168 | 99285 (13%), 85025 (12%), 70450 (11%) |

## Data quality gates

10 of 10 checks passed on this run.

| Check | Issues | Result |
| --- | ---: | --- |
| amount consistency | 0 | pass |
| denial reasons | 0 | pass |
| one member per claim | 0 | pass |
| billed within procedure range | 0 | pass |
| known diagnosis codes | 0 | pass |
| service dates | 0 | pass |
| member consistency | 0 | pass |
| age plausibility | 0 | pass |
| duplicate denials supported | 0 | pass |
| service month concentration | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 442 | $24,818 | $6,296,466 | 12.4% |
| 43239 | 545 | $2,039 | $625,058 | 13.6% |
| 99285 | 582 | $1,056 | $347,051 | 14.8% |
| 70450 | 524 | $650 | $197,213 | 12.0% |
| 99214 | 545 | $168 | $52,932 | 11.9% |

## Member utilization

1001 of 1846 synthetic members have 3+ claims and account for 78.6% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-0961 | 9 | $3,263 |
| MBR-0154 | 8 | $27,766 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 182 | out-of-network provider | 46 |
| HDHP | 162 | missing prior authorization | 45 |
| HMO | 196 | not medically necessary | 51 |
| PPO | 162 | not medically necessary | 43 |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1095.7% | +1068.8% | +3.59 pp |
| 2026-09 | +193.1% | +182.2% | +1.74 pp |
| 2026-10 | +1.3% | -6.5% | +0.01 pp |

## Potential duplicate services

120 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-10-13 | 3 | $55,302 |
| MBR-0743 | 27447 | 2026-08-29 | 2 | $54,807 |
| MBR-0076 | 27447 | 2026-10-19 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-02 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-08-30 | 2 | $33,395 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
