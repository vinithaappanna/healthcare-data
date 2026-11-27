# Healthcare Data - claims pipeline report

Generated 2026-11-27 18:56 UTC. All data is synthetic - no real member, patient or plan information.

**7100 claims** in store. Billed $17,719,888, paid $10,066,845, denied 929 overall.

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
| 2026-08 | 640 | $1,661,870 | $1,274,561 | $939,698 | 12.0% |
| 2026-09 | 2248 | $5,511,390 | $4,229,385 | $3,203,506 | 13.2% |
| 2026-10 | 2268 | $5,352,045 | $4,047,573 | $2,985,114 | 13.9% |
| 2026-11 | 1590 | $4,293,074 | $3,289,074 | $2,360,164 | 13.0% |

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
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 640 | 9.0% |
| 2026-09 | 2248 | 31.7% |
| 2026-10 (largest) | 2268 | 31.9% |
| 2026-11 | 1590 | 22.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1247 | $2,589 | $1,870,139 | 12.2% |
| R51 | Headache | 1276 | $2,581 | $1,755,222 | 13.4% |
| Z00.00 | General adult medical exam | 925 | $3,035 | $1,684,860 | 13.6% |
| E11.9 | Type 2 diabetes without complications | 1197 | $2,361 | $1,601,161 | 13.3% |
| J06.9 | Acute upper respiratory infection | 1237 | $2,313 | $1,582,645 | 13.4% |
| M54.5 | Low back pain | 1218 | $2,219 | $1,572,818 | 12.7% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 151 | 12.6% | $7,088 |
| J06.9 | 93000 | 150 | 13.3% | $8,774 |
| R51 | 93000 | 149 | 8.1% | $8,934 |
| R51 | 43239 | 142 | 17.6% | $159,373 |
| M54.5 | 80053 | 141 | 11.3% | $6,356 |
| E11.9 | 80053 | 136 | 14.7% | $6,105 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5480 | 77.2% | $13,372,811 | $8,774,598 |
| adjusted | 691 | 9.7% | $2,025,354 | $1,292,247 |
| denied | 929 | 13.1% | $2,321,724 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 296 | missing prior authorization | 26.4% |
| 2026-10 | 315 | missing prior authorization | 28.6% |
| 2026-11 | 206 | out-of-network provider | 24.8% |

## Denial reasons

- missing prior authorization (222)
- out-of-network provider (222)
- not medically necessary (217)
- timely filing exceeded (214)
- duplicate claim (54)

## Plan mix

- EPO: 1822
- HDHP: 1764
- HMO: 1763
- PPO: 1751

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1822 | 13.2% | 55.4% |
| HDHP | 1764 | 13.1% | 60.3% |
| HMO | 1763 | 13.6% | 57.0% |
| PPO | 1751 | 12.4% | 54.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1533 | 23.7% | 15.7% |
| HMO | 1524 | 22.7% | 15.3% |
| EPO | 1581 | 23.9% | 15.2% |
| HDHP | 1533 | 21.6% | 14.6% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 7100 claims: chi2 = 0.998, df = 3, p = 0.8018. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Claims per member: dispersion

Across 1932 members with claims: mean 3.675, variance 3.445, variance-to-mean ratio 0.937. A ratio near 1 matches random assignment; well above 1 would mean claims cluster on a few members. The generator assigns members at random, so about 1 is expected. No enrollment data, so zero-claim members are invisible and this is indicative only.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1751 | 12.4% | 700,152.04 | 15.8% |
| EPO | 1822 | 13.2% | 617,805.78 | 14.2% |
| HMO | 1763 | 13.6% | 515,434.32 | 12.9% |
| HDHP | 1764 | 13.1% | 488,331.43 | 9.9% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 436 | 46.9% | 1,139,843.05 |
| network / coverage | 222 | 23.9% | 514,690.92 |
| clinical review | 217 | 23.4% | 526,630.17 |
| billing error | 54 | 5.8% | 140,559.43 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5480 | 5480 | 84.9% | 77.5% |
| adjusted | 691 | 691 | 84.5% | 77.8% |
| denied | 929 | 876 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 222 | $583,552 | 25.1% | $2,629 |
| timely filing exceeded | 214 | $556,291 | 24.0% | $2,599 |
| not medically necessary | 217 | $526,630 | 22.7% | $2,427 |
| out-of-network provider | 222 | $514,691 | 22.2% | $2,318 |
| duplicate claim | 54 | $140,559 | 6.0% | $2,603 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 164 (173 later claims)
- Later claims denied as duplicate: 54
- Later claims still paid: 109 ($215,137 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 222 | 11.5% | $275,685 | 2.7% |
| 2 claims | 358 | 18.5% | $771,861 | 7.7% |
| 3 claims | 400 | 20.7% | $1,798,692 | 17.9% |
| 4+ claims | 952 | 49.3% | $7,220,607 | 71.7% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2086 | 29.4% | $81,637 | 0.8% | 13.0% |
| $100-$999 | 3286 | 46.3% | $595,245 | 5.9% | 13.2% |
| $1,000-$9,999 | 1143 | 16.1% | $1,148,707 | 11.4% | 13.0% |
| $10,000+ | 585 | 8.2% | $8,241,255 | 81.9% | 13.2% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 7,100 | 7,100 | yes |
| claims: plan mix | 7,100 | 7,100 | yes |
| claims: plan performance | 7,100 | 7,100 | yes |
| claims: age bands | 7,100 | 7,100 | yes |
| claims: cost per member | 7,100 | 7,100 | yes |
| paid $: monthly view | 10,066,844.66 | 10,066,844.66 | yes |
| paid $: age bands | 10,066,844.91 | 10,066,844.66 | yes |
| denied claims: reasons | 929 | 929 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1963 |
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
| HDHP | 459 | 1764 | 3.84 | $6,490 |
| PPO | 488 | 1751 | 3.59 | $4,912 |
| EPO | 495 | 1822 | 3.68 | $4,864 |
| HMO | 490 | 1763 | 3.60 | $4,660 |

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
| 27447 | 508 | $12,607,448 | $9,710,764 | 77.0% |
| 43239 | 638 | $1,313,106 | $1,013,908 | 77.2% |
| 85025 | 613 | $32,506 | $25,116 | 77.3% |
| 97110 | 579 | $69,519 | $53,786 | 77.4% |
| 99214 | 610 | $101,884 | $78,896 | 77.4% |
| 93000 | 675 | $67,580 | $52,407 | 77.5% |

## Paid-amount concentration

Share of total paid (7100 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 71 | 17.2% |
| top 5% | 355 | 65.0% |
| top 10% | 710 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 222 | 70450 (12%), 85025 (12%), 97110 (12%) |
| out-of-network provider | 222 | 80053 (14%), 93000 (14%), 99285 (12%) |
| not medically necessary | 217 | 43239 (14%), 93000 (13%), 99285 (13%) |

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
| 27447 | 585 | $24,820 | $8,241,255 | 13.2% |
| 43239 | 738 | $2,049 | $854,976 | 13.6% |
| 99285 | 729 | $1,058 | $441,413 | 13.3% |
| 70450 | 701 | $650 | $265,395 | 12.0% |
| 99214 | 700 | $167 | $67,006 | 12.9% |

## Member utilization

1352 of 1932 synthetic members have 3+ claims and account for 89.6% of paid dollars.

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
| EPO | 241 | not medically necessary | 60 |
| HDHP | 231 | missing prior authorization | 61 |
| HMO | 239 | not medically necessary | 60 |
| PPO | 218 | missing prior authorization | 56 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1822 | 13.2% | 11.8% to 14.9% | no |
| HDHP | 1764 | 13.1% | 11.6% to 14.8% | no |
| HMO | 1763 | 13.6% | 12.0% to 15.2% | no |
| PPO | 1751 | 12.4% | 11.0% to 14.1% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $231 | $1,323 | $1,416 | $1,615 | $1,616 | $1,805 |
| HDHP | $332 | $2,004 | $1,647 | $1,542 | $1,992 | $2,631 |
| HMO | $270 | $1,817 | $1,707 | $1,457 | $1,351 | $1,391 |
| PPO | $259 | $1,389 | $1,742 | $1,342 | $1,600 | $1,764 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1352). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 745 | 55.1% |
| 1 denial | 434 | 32.1% |
| 2+ denials | 173 | 12.8% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1216 | 131 | 10.8% | out-of-network provider |
| 18-29 | 1084 | 136 | 12.6% | timely filing exceeded |
| 30-44 | 1188 | 164 | 13.8% | not medically necessary |
| 45-59 | 1176 | 153 | 13.0% | out-of-network provider |
| 60-74 | 1227 | 161 | 13.1% | not medically necessary |
| 75+ | 1209 | 184 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1261.7% | +1215.0% | +3.52 pp |
| 2026-09 | +251.3% | +240.9% | +1.14 pp |
| 2026-10 | +0.9% | -6.8% | +0.72 pp |

## Potential duplicate services

164 groups share a member, procedure and service date (review queue, not a quality failure).

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
