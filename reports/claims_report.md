# Healthcare Data - claims pipeline report

Generated 2026-11-28 09:58 UTC. All data is synthetic - no real member, patient or plan information.

**7280 claims** in store. Billed $18,031,576, paid $10,233,389, denied 953 overall.

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
| 2026-09 | 2309 | $5,598,721 | $4,300,347 | $3,258,706 | 13.0% |
| 2026-10 | 2320 | $5,448,165 | $4,111,881 | $3,017,482 | 14.0% |
| 2026-11 | 1654 | $4,420,971 | $3,394,181 | $2,438,915 | 13.1% |

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
| 2026-08 | 643 | 8.8% |
| 2026-09 | 2309 | 31.7% |
| 2026-10 (largest) | 2320 | 31.9% |
| 2026-11 | 1654 | 22.7% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1277 | $2,537 | $1,877,873 | 12.1% |
| R51 | Headache | 1307 | $2,529 | $1,762,779 | 13.3% |
| Z00.00 | General adult medical exam | 942 | $3,056 | $1,709,219 | 13.8% |
| J06.9 | Acute upper respiratory infection | 1272 | $2,355 | $1,667,648 | 13.3% |
| E11.9 | Type 2 diabetes without complications | 1232 | $2,310 | $1,611,816 | 13.4% |
| M54.5 | Low back pain | 1250 | $2,212 | $1,604,054 | 12.9% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 158 | 12.7% | $7,311 |
| J06.9 | 93000 | 155 | 13.6% | $9,031 |
| R51 | 93000 | 154 | 8.4% | $9,218 |
| M54.5 | 80053 | 148 | 10.8% | $6,676 |
| R51 | 43239 | 145 | 17.2% | $163,777 |
| E11.9 | 93000 | 140 | 15.7% | $7,910 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5622 | 77.2% | $13,633,893 | $8,938,077 |
| adjusted | 705 | 9.7% | $2,030,058 | $1,295,312 |
| denied | 953 | 13.1% | $2,367,625 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 300 | missing prior authorization | 26.3% |
| 2026-10 | 324 | missing prior authorization | 28.7% |
| 2026-11 | 217 | not medically necessary | 24.4% |

## Denial reasons

- missing prior authorization (229)
- out-of-network provider (224)
- not medically necessary (223)
- timely filing exceeded (218)
- duplicate claim (59)

## Plan mix

- EPO: 1862
- HMO: 1812
- HDHP: 1809
- PPO: 1797

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1862 | 13.3% | 55.5% |
| HMO | 1812 | 13.5% | 57.0% |
| HDHP | 1809 | 13.2% | 59.9% |
| PPO | 1797 | 12.3% | 54.3% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1575 | 23.5% | 16.0% |
| HMO | 1567 | 22.8% | 15.4% |
| EPO | 1615 | 23.8% | 15.2% |
| HDHP | 1570 | 21.7% | 14.7% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 7280 claims: chi2 = 1.225, df = 3, p = 0.7469. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Claims per member: dispersion

Across 1937 members with claims: mean 3.758, variance 3.49, variance-to-mean ratio 0.929. A ratio near 1 matches random assignment; well above 1 would mean claims cluster on a few members. The generator assigns members at random, so about 1 is expected. No enrollment data, so zero-claim members are invisible and this is indicative only.

## Highest billed amounts relative to procedure median

Review-queue template: claims furthest above their procedure's median billed amount (procedures under 30 claims skipped). The generator draws amounts inside fixed per-procedure ranges, so no true outliers are expected here.

| Claim | Procedure | Billed ($) | Procedure median ($) | Ratio |
| --- | --- | ---: | ---: | ---: |
| CLM-61120-B11-000031 | 80053 | 119.76 | 77.96 | 1.54x |
| CLM-61125-B09-000034 | 80053 | 119.92 | 77.96 | 1.54x |
| CLM-00007-000110 | 80053 | 119.06 | 77.96 | 1.53x |
| CLM-61120-B08-000041 | 80053 | 119.15 | 77.96 | 1.53x |
| CLM-61120-B09-000001 | 80053 | 119.59 | 77.96 | 1.53x |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1797 | 12.3% | 700,527.84 | 15.5% |
| EPO | 1862 | 13.3% | 621,767.22 | 14.1% |
| HDHP | 1809 | 13.2% | 525,304.01 | 10.4% |
| HMO | 1812 | 13.5% | 520,026.41 | 12.8% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 447 | 46.9% | 1,177,603.40 |
| network / coverage | 224 | 23.5% | 516,926.65 |
| clinical review | 223 | 23.4% | 531,950.28 |
| billing error | 59 | 6.2% | 141,145.15 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5622 | 5622 | 84.9% | 77.5% |
| adjusted | 705 | 705 | 84.5% | 77.8% |
| denied | 953 | 895 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 229 | $620,873 | 26.2% | $2,711 |
| timely filing exceeded | 218 | $556,731 | 23.5% | $2,554 |
| not medically necessary | 223 | $531,950 | 22.5% | $2,385 |
| out-of-network provider | 224 | $516,927 | 21.8% | $2,308 |
| duplicate claim | 59 | $141,145 | 6.0% | $2,392 |

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
| 1 claim | 199 | 10.3% | $253,800 | 2.5% |
| 2 claims | 358 | 18.5% | $761,063 | 7.4% |
| 3 claims | 385 | 19.9% | $1,656,308 | 16.2% |
| 4+ claims | 995 | 51.4% | $7,562,218 | 73.9% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2144 | 29.4% | $83,828 | 0.8% | 13.0% |
| $100-$999 | 3371 | 46.3% | $609,004 | 5.9% | 13.1% |
| $1,000-$9,999 | 1171 | 16.1% | $1,172,613 | 11.5% | 13.3% |
| $10,000+ | 594 | 8.2% | $8,367,944 | 81.8% | 13.1% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 7,280 | 7,280 | yes |
| claims: plan mix | 7,280 | 7,280 | yes |
| claims: plan performance | 7,280 | 7,280 | yes |
| claims: age bands | 7,280 | 7,280 | yes |
| claims: cost per member | 7,280 | 7,280 | yes |
| paid $: monthly view | 10,233,389.37 | 10,233,389.37 | yes |
| paid $: age bands | 10,233,397.12 | 10,233,389.37 | yes |
| denied claims: reasons | 953 | 953 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 2143 |
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
| HDHP | 461 | 1809 | 3.92 | $6,538 |
| PPO | 488 | 1797 | 3.68 | $5,037 |
| EPO | 495 | 1862 | 3.76 | $4,951 |
| HMO | 493 | 1812 | 3.68 | $4,687 |

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
| 27447 | 516 | $12,812,343 | $9,871,181 | 77.0% |
| 43239 | 649 | $1,337,588 | $1,032,749 | 77.2% |
| 85025 | 629 | $33,332 | $25,764 | 77.3% |
| 97110 | 598 | $71,945 | $55,650 | 77.3% |
| 99214 | 632 | $105,590 | $81,718 | 77.4% |
| 99213 | 653 | $78,579 | $60,891 | 77.5% |

## Paid-amount concentration

Share of total paid (7280 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 73 | 17.4% |
| top 5% | 364 | 65.4% |
| top 10% | 728 | 85.5% |

Gini coefficient of paid per claim: **0.873** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 229 | 70450 (12%), 97110 (12%), 85025 (11%) |
| out-of-network provider | 224 | 80053 (14%), 93000 (14%), 99285 (12%) |
| not medically necessary | 223 | 43239 (15%), 93000 (13%), 99285 (13%) |

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
| 27447 | 594 | $24,842 | $8,367,944 | 13.1% |
| 43239 | 755 | $2,050 | $871,292 | 14.0% |
| 99285 | 742 | $1,060 | $450,269 | 13.2% |
| 70450 | 718 | $650 | $272,334 | 11.8% |
| 99214 | 724 | $168 | $69,458 | 12.7% |

## Member utilization

1380 of 1937 synthetic members have 3+ claims and account for 90.1% of paid dollars.

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
| EPO | 247 | not medically necessary | 62 |
| HDHP | 239 | missing prior authorization | 64 |
| HMO | 245 | not medically necessary | 60 |
| PPO | 222 | missing prior authorization | 57 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1862 | 13.3% | 11.8% to 14.9% | no |
| HMO | 1812 | 13.5% | 12.0% to 15.2% | no |
| HDHP | 1809 | 13.2% | 11.7% to 14.8% | no |
| PPO | 1797 | 12.3% | 10.9% to 14.0% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $227 | $1,299 | $1,432 | $1,680 | $1,584 | $1,753 |
| HDHP | $330 | $1,966 | $1,614 | $1,555 | $1,973 | $2,596 |
| HMO | $263 | $1,811 | $1,676 | $1,427 | $1,324 | $1,378 |
| PPO | $262 | $1,368 | $1,687 | $1,365 | $1,684 | $1,722 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1380). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 756 | 54.8% |
| 1 denial | 444 | 32.2% |
| 2+ denials | 180 | 13.0% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1252 | 137 | 10.9% | missing prior authorization |
| 18-29 | 1111 | 138 | 12.4% | timely filing exceeded |
| 30-44 | 1219 | 168 | 13.8% | not medically necessary |
| 45-59 | 1202 | 158 | 13.1% | out-of-network provider |
| 60-74 | 1261 | 165 | 13.1% | not medically necessary |
| 75+ | 1235 | 187 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1268.1% | +1215.3% | +3.47 pp |
| 2026-09 | +259.1% | +246.7% | +1.01 pp |
| 2026-10 | +0.5% | -7.4% | +0.98 pp |

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
