# Healthcare Data - claims pipeline report

Generated 2026-11-25 01:47 UTC. All data is synthetic - no real member, patient or plan information.

**5960 claims** in store. Billed $14,820,132, paid $8,399,518, denied 780 overall.

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
| 2026-08 | 594 | $1,562,470 | $1,196,738 | $878,934 | 12.1% |
| 2026-09 | 1866 | $4,531,768 | $3,479,517 | $2,632,982 | 13.5% |
| 2026-10 | 1870 | $4,370,069 | $3,302,503 | $2,443,198 | 13.9% |
| 2026-11 | 1276 | $3,454,314 | $2,613,152 | $1,866,041 | 12.8% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.7% |
| 2026-01 | 31 | 0.5% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.8% |
| 2026-04 | 48 | 0.8% |
| 2026-05 | 43 | 0.7% |
| 2026-06 | 46 | 0.8% |
| 2026-07 | 47 | 0.8% |
| 2026-08 | 594 | 10.0% |
| 2026-09 | 1866 | 31.3% |
| 2026-10 (largest) | 1870 | 31.4% |
| 2026-11 | 1276 | 21.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1045 | $2,649 | $1,594,636 | 12.4% |
| R51 | Headache | 1076 | $2,505 | $1,421,802 | 13.9% |
| Z00.00 | General adult medical exam | 769 | $2,988 | $1,386,742 | 14.2% |
| J06.9 | Acute upper respiratory infection | 1040 | $2,377 | $1,357,606 | 12.9% |
| M54.5 | Low back pain | 1021 | $2,242 | $1,331,075 | 12.6% |
| E11.9 | Type 2 diabetes without complications | 1009 | $2,277 | $1,307,656 | 12.9% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 126 | 8.7% | $7,334 |
| J06.9 | 93000 | 124 | 14.5% | $7,132 |
| R51 | 80053 | 123 | 11.4% | $5,885 |
| M54.5 | 99285 | 120 | 15.8% | $73,322 |
| R51 | 43239 | 114 | 17.5% | $124,194 |
| E11.9 | 99213 | 113 | 15.9% | $7,415 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4588 | 77.0% | $11,121,575 | $7,285,886 |
| adjusted | 591 | 9.9% | $1,736,181 | $1,113,632 |
| denied | 781 | 13.1% | $1,962,375 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 72 | not medically necessary | 27.8% |
| 2026-09 | 251 | missing prior authorization | 27.9% |
| 2026-10 | 259 | missing prior authorization | 27.0% |
| 2026-11 | 164 | timely filing exceeded | 25.6% |

## Denial reasons

- out-of-network provider (187)
- missing prior authorization (186)
- timely filing exceeded (186)
- not medically necessary (185)
- duplicate claim (37)

## Plan mix

- EPO: 1518
- HMO: 1488
- HDHP: 1477
- PPO: 1477

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1518 | 13.4% | 55.4% |
| HMO | 1488 | 14.1% | 56.3% |
| HDHP | 1477 | 12.8% | 59.6% |
| PPO | 1477 | 12.1% | 55.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1279 | 22.7% | 15.6% |
| PPO | 1298 | 24.2% | 15.4% |
| HDHP | 1288 | 22.0% | 14.9% |
| EPO | 1314 | 23.4% | 14.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 186 | $502,520 | 25.6% | $2,702 |
| not medically necessary | 185 | $488,962 | 24.9% | $2,643 |
| timely filing exceeded | 186 | $449,630 | 22.9% | $2,417 |
| out-of-network provider | 187 | $389,797 | 19.9% | $2,084 |
| duplicate claim | 37 | $131,466 | 6.7% | $3,553 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 135 (144 later claims)
- Later claims denied as duplicate: 37
- Later claims still paid: 97 ($211,053 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 305 | 16.2% | $294,965 | 3.5% |
| 2 claims | 436 | 23.2% | $1,154,362 | 13.7% |
| 3 claims | 432 | 23.0% | $1,847,304 | 22.0% |
| 4+ claims | 708 | 37.6% | $5,102,888 | 60.8% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1748 | 29.3% | $68,863 | 0.8% | 12.7% |
| $100-$999 | 2758 | 46.3% | $501,006 | 6.0% | 13.4% |
| $1,000-$9,999 | 964 | 16.2% | $957,282 | 11.4% | 12.9% |
| $10,000+ | 490 | 8.2% | $6,872,367 | 81.8% | 13.3% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,960 | 5,960 | yes |
| claims: plan mix | 5,960 | 5,960 | yes |
| claims: plan performance | 5,960 | 5,960 | yes |
| claims: age bands | 5,960 | 5,960 | yes |
| claims: cost per member | 5,960 | 5,960 | yes |
| paid $: monthly view | 8,399,517.76 | 8,399,517.76 | yes |
| paid $: age bands | 8,399,522.94 | 8,399,517.76 | yes |
| denied claims: reasons | 781 | 781 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 823 |
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
| HDHP | 450 | 1477 | 3.28 | $5,633 |
| PPO | 478 | 1477 | 3.09 | $4,497 |
| EPO | 480 | 1518 | 3.16 | $4,156 |
| HMO | 473 | 1488 | 3.15 | $3,637 |

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
| 43239 | 523 | $1,074,240 | $823,234 | 76.6% |
| 27447 | 425 | $10,515,484 | $8,089,656 | 76.9% |
| 99213 | 538 | $64,709 | $50,025 | 77.3% |
| 85025 | 515 | $27,453 | $21,267 | 77.5% |
| 99214 | 521 | $87,054 | $67,441 | 77.5% |
| 93000 | 554 | $55,377 | $42,914 | 77.5% |

## Paid-amount concentration

Share of total paid (5960 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 60 | 17.1% |
| top 5% | 298 | 65.0% |
| top 10% | 596 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 187 | 80053 (13%), 99285 (13%), 93000 (12%) |
| missing prior authorization | 186 | 85025 (12%), 99285 (12%), 70450 (12%) |
| timely filing exceeded | 186 | 99213 (13%), 93000 (12%), 97110 (10%) |

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
| 27447 | 490 | $24,762 | $6,872,367 | 13.3% |
| 43239 | 602 | $2,047 | $694,409 | 13.1% |
| 99285 | 639 | $1,065 | $387,368 | 14.1% |
| 70450 | 597 | $650 | $224,803 | 12.1% |
| 99214 | 595 | $168 | $57,332 | 12.4% |

## Member utilization

1140 of 1881 synthetic members have 3+ claims and account for 82.8% of paid dollars.

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
| EPO | 204 | out-of-network provider | 50 |
| HDHP | 189 | missing prior authorization | 50 |
| HMO | 209 | not medically necessary | 53 |
| PPO | 179 | not medically necessary | 45 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1518 | 13.4% | 11.8% to 15.2% | no |
| HMO | 1488 | 14.1% | 12.4% to 15.9% | no |
| HDHP | 1477 | 12.8% | 11.2% to 14.6% | no |
| PPO | 1477 | 12.1% | 10.5% to 13.9% | no |

## Member denial experience

Members with 3+ claims (1140). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 658 | 57.7% |
| 1 denial | 355 | 31.1% |
| 2+ denials | 127 | 11.1% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1017 | 110 | 10.8% | missing prior authorization |
| 18-29 | 923 | 118 | 12.8% | timely filing exceeded |
| 30-44 | 1009 | 138 | 13.7% | not medically necessary |
| 45-59 | 978 | 131 | 13.4% | out-of-network provider |
| 60-74 | 1032 | 126 | 12.2% | not medically necessary |
| 75+ | 1001 | 158 | 15.8% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1163.8% | +1130.0% | +3.61 pp |
| 2026-09 | +214.1% | +199.6% | +1.33 pp |
| 2026-10 | +0.2% | -7.2% | +0.40 pp |

## Potential duplicate services

135 groups share a member, procedure and service date (review queue, not a quality failure).

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
