# Healthcare Data - claims pipeline report

Generated 2026-11-28 04:57 UTC. All data is synthetic - no real member, patient or plan information.

**7220 claims** in store. Billed $17,919,818, paid $10,183,485, denied 946 overall.

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
| 2026-08 | 643 | $1,662,210 | $1,274,811 | $939,923 | 12.0% |
| 2026-09 | 2288 | $5,572,364 | $4,276,669 | $3,240,811 | 13.1% |
| 2026-10 | 2305 | $5,414,526 | $4,087,436 | $3,016,229 | 13.9% |
| 2026-11 | 1630 | $4,369,208 | $3,351,171 | $2,408,159 | 13.1% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.2% |
| 2025-12 | 44 | 0.6% |
| 2026-01 | 31 | 0.4% |
| 2026-02 | 32 | 0.4% |
| 2026-03 | 45 | 0.6% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.6% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 643 | 8.9% |
| 2026-09 | 2288 | 31.7% |
| 2026-10 (largest) | 2305 | 31.9% |
| 2026-11 | 1630 | 22.6% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1266 | $2,554 | $1,873,800 | 12.1% |
| R51 | Headache | 1294 | $2,553 | $1,761,696 | 13.4% |
| Z00.00 | General adult medical exam | 937 | $3,001 | $1,686,702 | 13.7% |
| J06.9 | Acute upper respiratory infection | 1264 | $2,356 | $1,654,562 | 13.3% |
| E11.9 | Type 2 diabetes without complications | 1221 | $2,324 | $1,606,223 | 13.5% |
| M54.5 | Low back pain | 1238 | $2,225 | $1,600,503 | 12.8% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 155 | 12.9% | $7,215 |
| J06.9 | 93000 | 154 | 13.6% | $8,999 |
| R51 | 93000 | 151 | 8.0% | $9,076 |
| M54.5 | 80053 | 145 | 11.0% | $6,592 |
| R51 | 43239 | 145 | 17.2% | $163,777 |
| E11.9 | 93000 | 139 | 15.8% | $7,801 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5571 | 77.2% | $13,560,351 | $8,888,630 |
| adjusted | 703 | 9.7% | $2,029,370 | $1,294,855 |
| denied | 946 | 13.1% | $2,330,097 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 299 | missing prior authorization | 26.4% |
| 2026-10 | 321 | missing prior authorization | 28.7% |
| 2026-11 | 214 | out-of-network provider | 24.3% |

## Denial reasons

- missing prior authorization (228)
- out-of-network provider (223)
- not medically necessary (221)
- timely filing exceeded (215)
- duplicate claim (59)

## Plan mix

- EPO: 1847
- HDHP: 1797
- HMO: 1795
- PPO: 1781

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1847 | 13.3% | 55.5% |
| HDHP | 1797 | 13.2% | 60.2% |
| HMO | 1795 | 13.5% | 56.9% |
| PPO | 1781 | 12.4% | 54.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1560 | 23.6% | 15.9% |
| HMO | 1553 | 22.8% | 15.4% |
| EPO | 1601 | 23.8% | 15.2% |
| HDHP | 1560 | 21.7% | 14.7% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 7220 claims: chi2 = 1.067, df = 3, p = 0.7849. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Claims per member: dispersion

Across 1935 members with claims: mean 3.731, variance 3.474, variance-to-mean ratio 0.931. A ratio near 1 matches random assignment; well above 1 would mean claims cluster on a few members. The generator assigns members at random, so about 1 is expected. No enrollment data, so zero-claim members are invisible and this is indicative only.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1781 | 12.4% | 700,463.20 | 15.6% |
| EPO | 1847 | 13.3% | 620,156.12 | 14.1% |
| HMO | 1795 | 13.5% | 517,646.66 | 12.8% |
| HDHP | 1797 | 13.2% | 491,831.25 | 9.8% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 443 | 46.8% | 1,145,716.36 |
| network / coverage | 223 | 23.6% | 514,851.43 |
| clinical review | 221 | 23.4% | 528,384.29 |
| billing error | 59 | 6.2% | 141,145.15 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5571 | 5571 | 84.9% | 77.5% |
| adjusted | 703 | 703 | 84.5% | 77.8% |
| denied | 946 | 888 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 228 | $589,355 | 25.3% | $2,585 |
| timely filing exceeded | 215 | $556,362 | 23.9% | $2,588 |
| not medically necessary | 221 | $528,384 | 22.7% | $2,391 |
| out-of-network provider | 223 | $514,851 | 22.1% | $2,309 |
| duplicate claim | 59 | $141,145 | 6.1% | $2,392 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 170 (179 later claims)
- Later claims denied as duplicate: 59
- Later claims still paid: 110 ($215,205 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 205 | 10.6% | $254,129 | 2.5% |
| 2 claims | 358 | 18.5% | $782,845 | 7.7% |
| 3 claims | 392 | 20.3% | $1,667,821 | 16.4% |
| 4+ claims | 980 | 50.6% | $7,478,690 | 73.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2124 | 29.4% | $83,179 | 0.8% | 13.0% |
| $100-$999 | 3344 | 46.3% | $603,328 | 5.9% | 13.2% |
| $1,000-$9,999 | 1161 | 16.1% | $1,163,261 | 11.4% | 13.2% |
| $10,000+ | 591 | 8.2% | $8,333,717 | 81.8% | 13.0% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 7,220 | 7,220 | yes |
| claims: plan mix | 7,220 | 7,220 | yes |
| claims: plan performance | 7,220 | 7,220 | yes |
| claims: age bands | 7,220 | 7,220 | yes |
| claims: cost per member | 7,220 | 7,220 | yes |
| paid $: monthly view | 10,183,484.97 | 10,183,484.97 | yes |
| paid $: age bands | 10,183,484.53 | 10,183,484.97 | yes |
| denied claims: reasons | 946 | 946 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 2083 |
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
| HDHP | 460 | 1797 | 3.91 | $6,544 |
| PPO | 488 | 1781 | 3.65 | $4,987 |
| EPO | 495 | 1847 | 3.73 | $4,923 |
| HMO | 492 | 1795 | 3.65 | $4,680 |

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
| 27447 | 514 | $12,761,159 | $9,825,951 | 77.0% |
| 43239 | 643 | $1,325,449 | $1,023,185 | 77.2% |
| 85025 | 623 | $33,092 | $25,576 | 77.3% |
| 97110 | 594 | $71,355 | $55,223 | 77.4% |
| 99214 | 622 | $103,860 | $80,389 | 77.4% |
| 99213 | 650 | $78,286 | $60,684 | 77.5% |

## Paid-amount concentration

Share of total paid (7220 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 73 | 17.5% |
| top 5% | 361 | 65.2% |
| top 10% | 722 | 85.5% |

Gini coefficient of paid per claim: **0.873** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 228 | 70450 (12%), 97110 (12%), 85025 (11%) |
| out-of-network provider | 223 | 80053 (14%), 93000 (14%), 99285 (12%) |
| not medically necessary | 221 | 43239 (14%), 93000 (13%), 99285 (13%) |

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
| 27447 | 591 | $24,828 | $8,333,717 | 13.0% |
| 43239 | 746 | $2,051 | $862,822 | 13.8% |
| 99285 | 741 | $1,059 | $449,387 | 13.2% |
| 70450 | 710 | $649 | $268,491 | 12.0% |
| 99214 | 713 | $167 | $68,314 | 12.8% |

## Member utilization

1372 of 1935 synthetic members have 3+ claims and account for 89.8% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0297 | 10 | $4,838 |
| MBR-0844 | 10 | $2,703 |
| MBR-1120 | 10 | $2,050 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 246 | not medically necessary | 61 |
| HDHP | 237 | missing prior authorization | 63 |
| HMO | 242 | not medically necessary | 60 |
| PPO | 221 | missing prior authorization | 57 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1847 | 13.3% | 11.8% to 14.9% | no |
| HDHP | 1797 | 13.2% | 11.7% to 14.8% | no |
| HMO | 1795 | 13.5% | 12.0% to 15.1% | no |
| PPO | 1781 | 12.4% | 11.0% to 14.0% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $228 | $1,305 | $1,412 | $1,684 | $1,589 | $1,781 |
| HDHP | $332 | $1,968 | $1,638 | $1,560 | $1,981 | $2,596 |
| HMO | $263 | $1,832 | $1,688 | $1,437 | $1,334 | $1,381 |
| PPO | $262 | $1,372 | $1,720 | $1,377 | $1,621 | $1,731 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1372). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 752 | 54.8% |
| 1 denial | 442 | 32.2% |
| 2+ denials | 178 | 13.0% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1244 | 137 | 11.0% | missing prior authorization |
| 18-29 | 1104 | 137 | 12.4% | timely filing exceeded |
| 30-44 | 1200 | 165 | 13.8% | not medically necessary |
| 45-59 | 1195 | 156 | 13.1% | out-of-network provider |
| 60-74 | 1250 | 164 | 13.1% | not medically necessary |
| 75+ | 1227 | 187 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1268.1% | +1215.3% | +3.47 pp |
| 2026-09 | +255.8% | +244.8% | +1.09 pp |
| 2026-10 | +0.7% | -6.9% | +0.86 pp |

## Potential duplicate services

170 groups share a member, procedure and service date (review queue, not a quality failure).

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
