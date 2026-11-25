# Healthcare Data - claims pipeline report

Generated 2026-11-25 11:49 UTC. All data is synthetic - no real member, patient or plan information.

**6320 claims** in store. Billed $15,814,071, paid $8,911,302, denied 824 overall.

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
| 2026-08 | 612 | $1,576,065 | $1,206,670 | $885,668 | 12.2% |
| 2026-09 | 1989 | $4,882,365 | $3,726,176 | $2,823,909 | 13.4% |
| 2026-10 | 1991 | $4,732,849 | $3,573,579 | $2,592,888 | 14.0% |
| 2026-11 | 1374 | $3,721,282 | $2,838,936 | $2,030,473 | 12.4% |

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
| 2026-08 | 612 | 9.7% |
| 2026-09 | 1989 | 31.5% |
| 2026-10 (largest) | 1991 | 31.5% |
| 2026-11 | 1374 | 21.7% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1107 | $2,680 | $1,695,361 | 12.7% |
| R51 | Headache | 1135 | $2,571 | $1,556,498 | 13.7% |
| Z00.00 | General adult medical exam | 817 | $3,027 | $1,462,588 | 13.8% |
| J06.9 | Acute upper respiratory infection | 1105 | $2,367 | $1,423,294 | 12.8% |
| M54.5 | Low back pain | 1089 | $2,215 | $1,401,583 | 12.6% |
| E11.9 | Type 2 diabetes without complications | 1067 | $2,276 | $1,371,976 | 12.8% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 134 | 8.2% | $7,970 |
| J06.9 | 93000 | 130 | 15.4% | $7,486 |
| R51 | 80053 | 127 | 11.0% | $6,082 |
| M54.5 | 99285 | 124 | 16.1% | $75,905 |
| M54.5 | 80053 | 122 | 11.5% | $5,547 |
| M54.5 | 93000 | 122 | 13.1% | $7,083 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4867 | 77.0% | $11,841,748 | $7,743,115 |
| adjusted | 628 | 9.9% | $1,829,876 | $1,168,187 |
| denied | 825 | 13.1% | $2,142,446 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 75 | not medically necessary | 28.0% |
| 2026-09 | 266 | missing prior authorization | 28.2% |
| 2026-10 | 278 | missing prior authorization | 27.7% |
| 2026-11 | 171 | timely filing exceeded | 24.6% |

## Denial reasons

- missing prior authorization (201)
- out-of-network provider (195)
- not medically necessary (195)
- timely filing exceeded (193)
- duplicate claim (41)

## Plan mix

- EPO: 1613
- HMO: 1572
- HDHP: 1571
- PPO: 1564

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1613 | 13.4% | 55.2% |
| HMO | 1572 | 13.9% | 55.9% |
| HDHP | 1571 | 12.7% | 59.5% |
| PPO | 1564 | 12.2% | 54.4% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1353 | 23.2% | 15.7% |
| PPO | 1373 | 24.0% | 15.5% |
| HDHP | 1372 | 21.9% | 15.0% |
| EPO | 1397 | 23.6% | 14.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 201 | $561,782 | 26.2% | $2,795 |
| not medically necessary | 195 | $513,063 | 23.9% | $2,631 |
| timely filing exceeded | 193 | $483,976 | 22.6% | $2,508 |
| out-of-network provider | 195 | $451,784 | 21.1% | $2,317 |
| duplicate claim | 41 | $131,841 | 6.2% | $3,216 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 144 (153 later claims)
- Later claims denied as duplicate: 41
- Later claims still paid: 102 ($212,485 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 273 | 14.4% | $294,769 | 3.3% |
| 2 claims | 420 | 22.1% | $1,139,097 | 12.8% |
| 3 claims | 420 | 22.1% | $1,682,194 | 18.9% |
| 4+ claims | 788 | 41.4% | $5,795,242 | 65.0% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1853 | 29.3% | $73,097 | 0.8% | 12.6% |
| $100-$999 | 2923 | 46.2% | $529,650 | 5.9% | 13.3% |
| $1,000-$9,999 | 1023 | 16.2% | $1,017,514 | 11.4% | 12.9% |
| $10,000+ | 521 | 8.2% | $7,291,041 | 81.8% | 13.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,320 | 6,320 | yes |
| claims: plan mix | 6,320 | 6,320 | yes |
| claims: plan performance | 6,320 | 6,320 | yes |
| claims: age bands | 6,320 | 6,320 | yes |
| claims: cost per member | 6,320 | 6,320 | yes |
| paid $: monthly view | 8,911,301.86 | 8,911,301.86 | yes |
| paid $: age bands | 8,911,310.32 | 8,911,301.86 | yes |
| denied claims: reasons | 825 | 825 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1183 |
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
| HDHP | 453 | 1571 | 3.47 | $5,851 |
| PPO | 483 | 1564 | 3.24 | $4,666 |
| EPO | 487 | 1613 | 3.31 | $4,369 |
| HMO | 478 | 1572 | 3.29 | $3,932 |

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
| 43239 | 558 | $1,145,300 | $877,687 | 76.6% |
| 27447 | 450 | $11,189,939 | $8,596,323 | 76.8% |
| 99213 | 570 | $68,465 | $52,989 | 77.4% |
| 85025 | 541 | $28,821 | $22,332 | 77.5% |
| 70450 | 553 | $360,664 | $279,784 | 77.6% |
| 99214 | 555 | $92,931 | $72,088 | 77.6% |

## Paid-amount concentration

Share of total paid (6320 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 64 | 17.2% |
| top 5% | 316 | 65.0% |
| top 10% | 632 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 201 | 70450 (12%), 85025 (12%), 99285 (11%) |
| not medically necessary | 195 | 43239 (13%), 93000 (13%), 99285 (13%) |
| out-of-network provider | 195 | 80053 (13%), 99285 (13%), 93000 (12%) |

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
| 27447 | 521 | $24,887 | $7,291,041 | 13.6% |
| 43239 | 644 | $2,044 | $741,456 | 13.4% |
| 99285 | 670 | $1,063 | $407,028 | 13.9% |
| 70450 | 631 | $648 | $236,560 | 12.4% |
| 99214 | 635 | $168 | $61,223 | 12.6% |

## Member utilization

1208 of 1901 synthetic members have 3+ claims and account for 83.9% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-1467 | 10 | $1,872 |
| MBR-1497 | 9 | $16,646 |
| MBR-1344 | 9 | $4,918 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 216 | out-of-network provider | 53 |
| HDHP | 199 | missing prior authorization | 53 |
| HMO | 219 | not medically necessary | 56 |
| PPO | 191 | missing prior authorization | 50 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1613 | 13.4% | 11.8% to 15.1% | no |
| HMO | 1572 | 13.9% | 12.3% to 15.7% | no |
| HDHP | 1571 | 12.7% | 11.1% to 14.4% | no |
| PPO | 1564 | 12.2% | 10.7% to 13.9% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $225 | $1,355 | $1,396 | $1,629 | $1,644 | $1,726 |
| HDHP | $343 | $1,867 | $1,603 | $1,525 | $2,037 | $2,713 |
| HMO | $266 | $1,614 | $1,502 | $1,221 | $1,387 | $1,355 |
| PPO | $263 | $1,460 | $1,670 | $1,430 | $1,714 | $1,960 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1208). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 685 | 56.7% |
| 1 denial | 384 | 31.8% |
| 2+ denials | 139 | 11.5% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1066 | 114 | 10.7% | missing prior authorization |
| 18-29 | 981 | 125 | 12.7% | timely filing exceeded |
| 30-44 | 1080 | 152 | 14.1% | not medically necessary |
| 45-59 | 1034 | 134 | 13.0% | out-of-network provider |
| 60-74 | 1097 | 137 | 12.5% | not medically necessary |
| 75+ | 1062 | 163 | 15.3% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1202.1% | +1139.4% | +3.74 pp |
| 2026-09 | +225.0% | +218.8% | +1.12 pp |
| 2026-10 | +0.1% | -8.2% | +0.59 pp |

## Potential duplicate services

144 groups share a member, procedure and service date (review queue, not a quality failure).

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
