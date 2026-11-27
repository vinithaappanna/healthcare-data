# Healthcare Data - claims pipeline report

Generated 2026-11-27 08:55 UTC. All data is synthetic - no real member, patient or plan information.

**6980 claims** in store. Billed $17,441,826, paid $9,880,982, denied 911 overall.

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
| 2026-08 | 639 | $1,661,794 | $1,274,504 | $939,646 | 12.0% |
| 2026-09 | 2209 | $5,434,393 | $4,173,260 | $3,160,152 | 13.3% |
| 2026-10 | 2227 | $5,270,526 | $3,983,449 | $2,925,280 | 13.8% |
| 2026-11 | 1551 | $4,173,603 | $3,185,662 | $2,277,542 | 12.8% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.6% |
| 2026-01 | 31 | 0.4% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.6% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 639 | 9.2% |
| 2026-09 | 2209 | 31.6% |
| 2026-10 (largest) | 2227 | 31.9% |
| 2026-11 | 1551 | 22.2% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1224 | $2,597 | $1,831,519 | 12.2% |
| R51 | Headache | 1255 | $2,612 | $1,748,945 | 13.3% |
| Z00.00 | General adult medical exam | 909 | $3,030 | $1,639,655 | 13.8% |
| E11.9 | Type 2 diabetes without complications | 1175 | $2,377 | $1,584,210 | 13.0% |
| M54.5 | Low back pain | 1205 | $2,224 | $1,560,278 | 12.9% |
| J06.9 | Acute upper respiratory infection | 1212 | $2,276 | $1,516,375 | 13.4% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| J06.9 | 93000 | 150 | 13.3% | $8,774 |
| R51 | 80053 | 148 | 12.2% | $7,004 |
| R51 | 93000 | 147 | 8.2% | $8,819 |
| M54.5 | 80053 | 138 | 11.6% | $6,210 |
| R51 | 43239 | 138 | 16.7% | $155,832 |
| E11.9 | 93000 | 134 | 16.4% | $7,431 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5386 | 77.2% | $13,112,684 | $8,589,910 |
| adjusted | 683 | 9.8% | $2,023,339 | $1,291,072 |
| denied | 911 | 13.1% | $2,305,804 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 293 | missing prior authorization | 26.6% |
| 2026-10 | 307 | missing prior authorization | 28.3% |
| 2026-11 | 199 | out-of-network provider | 24.6% |

## Denial reasons

- missing prior authorization (219)
- out-of-network provider (219)
- timely filing exceeded (212)
- not medically necessary (211)
- duplicate claim (50)

## Plan mix

- EPO: 1797
- HDHP: 1732
- HMO: 1729
- PPO: 1722

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1797 | 13.0% | 55.5% |
| HDHP | 1732 | 13.1% | 60.3% |
| HMO | 1729 | 13.8% | 56.2% |
| PPO | 1722 | 12.4% | 54.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1509 | 23.7% | 15.7% |
| HMO | 1491 | 23.1% | 15.6% |
| EPO | 1563 | 23.8% | 15.1% |
| HDHP | 1506 | 21.6% | 14.7% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 6980 claims: chi2 = 1.484, df = 3, p = 0.6861. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1722 | 12.4% | 697,815.75 | 15.9% |
| EPO | 1797 | 13.0% | 608,804.82 | 14.3% |
| HMO | 1729 | 13.8% | 515,376.17 | 13.3% |
| HDHP | 1732 | 13.1% | 483,807.10 | 9.9% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 431 | 47.3% | 1,137,210.10 |
| network / coverage | 219 | 24.0% | 511,537.25 |
| clinical review | 211 | 23.2% | 521,696.60 |
| billing error | 50 | 5.5% | 135,359.89 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5386 | 5386 | 84.9% | 77.5% |
| adjusted | 683 | 683 | 84.6% | 77.8% |
| denied | 911 | 862 | 0.0% | 77.3% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 219 | $583,164 | 25.3% | $2,663 |
| timely filing exceeded | 212 | $554,047 | 24.0% | $2,613 |
| not medically necessary | 211 | $521,697 | 22.6% | $2,472 |
| out-of-network provider | 219 | $511,537 | 22.2% | $2,336 |
| duplicate claim | 50 | $135,360 | 5.9% | $2,707 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 159 (168 later claims)
- Later claims denied as duplicate: 50
- Later claims still paid: 108 ($215,060 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 233 | 12.1% | $278,441 | 2.8% |
| 2 claims | 358 | 18.6% | $834,580 | 8.5% |
| 3 claims | 416 | 21.6% | $1,809,163 | 18.3% |
| 4+ claims | 923 | 47.8% | $6,958,797 | 70.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2053 | 29.4% | $80,461 | 0.8% | 13.0% |
| $100-$999 | 3233 | 46.3% | $585,705 | 5.9% | 13.2% |
| $1,000-$9,999 | 1118 | 16.0% | $1,124,936 | 11.4% | 12.7% |
| $10,000+ | 576 | 8.2% | $8,089,879 | 81.9% | 13.4% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,980 | 6,980 | yes |
| claims: plan mix | 6,980 | 6,980 | yes |
| claims: plan performance | 6,980 | 6,980 | yes |
| claims: age bands | 6,980 | 6,980 | yes |
| claims: cost per member | 6,980 | 6,980 | yes |
| paid $: monthly view | 9,880,982.08 | 9,880,982.08 | yes |
| paid $: age bands | 9,880,962.84 | 9,880,982.08 | yes |
| denied claims: reasons | 911 | 911 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1843 |
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
| HDHP | 458 | 1732 | 3.78 | $6,447 |
| PPO | 488 | 1722 | 3.53 | $4,879 |
| EPO | 495 | 1797 | 3.63 | $4,783 |
| HMO | 489 | 1729 | 3.54 | $4,456 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0203 | 7 | 4 | 57.1% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1120 | 10 | 4 | 40.0% |
| MBR-0093 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 499 | $12,397,639 | $9,535,664 | 76.9% |
| 43239 | 623 | $1,280,731 | $988,834 | 77.2% |
| 85025 | 601 | $31,847 | $24,634 | 77.3% |
| 97110 | 573 | $68,718 | $53,199 | 77.4% |
| 99214 | 600 | $100,447 | $77,773 | 77.4% |
| 99213 | 626 | $75,422 | $58,432 | 77.5% |

## Paid-amount concentration

Share of total paid (6980 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 70 | 17.2% |
| top 5% | 349 | 65.0% |
| top 10% | 698 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 219 | 70450 (12%), 85025 (12%), 97110 (11%) |
| out-of-network provider | 219 | 93000 (14%), 80053 (14%), 99285 (11%) |
| timely filing exceeded | 212 | 93000 (13%), 99213 (11%), 85025 (11%) |

## Data quality gates

12 of 12 checks passed on this run.

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
| status vocabulary and ids | 0 | pass |
| data origin tags | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 576 | $24,843 | $8,089,879 | 13.4% |
| 43239 | 718 | $2,045 | $833,777 | 13.2% |
| 99285 | 722 | $1,057 | $438,263 | 13.0% |
| 70450 | 687 | $650 | $259,238 | 12.2% |
| 99214 | 688 | $168 | $66,042 | 12.8% |

## Member utilization

1339 of 1930 synthetic members have 3+ claims and account for 88.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0844 | 10 | $2,703 |
| MBR-1120 | 10 | $2,050 |
| MBR-1467 | 10 | $1,872 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 234 | out-of-network provider | 58 |
| HDHP | 226 | missing prior authorization | 61 |
| HMO | 238 | not medically necessary | 60 |
| PPO | 213 | missing prior authorization | 55 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1797 | 13.0% | 11.5% to 14.7% | no |
| HDHP | 1732 | 13.1% | 11.5% to 14.7% | no |
| HMO | 1729 | 13.8% | 12.2% to 15.5% | no |
| PPO | 1722 | 12.4% | 10.9% to 14.0% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $229 | $1,305 | $1,423 | $1,611 | $1,593 | $1,837 |
| HDHP | $335 | $2,041 | $1,658 | $1,577 | $2,027 | $2,597 |
| HMO | $272 | $1,741 | $1,632 | $1,345 | $1,361 | $1,403 |
| PPO | $260 | $1,407 | $1,751 | $1,354 | $1,629 | $1,794 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1339). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 747 | 55.8% |
| 1 denial | 421 | 31.4% |
| 2+ denials | 171 | 12.8% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1197 | 129 | 10.8% | out-of-network provider |
| 18-29 | 1067 | 134 | 12.6% | timely filing exceeded |
| 30-44 | 1173 | 163 | 13.9% | not medically necessary |
| 45-59 | 1152 | 148 | 12.8% | out-of-network provider |
| 60-74 | 1207 | 158 | 13.1% | not medically necessary |
| 75+ | 1184 | 179 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1259.6% | +1214.9% | +3.54 pp |
| 2026-09 | +245.7% | +236.3% | +1.21 pp |
| 2026-10 | +0.8% | -7.4% | +0.53 pp |

## Potential duplicate services

159 groups share a member, procedure and service date (review queue, not a quality failure).

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
