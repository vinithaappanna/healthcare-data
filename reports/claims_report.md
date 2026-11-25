# Healthcare Data - claims pipeline report

Generated 2026-11-25 06:47 UTC. All data is synthetic - no real member, patient or plan information.

**6140 claims** in store. Billed $15,298,027, paid $8,661,478, denied 806 overall.

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
| 2026-08 | 600 | $1,566,593 | $1,199,462 | $879,969 | 12.3% |
| 2026-09 | 1924 | $4,647,094 | $3,567,360 | $2,702,103 | 13.5% |
| 2026-10 | 1938 | $4,589,936 | $3,464,332 | $2,539,827 | 14.0% |
| 2026-11 | 1324 | $3,592,894 | $2,729,121 | $1,961,216 | 12.5% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.7% |
| 2026-01 | 31 | 0.5% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.7% |
| 2026-04 | 48 | 0.8% |
| 2026-05 | 43 | 0.7% |
| 2026-06 | 46 | 0.8% |
| 2026-07 | 47 | 0.8% |
| 2026-08 | 600 | 9.8% |
| 2026-09 | 1924 | 31.3% |
| 2026-10 (largest) | 1938 | 31.6% |
| 2026-11 | 1324 | 21.6% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1078 | $2,642 | $1,648,332 | 12.7% |
| R51 | Headache | 1109 | $2,516 | $1,477,962 | 13.8% |
| Z00.00 | General adult medical exam | 790 | $3,036 | $1,432,281 | 13.9% |
| J06.9 | Acute upper respiratory infection | 1070 | $2,387 | $1,388,582 | 12.9% |
| M54.5 | Low back pain | 1054 | $2,219 | $1,362,389 | 12.9% |
| E11.9 | Type 2 diabetes without complications | 1039 | $2,280 | $1,351,931 | 12.7% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 129 | 8.5% | $7,528 |
| J06.9 | 93000 | 126 | 14.3% | $7,276 |
| R51 | 80053 | 125 | 11.2% | $5,988 |
| M54.5 | 99285 | 121 | 16.5% | $73,322 |
| E11.9 | 99213 | 117 | 15.4% | $7,732 |
| M54.5 | 80053 | 117 | 12.0% | $5,224 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4727 | 77.0% | $11,476,062 | $7,514,835 |
| adjusted | 607 | 9.9% | $1,788,184 | $1,146,643 |
| denied | 806 | 13.1% | $2,033,780 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 74 | timely filing exceeded | 28.4% |
| 2026-09 | 259 | missing prior authorization | 28.6% |
| 2026-10 | 272 | missing prior authorization | 27.9% |
| 2026-11 | 166 | timely filing exceeded | 25.3% |

## Denial reasons

- missing prior authorization (197)
- out-of-network provider (190)
- not medically necessary (190)
- timely filing exceeded (189)
- duplicate claim (40)

## Plan mix

- EPO: 1571
- HMO: 1537
- PPO: 1517
- HDHP: 1515

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1571 | 13.5% | 55.0% |
| HMO | 1537 | 14.1% | 56.7% |
| PPO | 1517 | 12.2% | 54.8% |
| HDHP | 1515 | 12.7% | 59.6% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1332 | 24.0% | 15.6% |
| HMO | 1321 | 22.8% | 15.3% |
| HDHP | 1322 | 21.9% | 15.1% |
| EPO | 1359 | 23.4% | 14.7% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 197 | $534,223 | 26.3% | $2,712 |
| not medically necessary | 190 | $490,004 | 24.1% | $2,579 |
| timely filing exceeded | 189 | $483,672 | 23.8% | $2,559 |
| out-of-network provider | 190 | $394,115 | 19.4% | $2,074 |
| duplicate claim | 40 | $131,767 | 6.5% | $3,294 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 138 (147 later claims)
- Later claims denied as duplicate: 40
- Later claims still paid: 97 ($211,053 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 287 | 15.2% | $292,216 | 3.4% |
| 2 claims | 429 | 22.7% | $1,162,059 | 13.4% |
| 3 claims | 427 | 22.6% | $1,778,181 | 20.5% |
| 4+ claims | 749 | 39.6% | $5,429,022 | 62.7% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1804 | 29.4% | $71,152 | 0.8% | 12.6% |
| $100-$999 | 2837 | 46.2% | $515,281 | 5.9% | 13.5% |
| $1,000-$9,999 | 994 | 16.2% | $986,717 | 11.4% | 13.0% |
| $10,000+ | 505 | 8.2% | $7,088,327 | 81.8% | 13.3% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,140 | 6,140 | yes |
| claims: plan mix | 6,140 | 6,140 | yes |
| claims: plan performance | 6,140 | 6,140 | yes |
| claims: age bands | 6,140 | 6,140 | yes |
| claims: cost per member | 6,140 | 6,140 | yes |
| paid $: monthly view | 8,661,478.15 | 8,661,478.15 | yes |
| paid $: age bands | 8,661,473.55 | 8,661,478.15 | yes |
| denied claims: reasons | 806 | 806 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1003 |
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
| HDHP | 452 | 1515 | 3.35 | $5,752 |
| PPO | 479 | 1517 | 3.17 | $4,611 |
| EPO | 485 | 1571 | 3.24 | $4,226 |
| HMO | 476 | 1537 | 3.23 | $3,788 |

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
| 43239 | 540 | $1,108,484 | $848,993 | 76.6% |
| 27447 | 438 | $10,853,417 | $8,352,608 | 77.0% |
| 99213 | 554 | $66,623 | $51,552 | 77.4% |
| 93000 | 576 | $57,477 | $44,515 | 77.5% |
| 85025 | 528 | $28,132 | $21,794 | 77.5% |
| 70450 | 540 | $352,453 | $273,306 | 77.5% |

## Paid-amount concentration

Share of total paid (6140 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 62 | 17.1% |
| top 5% | 307 | 65.0% |
| top 10% | 614 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 197 | 85025 (12%), 70450 (12%), 99285 (12%) |
| not medically necessary | 190 | 93000 (14%), 43239 (13%), 99285 (12%) |
| out-of-network provider | 190 | 80053 (13%), 99285 (13%), 93000 (12%) |

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
| 27447 | 505 | $24,811 | $7,088,327 | 13.3% |
| 43239 | 624 | $2,044 | $716,912 | 13.5% |
| 99285 | 654 | $1,064 | $397,656 | 13.9% |
| 70450 | 614 | $649 | $231,066 | 12.0% |
| 99214 | 617 | $168 | $59,333 | 12.8% |

## Member utilization

1176 of 1892 synthetic members have 3+ claims and account for 83.2% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-0961 | 9 | $3,263 |
| MBR-0844 | 9 | $2,678 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 212 | out-of-network provider | 51 |
| HDHP | 193 | missing prior authorization | 52 |
| HMO | 216 | not medically necessary | 55 |
| PPO | 185 | missing prior authorization | 48 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1571 | 13.5% | 11.9% to 15.3% | no |
| HMO | 1537 | 14.1% | 12.4% to 15.9% | no |
| PPO | 1517 | 12.2% | 10.6% to 13.9% | no |
| HDHP | 1515 | 12.7% | 11.2% to 14.5% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $228 | $1,386 | $1,317 | $1,582 | $1,669 | $1,714 |
| HDHP | $347 | $1,939 | $1,662 | $1,561 | $2,036 | $2,712 |
| HMO | $268 | $1,558 | $1,471 | $1,242 | $1,342 | $1,332 |
| PPO | $265 | $1,495 | $1,715 | $1,467 | $1,740 | $1,923 |

## Member denial experience

Members with 3+ claims (1176). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 670 | 57.0% |
| 1 denial | 373 | 31.7% |
| 2+ denials | 133 | 11.3% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1042 | 111 | 10.7% | missing prior authorization |
| 18-29 | 950 | 120 | 12.6% | timely filing exceeded |
| 30-44 | 1049 | 149 | 14.2% | not medically necessary |
| 45-59 | 1005 | 132 | 13.1% | out-of-network provider |
| 60-74 | 1068 | 133 | 12.4% | not medically necessary |
| 75+ | 1026 | 161 | 15.7% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1176.6% | +1131.4% | +3.82 pp |
| 2026-09 | +220.7% | +207.1% | +1.13 pp |
| 2026-10 | +0.7% | -6.0% | +0.58 pp |

## Potential duplicate services

138 groups share a member, procedure and service date (review queue, not a quality failure).

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
