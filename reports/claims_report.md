# Healthcare Data - claims pipeline report

Generated 2026-11-25 16:49 UTC. All data is synthetic - no real member, patient or plan information.

**6440 claims** in store. Billed $16,142,331, paid $9,103,121, denied 837 overall.

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
| 2026-08 | 621 | $1,606,428 | $1,229,087 | $902,040 | 12.1% |
| 2026-09 | 2027 | $4,967,389 | $3,792,322 | $2,881,678 | 13.3% |
| 2026-10 | 2030 | $4,850,108 | $3,664,611 | $2,670,267 | 13.9% |
| 2026-11 | 1408 | $3,816,896 | $2,911,010 | $2,070,772 | 12.5% |

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
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 621 | 9.6% |
| 2026-09 | 2027 | 31.5% |
| 2026-10 (largest) | 2030 | 31.5% |
| 2026-11 | 1408 | 21.9% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1118 | $2,658 | $1,698,846 | 12.7% |
| R51 | Headache | 1168 | $2,623 | $1,629,222 | 13.5% |
| Z00.00 | General adult medical exam | 834 | $2,979 | $1,470,050 | 13.8% |
| E11.9 | Type 2 diabetes without complications | 1084 | $2,357 | $1,453,650 | 12.8% |
| M54.5 | Low back pain | 1116 | $2,194 | $1,426,699 | 12.5% |
| J06.9 | Acute upper respiratory infection | 1120 | $2,337 | $1,424,654 | 12.9% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 136 | 8.1% | $8,105 |
| J06.9 | 93000 | 133 | 15.0% | $7,663 |
| R51 | 80053 | 132 | 10.6% | $6,363 |
| R51 | 43239 | 128 | 17.2% | $141,239 |
| M54.5 | 80053 | 127 | 11.8% | $5,706 |
| M54.5 | 99285 | 124 | 16.1% | $75,905 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4962 | 77.0% | $12,105,425 | $7,917,976 |
| adjusted | 640 | 9.9% | $1,861,293 | $1,185,144 |
| denied | 838 | 13.0% | $2,175,613 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 75 | not medically necessary | 28.0% |
| 2026-09 | 270 | missing prior authorization | 27.8% |
| 2026-10 | 282 | missing prior authorization | 28.0% |
| 2026-11 | 176 | out-of-network provider | 23.9% |

## Denial reasons

- missing prior authorization (204)
- out-of-network provider (198)
- timely filing exceeded (196)
- not medically necessary (196)
- duplicate claim (44)

## Plan mix

- EPO: 1650
- HDHP: 1609
- PPO: 1591
- HMO: 1590

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1650 | 13.2% | 55.6% |
| HDHP | 1609 | 12.7% | 59.5% |
| PPO | 1591 | 12.2% | 54.2% |
| HMO | 1590 | 13.9% | 55.9% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1369 | 23.2% | 15.9% |
| PPO | 1397 | 23.9% | 15.5% |
| HDHP | 1404 | 22.1% | 15.0% |
| EPO | 1432 | 23.4% | 14.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 204 | $562,434 | 25.9% | $2,757 |
| not medically necessary | 196 | $513,208 | 23.6% | $2,618 |
| timely filing exceeded | 196 | $485,753 | 22.3% | $2,478 |
| out-of-network provider | 198 | $481,627 | 22.1% | $2,432 |
| duplicate claim | 44 | $132,591 | 6.1% | $3,013 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 148 (157 later claims)
- Later claims denied as duplicate: 44
- Later claims still paid: 103 ($213,742 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 261 | 13.7% | $290,299 | 3.2% |
| 2 claims | 411 | 21.6% | $1,125,881 | 12.4% |
| 3 claims | 418 | 22.0% | $1,687,740 | 18.5% |
| 4+ claims | 812 | 42.7% | $5,999,201 | 65.9% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1887 | 29.3% | $74,340 | 0.8% | 12.7% |
| $100-$999 | 2979 | 46.3% | $540,446 | 5.9% | 13.2% |
| $1,000-$9,999 | 1043 | 16.2% | $1,043,947 | 11.5% | 12.8% |
| $10,000+ | 531 | 8.2% | $7,444,387 | 81.8% | 13.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,440 | 6,440 | yes |
| claims: plan mix | 6,440 | 6,440 | yes |
| claims: plan performance | 6,440 | 6,440 | yes |
| claims: age bands | 6,440 | 6,440 | yes |
| claims: cost per member | 6,440 | 6,440 | yes |
| paid $: monthly view | 9,103,120.7 | 9,103,120.7 | yes |
| paid $: age bands | 9,103,112.85 | 9,103,120.7 | yes |
| denied claims: reasons | 838 | 838 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1303 |
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
| HDHP | 454 | 1609 | 3.54 | $5,909 |
| PPO | 483 | 1591 | 3.29 | $4,734 |
| EPO | 487 | 1650 | 3.39 | $4,547 |
| HMO | 478 | 1590 | 3.33 | $4,016 |

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
| 43239 | 577 | $1,185,005 | $909,480 | 76.8% |
| 27447 | 459 | $11,426,320 | $8,779,908 | 76.8% |
| 99213 | 579 | $69,557 | $53,886 | 77.5% |
| 99214 | 567 | $94,821 | $73,481 | 77.5% |
| 70450 | 563 | $367,762 | $285,147 | 77.5% |
| 93000 | 610 | $60,927 | $47,258 | 77.6% |

## Paid-amount concentration

Share of total paid (6440 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 65 | 17.2% |
| top 5% | 322 | 64.9% |
| top 10% | 644 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 204 | 70450 (13%), 85025 (12%), 99285 (11%) |
| out-of-network provider | 198 | 80053 (13%), 99285 (13%), 93000 (12%) |
| not medically necessary | 196 | 93000 (14%), 43239 (13%), 99285 (13%) |

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
| 27447 | 531 | $24,920 | $7,444,387 | 13.6% |
| 43239 | 664 | $2,044 | $767,890 | 13.1% |
| 99285 | 676 | $1,062 | $410,159 | 13.8% |
| 70450 | 643 | $649 | $241,121 | 12.4% |
| 99214 | 648 | $168 | $62,400 | 12.5% |

## Member utilization

1230 of 1902 synthetic members have 3+ claims and account for 84.4% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0844 | 10 | $2,703 |
| MBR-1467 | 10 | $1,872 |
| MBR-1497 | 9 | $16,646 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 218 | out-of-network provider | 54 |
| HDHP | 205 | missing prior authorization | 55 |
| HMO | 221 | not medically necessary | 56 |
| PPO | 194 | missing prior authorization | 51 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1650 | 13.2% | 11.7% to 14.9% | no |
| HDHP | 1609 | 12.7% | 11.2% to 14.5% | no |
| PPO | 1591 | 12.2% | 10.7% to 13.9% | no |
| HMO | 1590 | 13.9% | 12.3% to 15.7% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $227 | $1,382 | $1,374 | $1,655 | $1,623 | $1,870 |
| HDHP | $339 | $1,860 | $1,583 | $1,492 | $2,043 | $2,645 |
| HMO | $269 | $1,607 | $1,555 | $1,221 | $1,428 | $1,340 |
| PPO | $260 | $1,445 | $1,751 | $1,401 | $1,686 | $1,935 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.0%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1230). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 692 | 56.3% |
| 1 denial | 395 | 32.1% |
| 2+ denials | 143 | 11.6% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1091 | 115 | 10.5% | missing prior authorization |
| 18-29 | 992 | 126 | 12.7% | timely filing exceeded |
| 30-44 | 1095 | 153 | 14.0% | not medically necessary |
| 45-59 | 1054 | 136 | 12.9% | out-of-network provider |
| 60-74 | 1121 | 143 | 12.8% | not medically necessary |
| 75+ | 1087 | 165 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1221.3% | +1162.3% | +3.57 pp |
| 2026-09 | +226.4% | +219.5% | +1.24 pp |
| 2026-10 | +0.1% | -7.3% | +0.57 pp |

## Potential duplicate services

148 groups share a member, procedure and service date (review queue, not a quality failure).

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
