# Healthcare Data - claims pipeline report

Generated 2026-11-27 23:57 UTC. All data is synthetic - no real member, patient or plan information.

**7160 claims** in store. Billed $17,799,307, paid $10,106,885, denied 937 overall.

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
| 2026-08 | 642 | $1,662,139 | $1,274,756 | $939,874 | 12.0% |
| 2026-09 | 2264 | $5,516,539 | $4,233,291 | $3,206,741 | 13.1% |
| 2026-10 | 2288 | $5,387,949 | $4,070,030 | $3,001,745 | 13.9% |
| 2026-11 | 1612 | $4,331,170 | $3,318,897 | $2,380,162 | 13.0% |

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
| 2026-08 | 642 | 9.0% |
| 2026-09 | 2264 | 31.6% |
| 2026-10 (largest) | 2288 | 32.0% |
| 2026-11 | 1612 | 22.5% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1259 | $2,565 | $1,870,965 | 12.2% |
| R51 | Headache | 1286 | $2,565 | $1,758,299 | 13.3% |
| Z00.00 | General adult medical exam | 932 | $3,016 | $1,686,183 | 13.7% |
| J06.9 | Acute upper respiratory infection | 1252 | $2,333 | $1,614,683 | 13.3% |
| E11.9 | Type 2 diabetes without complications | 1207 | $2,348 | $1,603,358 | 13.4% |
| M54.5 | Low back pain | 1224 | $2,211 | $1,573,397 | 12.8% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 152 | 12.5% | $7,124 |
| J06.9 | 93000 | 151 | 13.2% | $8,821 |
| R51 | 93000 | 151 | 8.0% | $9,076 |
| M54.5 | 80053 | 143 | 11.2% | $6,479 |
| R51 | 43239 | 143 | 17.5% | $161,011 |
| E11.9 | 93000 | 137 | 16.1% | $7,718 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5525 | 77.2% | $13,441,747 | $8,812,431 |
| adjusted | 698 | 9.8% | $2,028,819 | $1,294,454 |
| denied | 937 | 13.1% | $2,328,740 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 297 | missing prior authorization | 26.6% |
| 2026-10 | 319 | missing prior authorization | 28.8% |
| 2026-11 | 209 | out-of-network provider | 24.4% |

## Denial reasons

- missing prior authorization (227)
- out-of-network provider (222)
- not medically necessary (219)
- timely filing exceeded (214)
- duplicate claim (55)

## Plan mix

- EPO: 1834
- HDHP: 1782
- HMO: 1778
- PPO: 1766

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1834 | 13.2% | 55.3% |
| HDHP | 1782 | 13.2% | 60.3% |
| HMO | 1778 | 13.5% | 56.9% |
| PPO | 1766 | 12.4% | 54.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1547 | 23.6% | 15.8% |
| HMO | 1538 | 22.8% | 15.4% |
| EPO | 1591 | 23.9% | 15.2% |
| HDHP | 1547 | 21.6% | 14.6% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 7160 claims: chi2 = 1.054, df = 3, p = 0.7882. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Claims per member: dispersion

Across 1932 members with claims: mean 3.706, variance 3.455, variance-to-mean ratio 0.932. A ratio near 1 matches random assignment; well above 1 would mean claims cluster on a few members. The generator assigns members at random, so about 1 is expected. No enrollment data, so zero-claim members are invisible and this is indicative only.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1766 | 12.4% | 700,326.80 | 15.7% |
| EPO | 1834 | 13.2% | 619,739.01 | 14.2% |
| HMO | 1778 | 13.5% | 517,426.87 | 12.8% |
| HDHP | 1782 | 13.2% | 491,247.42 | 9.9% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 441 | 47.1% | 1,145,142.25 |
| network / coverage | 222 | 23.7% | 514,690.92 |
| clinical review | 219 | 23.4% | 528,175.85 |
| billing error | 55 | 5.9% | 140,731.08 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5525 | 5525 | 84.9% | 77.5% |
| adjusted | 698 | 698 | 84.5% | 77.8% |
| denied | 937 | 883 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 227 | $588,851 | 25.3% | $2,594 |
| timely filing exceeded | 214 | $556,291 | 23.9% | $2,599 |
| not medically necessary | 219 | $528,176 | 22.7% | $2,412 |
| out-of-network provider | 222 | $514,691 | 22.1% | $2,318 |
| duplicate claim | 55 | $140,731 | 6.0% | $2,559 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 166 (175 later claims)
- Later claims denied as duplicate: 55
- Later claims still paid: 110 ($215,205 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 213 | 11.0% | $274,524 | 2.7% |
| 2 claims | 358 | 18.5% | $755,175 | 7.5% |
| 3 claims | 394 | 20.4% | $1,666,823 | 16.5% |
| 4+ claims | 967 | 50.0% | $7,410,362 | 73.3% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2102 | 29.4% | $82,377 | 0.8% | 12.9% |
| $100-$999 | 3318 | 46.3% | $600,001 | 5.9% | 13.1% |
| $1,000-$9,999 | 1153 | 16.1% | $1,153,806 | 11.4% | 13.3% |
| $10,000+ | 587 | 8.2% | $8,270,701 | 81.8% | 13.1% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 7,160 | 7,160 | yes |
| claims: plan mix | 7,160 | 7,160 | yes |
| claims: plan performance | 7,160 | 7,160 | yes |
| claims: age bands | 7,160 | 7,160 | yes |
| claims: cost per member | 7,160 | 7,160 | yes |
| paid $: monthly view | 10,106,884.64 | 10,106,884.64 | yes |
| paid $: age bands | 10,106,876.88 | 10,106,884.64 | yes |
| denied claims: reasons | 937 | 937 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 2023 |
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
| HDHP | 459 | 1782 | 3.88 | $6,499 |
| PPO | 488 | 1766 | 3.62 | $4,949 |
| EPO | 495 | 1834 | 3.71 | $4,868 |
| HMO | 490 | 1778 | 3.63 | $4,692 |

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
| 27447 | 510 | $12,662,912 | $9,749,742 | 77.0% |
| 43239 | 639 | $1,315,493 | $1,015,616 | 77.2% |
| 85025 | 616 | $32,678 | $25,236 | 77.2% |
| 97110 | 590 | $70,863 | $54,807 | 77.3% |
| 99214 | 618 | $103,207 | $79,894 | 77.4% |
| 99213 | 642 | $77,303 | $59,906 | 77.5% |

## Paid-amount concentration

Share of total paid (7160 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 72 | 17.4% |
| top 5% | 358 | 65.2% |
| top 10% | 716 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 227 | 97110 (12%), 70450 (12%), 85025 (11%) |
| out-of-network provider | 222 | 80053 (14%), 93000 (14%), 99285 (12%) |
| not medically necessary | 219 | 43239 (14%), 93000 (13%), 99285 (13%) |

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
| 27447 | 587 | $24,830 | $8,270,701 | 13.1% |
| 43239 | 742 | $2,048 | $856,614 | 13.9% |
| 99285 | 736 | $1,059 | $445,603 | 13.3% |
| 70450 | 706 | $650 | $267,313 | 11.9% |
| 99214 | 709 | $167 | $67,876 | 12.8% |

## Member utilization

1361 of 1932 synthetic members have 3+ claims and account for 89.8% of paid dollars.

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
| EPO | 243 | not medically necessary | 60 |
| HDHP | 235 | missing prior authorization | 62 |
| HMO | 240 | not medically necessary | 60 |
| PPO | 219 | missing prior authorization | 57 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1834 | 13.2% | 11.8% to 14.9% | no |
| HDHP | 1782 | 13.2% | 11.7% to 14.8% | no |
| HMO | 1778 | 13.5% | 12.0% to 15.2% | no |
| PPO | 1766 | 12.4% | 10.9% to 14.0% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $230 | $1,319 | $1,416 | $1,605 | $1,596 | $1,799 |
| HDHP | $329 | $1,996 | $1,638 | $1,523 | $1,976 | $2,596 |
| HMO | $268 | $1,839 | $1,693 | $1,451 | $1,343 | $1,387 |
| PPO | $258 | $1,376 | $1,732 | $1,375 | $1,590 | $1,755 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1361). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 747 | 54.9% |
| 1 denial | 438 | 32.2% |
| 2+ denials | 176 | 12.9% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1227 | 133 | 10.8% | missing prior authorization |
| 18-29 | 1095 | 137 | 12.5% | timely filing exceeded |
| 30-44 | 1195 | 165 | 13.8% | not medically necessary |
| 45-59 | 1187 | 156 | 13.1% | out-of-network provider |
| 60-74 | 1239 | 162 | 13.1% | not medically necessary |
| 75+ | 1217 | 184 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1266.0% | +1215.2% | +3.48 pp |
| 2026-09 | +252.7% | +241.2% | +1.13 pp |
| 2026-10 | +1.1% | -6.4% | +0.82 pp |

## Potential duplicate services

166 groups share a member, procedure and service date (review queue, not a quality failure).

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
