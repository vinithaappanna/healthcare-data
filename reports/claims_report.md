# Healthcare Data - claims pipeline report

Generated 2026-11-26 22:54 UTC. All data is synthetic - no real member, patient or plan information.

**6860 claims** in store. Billed $17,089,473, paid $9,655,766, denied 898 overall.

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
| 2026-08 | 636 | $1,660,068 | $1,272,996 | $938,265 | 12.1% |
| 2026-09 | 2160 | $5,284,899 | $4,050,119 | $3,074,939 | 13.4% |
| 2026-10 | 2185 | $5,132,406 | $3,874,132 | $2,832,122 | 13.8% |
| 2026-11 | 1525 | $4,110,590 | $3,134,784 | $2,232,077 | 12.8% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.6% |
| 2026-01 | 31 | 0.4% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.7% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 636 | 9.3% |
| 2026-09 | 2160 | 31.5% |
| 2026-10 (largest) | 2185 | 31.9% |
| 2026-11 | 1525 | 22.2% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1199 | $2,592 | $1,784,313 | 12.4% |
| R51 | Headache | 1234 | $2,605 | $1,716,603 | 13.4% |
| Z00.00 | General adult medical exam | 895 | $3,013 | $1,593,248 | 13.7% |
| E11.9 | Type 2 diabetes without complications | 1152 | $2,392 | $1,577,683 | 13.0% |
| M54.5 | Low back pain | 1191 | $2,224 | $1,542,851 | 12.9% |
| J06.9 | Acute upper respiratory infection | 1189 | $2,242 | $1,441,068 | 13.2% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 147 | 12.2% | $6,953 |
| J06.9 | 93000 | 145 | 13.8% | $8,489 |
| R51 | 93000 | 145 | 8.3% | $8,657 |
| M54.5 | 80053 | 137 | 11.7% | $6,167 |
| R51 | 43239 | 136 | 16.2% | $154,495 |
| E11.9 | 93000 | 131 | 16.0% | $7,261 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5286 | 77.1% | $12,799,325 | $8,369,833 |
| adjusted | 676 | 9.8% | $2,016,113 | $1,285,933 |
| denied | 898 | 13.1% | $2,274,035 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 289 | missing prior authorization | 27.0% |
| 2026-10 | 302 | missing prior authorization | 28.5% |
| 2026-11 | 195 | out-of-network provider | 24.6% |

## Denial reasons

- missing prior authorization (217)
- out-of-network provider (215)
- timely filing exceeded (209)
- not medically necessary (208)
- duplicate claim (49)

## Plan mix

- EPO: 1761
- HMO: 1707
- HDHP: 1696
- PPO: 1696

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1761 | 13.0% | 55.5% |
| HMO | 1707 | 13.7% | 56.5% |
| HDHP | 1696 | 13.2% | 59.7% |
| PPO | 1696 | 12.5% | 54.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1473 | 23.1% | 15.7% |
| PPO | 1484 | 23.7% | 15.7% |
| EPO | 1533 | 23.7% | 15.1% |
| HDHP | 1472 | 21.9% | 14.9% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 6860 claims: chi2 = 1.145, df = 3, p = 0.7663. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1696 | 12.5% | 697,675.29 | 16.1% |
| EPO | 1761 | 13.0% | 605,299.32 | 14.3% |
| HMO | 1707 | 13.7% | 487,921.78 | 12.9% |
| HDHP | 1696 | 13.2% | 483,138.95 | 10.2% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 426 | 47.4% | 1,108,059.09 |
| network / coverage | 215 | 23.9% | 510,720.49 |
| clinical review | 208 | 23.2% | 519,958.57 |
| billing error | 49 | 5.5% | 135,297.19 |

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5286 | 5286 | 84.9% | 77.5% |
| adjusted | 676 | 676 | 84.5% | 77.8% |
| denied | 898 | 850 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 217 | $582,968 | 25.6% | $2,686 |
| timely filing exceeded | 209 | $525,091 | 23.1% | $2,512 |
| not medically necessary | 208 | $519,959 | 22.9% | $2,500 |
| out-of-network provider | 215 | $510,720 | 22.5% | $2,375 |
| duplicate claim | 49 | $135,297 | 5.9% | $2,761 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 157 (166 later claims)
- Later claims denied as duplicate: 49
- Later claims still paid: 107 ($214,506 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 234 | 12.2% | $279,901 | 2.9% |
| 2 claims | 380 | 19.8% | $971,963 | 10.1% |
| 3 claims | 409 | 21.3% | $1,697,568 | 17.6% |
| 4+ claims | 901 | 46.8% | $6,706,334 | 69.5% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2018 | 29.4% | $79,062 | 0.8% | 13.0% |
| $100-$999 | 3181 | 46.4% | $575,541 | 6.0% | 13.2% |
| $1,000-$9,999 | 1098 | 16.0% | $1,105,982 | 11.5% | 12.8% |
| $10,000+ | 563 | 8.2% | $7,895,181 | 81.8% | 13.5% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,860 | 6,860 | yes |
| claims: plan mix | 6,860 | 6,860 | yes |
| claims: plan performance | 6,860 | 6,860 | yes |
| claims: age bands | 6,860 | 6,860 | yes |
| claims: cost per member | 6,860 | 6,860 | yes |
| paid $: monthly view | 9,655,765.91 | 9,655,765.91 | yes |
| paid $: age bands | 9,655,767.04 | 9,655,765.91 | yes |
| denied claims: reasons | 898 | 898 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1723 |
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
| HDHP | 457 | 1696 | 3.71 | $6,172 |
| PPO | 487 | 1696 | 3.48 | $4,822 |
| EPO | 493 | 1761 | 3.57 | $4,765 |
| HMO | 487 | 1707 | 3.51 | $4,390 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0203 | 7 | 4 | 57.1% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1120 | 10 | 4 | 40.0% |
| MBR-0825 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 487 | $12,122,261 | $9,314,449 | 76.8% |
| 43239 | 615 | $1,264,541 | $975,703 | 77.2% |
| 85025 | 592 | $31,367 | $24,286 | 77.4% |
| 99213 | 619 | $74,562 | $57,741 | 77.4% |
| 97110 | 561 | $67,324 | $52,170 | 77.5% |
| 99214 | 588 | $98,303 | $76,204 | 77.5% |

## Paid-amount concentration

Share of total paid (6860 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 69 | 17.2% |
| top 5% | 343 | 65.2% |
| top 10% | 686 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 217 | 70450 (12%), 85025 (12%), 97110 (12%) |
| out-of-network provider | 215 | 93000 (14%), 80053 (13%), 99285 (12%) |
| timely filing exceeded | 209 | 93000 (13%), 99213 (11%), 85025 (11%) |

## Data quality gates

11 of 11 checks passed on this run.

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

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 563 | $24,879 | $7,895,181 | 13.5% |
| 43239 | 708 | $2,047 | $822,391 | 13.1% |
| 99285 | 702 | $1,059 | $425,362 | 13.4% |
| 70450 | 683 | $649 | $257,516 | 12.2% |
| 99214 | 674 | $168 | $64,677 | 12.8% |

## Member utilization

1310 of 1924 synthetic members have 3+ claims and account for 87.0% of paid dollars.

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
| EPO | 228 | out-of-network provider | 57 |
| HDHP | 224 | missing prior authorization | 61 |
| HMO | 234 | not medically necessary | 60 |
| PPO | 212 | missing prior authorization | 55 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1761 | 13.0% | 11.5% to 14.6% | no |
| HMO | 1707 | 13.7% | 12.2% to 15.4% | no |
| HDHP | 1696 | 13.2% | 11.7% to 14.9% | no |
| PPO | 1696 | 12.5% | 11.0% to 14.2% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $232 | $1,318 | $1,440 | $1,637 | $1,595 | $1,866 |
| HDHP | $337 | $1,881 | $1,584 | $1,519 | $2,020 | $2,642 |
| HMO | $270 | $1,764 | $1,641 | $1,310 | $1,338 | $1,385 |
| PPO | $262 | $1,419 | $1,707 | $1,372 | $1,639 | $1,800 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1310). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 727 | 55.5% |
| 1 denial | 417 | 31.8% |
| 2+ denials | 166 | 12.7% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1174 | 125 | 10.7% | missing prior authorization |
| 18-29 | 1050 | 134 | 12.8% | timely filing exceeded |
| 30-44 | 1156 | 161 | 13.9% | not medically necessary |
| 45-59 | 1132 | 146 | 12.9% | out-of-network provider |
| 60-74 | 1187 | 156 | 13.1% | not medically necessary |
| 75+ | 1161 | 176 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1253.2% | +1213.0% | +3.60 pp |
| 2026-09 | +239.6% | +227.7% | +1.27 pp |
| 2026-10 | +1.2% | -7.9% | +0.44 pp |

## Potential duplicate services

157 groups share a member, procedure and service date (review queue, not a quality failure).

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
