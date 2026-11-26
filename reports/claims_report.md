# Healthcare Data - claims pipeline report

Generated 2026-11-26 17:53 UTC. All data is synthetic - no real member, patient or plan information.

**6800 claims** in store. Billed $16,900,604, paid $9,542,162, denied 890 overall.

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
| 2026-08 | 635 | $1,659,957 | $1,272,925 | $938,212 | 12.1% |
| 2026-09 | 2135 | $5,176,514 | $3,961,246 | $2,995,333 | 13.4% |
| 2026-10 | 2166 | $5,086,797 | $3,840,649 | $2,816,769 | 13.8% |
| 2026-11 | 1510 | $4,075,826 | $3,110,510 | $2,213,485 | 12.8% |

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
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 635 | 9.3% |
| 2026-09 | 2135 | 31.4% |
| 2026-10 (largest) | 2166 | 31.9% |
| 2026-11 | 1510 | 22.2% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1187 | $2,592 | $1,766,630 | 12.5% |
| R51 | Headache | 1226 | $2,605 | $1,714,733 | 13.3% |
| Z00.00 | General adult medical exam | 885 | $3,041 | $1,590,741 | 13.8% |
| E11.9 | Type 2 diabetes without complications | 1144 | $2,375 | $1,553,754 | 13.1% |
| M54.5 | Low back pain | 1179 | $2,175 | $1,477,902 | 13.1% |
| J06.9 | Acute upper respiratory infection | 1179 | $2,255 | $1,438,403 | 13.1% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 145 | 11.7% | $6,905 |
| R51 | 93000 | 145 | 8.3% | $8,657 |
| J06.9 | 93000 | 144 | 13.9% | $8,414 |
| M54.5 | 80053 | 137 | 11.7% | $6,167 |
| R51 | 43239 | 136 | 16.2% | $154,495 |
| E11.9 | 93000 | 130 | 16.2% | $7,205 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5238 | 77.0% | $12,638,096 | $8,257,368 |
| adjusted | 671 | 9.9% | $2,014,150 | $1,284,794 |
| denied | 891 | 13.1% | $2,248,358 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 287 | missing prior authorization | 26.8% |
| 2026-10 | 299 | missing prior authorization | 28.1% |
| 2026-11 | 193 | timely filing exceeded | 24.9% |

## Denial reasons

- missing prior authorization (214)
- out-of-network provider (214)
- timely filing exceeded (208)
- not medically necessary (207)
- duplicate claim (48)

## Plan mix

- EPO: 1744
- HMO: 1695
- HDHP: 1682
- PPO: 1679

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1744 | 13.1% | 55.5% |
| HMO | 1695 | 13.7% | 56.7% |
| HDHP | 1682 | 13.1% | 59.4% |
| PPO | 1679 | 12.6% | 54.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1468 | 23.7% | 15.7% |
| HMO | 1463 | 23.2% | 15.6% |
| EPO | 1516 | 23.6% | 15.1% |
| HDHP | 1462 | 22.0% | 15.0% |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1679 | 12.6% | 695,270.81 | 16.0% |
| EPO | 1744 | 13.1% | 605,299.32 | 14.4% |
| HDHP | 1682 | 13.1% | 480,857.25 | 10.4% |
| HMO | 1695 | 13.7% | 466,930.91 | 12.5% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 422 | 47.4% | 1,088,699.51 |
| network / coverage | 214 | 24.0% | 508,912.56 |
| clinical review | 207 | 23.2% | 517,554.09 |
| billing error | 48 | 5.4% | 133,192.13 |

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5238 | 5238 | 84.9% | 77.5% |
| adjusted | 671 | 671 | 84.5% | 77.8% |
| denied | 891 | 844 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 214 | $582,494 | 25.9% | $2,722 |
| not medically necessary | 207 | $517,554 | 23.0% | $2,500 |
| out-of-network provider | 214 | $508,913 | 22.6% | $2,378 |
| timely filing exceeded | 208 | $506,206 | 22.5% | $2,434 |
| duplicate claim | 48 | $133,192 | 5.9% | $2,775 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 156 (165 later claims)
- Later claims denied as duplicate: 48
- Later claims still paid: 107 ($214,506 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 238 | 12.4% | $280,863 | 2.9% |
| 2 claims | 385 | 20.0% | $1,003,593 | 10.5% |
| 3 claims | 414 | 21.5% | $1,711,859 | 17.9% |
| 4+ claims | 887 | 46.1% | $6,545,848 | 68.6% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2002 | 29.4% | $78,333 | 0.8% | 13.1% |
| $100-$999 | 3153 | 46.4% | $569,173 | 6.0% | 13.2% |
| $1,000-$9,999 | 1089 | 16.0% | $1,099,630 | 11.5% | 12.6% |
| $10,000+ | 556 | 8.2% | $7,795,026 | 81.7% | 13.5% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,800 | 6,800 | yes |
| claims: plan mix | 6,800 | 6,800 | yes |
| claims: plan performance | 6,800 | 6,800 | yes |
| claims: age bands | 6,800 | 6,800 | yes |
| claims: cost per member | 6,800 | 6,800 | yes |
| paid $: monthly view | 9,542,162.41 | 9,542,162.41 | yes |
| paid $: age bands | 9,542,167.72 | 9,542,162.41 | yes |
| denied claims: reasons | 891 | 891 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1663 |
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
| HDHP | 457 | 1682 | 3.68 | $6,024 |
| PPO | 487 | 1679 | 3.45 | $4,810 |
| EPO | 493 | 1744 | 3.54 | $4,720 |
| HMO | 487 | 1695 | 3.48 | $4,352 |

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
| 27447 | 481 | $11,980,064 | $9,202,636 | 76.8% |
| 43239 | 611 | $1,256,747 | $969,653 | 77.2% |
| 85025 | 587 | $31,120 | $24,088 | 77.4% |
| 99213 | 614 | $73,965 | $57,303 | 77.5% |
| 99214 | 587 | $98,153 | $76,105 | 77.5% |
| 97110 | 554 | $66,459 | $51,538 | 77.5% |

## Paid-amount concentration

Share of total paid (6800 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 68 | 17.1% |
| top 5% | 340 | 65.2% |
| top 10% | 680 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 214 | 70450 (13%), 85025 (12%), 97110 (11%) |
| out-of-network provider | 214 | 93000 (14%), 80053 (14%), 99285 (12%) |
| timely filing exceeded | 208 | 93000 (13%), 99213 (12%), 85025 (11%) |

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
| 27447 | 556 | $24,903 | $7,795,026 | 13.5% |
| 43239 | 701 | $2,047 | $817,732 | 12.8% |
| 99285 | 697 | $1,060 | $422,078 | 13.5% |
| 70450 | 675 | $649 | $253,882 | 12.3% |
| 99214 | 673 | $168 | $64,586 | 12.8% |

## Member utilization

1301 of 1924 synthetic members have 3+ claims and account for 86.5% of paid dollars.

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
| HDHP | 220 | missing prior authorization | 58 |
| HMO | 232 | not medically necessary | 60 |
| PPO | 211 | missing prior authorization | 55 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1744 | 13.1% | 11.6% to 14.7% | no |
| HMO | 1695 | 13.7% | 12.1% to 15.4% | no |
| HDHP | 1682 | 13.1% | 11.6% to 14.8% | no |
| PPO | 1679 | 12.6% | 11.1% to 14.2% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $233 | $1,326 | $1,450 | $1,619 | $1,577 | $1,885 |
| HDHP | $338 | $1,796 | $1,506 | $1,519 | $2,038 | $2,639 |
| HMO | $268 | $1,716 | $1,641 | $1,319 | $1,348 | $1,389 |
| PPO | $261 | $1,424 | $1,715 | $1,388 | $1,639 | $1,830 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1301). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 723 | 55.6% |
| 1 denial | 417 | 32.0% |
| 2+ denials | 161 | 12.4% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1163 | 124 | 10.7% | missing prior authorization |
| 18-29 | 1042 | 134 | 12.9% | timely filing exceeded |
| 30-44 | 1150 | 161 | 14.0% | not medically necessary |
| 45-59 | 1121 | 143 | 12.8% | out-of-network provider |
| 60-74 | 1178 | 156 | 13.2% | not medically necessary |
| 75+ | 1146 | 173 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1251.1% | +1212.9% | +3.62 pp |
| 2026-09 | +236.2% | +219.3% | +1.31 pp |
| 2026-10 | +1.5% | -6.0% | +0.36 pp |

## Potential duplicate services

156 groups share a member, procedure and service date (review queue, not a quality failure).

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
