# Healthcare Data - claims pipeline report

Generated 2026-11-25 21:51 UTC. All data is synthetic - no real member, patient or plan information.

**6560 claims** in store. Billed $16,311,064, paid $9,177,543, denied 857 overall.

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
| 2026-08 | 626 | $1,608,603 | $1,230,942 | $903,807 | 12.1% |
| 2026-09 | 2055 | $4,998,532 | $3,818,572 | $2,890,020 | 13.3% |
| 2026-10 | 2078 | $4,890,233 | $3,694,465 | $2,692,458 | 13.9% |
| 2026-11 | 1447 | $3,912,186 | $2,988,019 | $2,112,894 | 12.7% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.7% |
| 2026-01 | 31 | 0.5% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.7% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.7% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 626 | 9.5% |
| 2026-09 | 2055 | 31.3% |
| 2026-10 (largest) | 2078 | 31.7% |
| 2026-11 | 1447 | 22.1% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1140 | $2,616 | $1,706,603 | 12.5% |
| R51 | Headache | 1185 | $2,592 | $1,633,978 | 13.4% |
| Z00.00 | General adult medical exam | 855 | $2,958 | $1,492,013 | 13.8% |
| E11.9 | Type 2 diabetes without complications | 1105 | $2,331 | $1,464,444 | 12.9% |
| M54.5 | Low back pain | 1136 | $2,222 | $1,450,838 | 12.8% |
| J06.9 | Acute upper respiratory infection | 1139 | $2,307 | $1,429,666 | 13.0% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 137 | 8.0% | $8,182 |
| J06.9 | 93000 | 136 | 14.7% | $7,855 |
| R51 | 80053 | 136 | 11.0% | $6,535 |
| R51 | 43239 | 131 | 16.8% | $144,803 |
| M54.5 | 80053 | 129 | 11.6% | $5,795 |
| M54.5 | 99285 | 126 | 15.9% | $77,559 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5054 | 77.0% | $12,223,704 | $7,991,397 |
| adjusted | 649 | 9.9% | $1,862,897 | $1,186,145 |
| denied | 857 | 13.1% | $2,224,463 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 76 | not medically necessary | 27.6% |
| 2026-09 | 274 | missing prior authorization | 27.4% |
| 2026-10 | 289 | missing prior authorization | 27.7% |
| 2026-11 | 183 | out-of-network provider | 24.6% |

## Denial reasons

- missing prior authorization (206)
- out-of-network provider (204)
- not medically necessary (201)
- timely filing exceeded (200)
- duplicate claim (46)

## Plan mix

- EPO: 1673
- HDHP: 1638
- HMO: 1628
- PPO: 1621

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1673 | 13.2% | 55.7% |
| HDHP | 1638 | 13.0% | 59.2% |
| HMO | 1628 | 13.9% | 56.0% |
| PPO | 1621 | 12.2% | 53.9% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1402 | 23.2% | 16.0% |
| PPO | 1424 | 23.8% | 15.5% |
| HDHP | 1425 | 22.1% | 15.0% |
| EPO | 1452 | 23.4% | 14.8% |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1621 | 12.2% | 693,281.33 | 16.3% |
| EPO | 1673 | 13.2% | 586,153.47 | 14.7% |
| HDHP | 1638 | 13.0% | 480,250.31 | 10.6% |
| HMO | 1628 | 13.9% | 464,777.55 | 13.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 206 | $564,456 | 25.4% | $2,740 |
| not medically necessary | 201 | $514,080 | 23.1% | $2,558 |
| out-of-network provider | 204 | $507,941 | 22.8% | $2,490 |
| timely filing exceeded | 200 | $505,101 | 22.7% | $2,526 |
| duplicate claim | 46 | $132,884 | 6.0% | $2,889 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 152 (161 later claims)
- Later claims denied as duplicate: 46
- Later claims still paid: 105 ($214,305 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 254 | 13.3% | $284,909 | 3.1% |
| 2 claims | 401 | 21.0% | $1,114,275 | 12.1% |
| 3 claims | 419 | 21.9% | $1,655,392 | 18.0% |
| 4+ claims | 836 | 43.8% | $6,122,967 | 66.7% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1928 | 29.4% | $75,690 | 0.8% | 12.9% |
| $100-$999 | 3033 | 46.2% | $548,984 | 6.0% | 13.2% |
| $1,000-$9,999 | 1063 | 16.2% | $1,068,603 | 11.6% | 12.7% |
| $10,000+ | 536 | 8.2% | $7,484,265 | 81.5% | 13.8% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,560 | 6,560 | yes |
| claims: plan mix | 6,560 | 6,560 | yes |
| claims: plan performance | 6,560 | 6,560 | yes |
| claims: age bands | 6,560 | 6,560 | yes |
| claims: cost per member | 6,560 | 6,560 | yes |
| paid $: monthly view | 9,177,542.53 | 9,177,542.53 | yes |
| paid $: age bands | 9,177,547.78 | 9,177,542.53 | yes |
| denied claims: reasons | 857 | 857 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1423 |
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
| HDHP | 455 | 1638 | 3.60 | $5,904 |
| PPO | 484 | 1621 | 3.35 | $4,745 |
| EPO | 490 | 1673 | 3.41 | $4,538 |
| HMO | 481 | 1628 | 3.38 | $4,097 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0825 | 4 | 3 | 75.0% |
| MBR-1282 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 462 | $11,495,656 | $8,830,256 | 76.8% |
| 43239 | 593 | $1,218,167 | $937,480 | 77.0% |
| 85025 | 565 | $30,060 | $23,286 | 77.5% |
| 97110 | 531 | $63,614 | $49,281 | 77.5% |
| 99213 | 590 | $70,992 | $55,022 | 77.5% |
| 99214 | 574 | $95,921 | $74,369 | 77.5% |

## Paid-amount concentration

Share of total paid (6560 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 66 | 17.2% |
| top 5% | 328 | 65.3% |
| top 10% | 656 | 85.4% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 206 | 70450 (13%), 85025 (12%), 99285 (11%) |
| out-of-network provider | 204 | 80053 (13%), 93000 (13%), 99285 (12%) |
| not medically necessary | 201 | 93000 (14%), 43239 (13%), 99285 (12%) |

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
| 27447 | 536 | $24,897 | $7,484,265 | 13.8% |
| 43239 | 682 | $2,045 | $790,891 | 13.1% |
| 99285 | 679 | $1,062 | $412,265 | 13.7% |
| 70450 | 654 | $649 | $245,834 | 12.4% |
| 99214 | 656 | $168 | $63,152 | 12.5% |

## Member utilization

1255 of 1910 synthetic members have 3+ claims and account for 84.8% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0844 | 10 | $2,703 |
| MBR-1467 | 10 | $1,872 |
| MBR-0187 | 9 | $38,393 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 221 | out-of-network provider | 55 |
| HDHP | 213 | missing prior authorization | 56 |
| HMO | 226 | not medically necessary | 58 |
| PPO | 197 | missing prior authorization | 51 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1673 | 13.2% | 11.7% to 14.9% | no |
| HDHP | 1638 | 13.0% | 11.5% to 14.7% | no |
| HMO | 1628 | 13.9% | 12.3% to 15.7% | no |
| PPO | 1621 | 12.2% | 10.7% to 13.8% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $229 | $1,364 | $1,365 | $1,632 | $1,612 | $1,853 |
| HDHP | $334 | $1,827 | $1,527 | $1,483 | $2,033 | $2,625 |
| HMO | $271 | $1,600 | $1,579 | $1,225 | $1,393 | $1,361 |
| PPO | $264 | $1,418 | $1,739 | $1,373 | $1,669 | $1,892 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1255). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 698 | 55.6% |
| 1 denial | 406 | 32.4% |
| 2+ denials | 151 | 12.0% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1112 | 118 | 10.6% | missing prior authorization |
| 18-29 | 1008 | 131 | 13.0% | timely filing exceeded |
| 30-44 | 1119 | 156 | 13.9% | not medically necessary |
| 45-59 | 1078 | 139 | 12.9% | out-of-network provider |
| 60-74 | 1137 | 147 | 12.9% | not medically necessary |
| 75+ | 1106 | 166 | 15.0% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1231.9% | +1164.8% | +3.63 pp |
| 2026-09 | +228.3% | +219.8% | +1.19 pp |
| 2026-10 | +1.1% | -6.8% | +0.58 pp |

## Potential duplicate services

152 groups share a member, procedure and service date (review queue, not a quality failure).

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
