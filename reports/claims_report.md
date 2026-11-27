# Healthcare Data - claims pipeline report

Generated 2026-11-27 13:55 UTC. All data is synthetic - no real member, patient or plan information.

**7040 claims** in store. Billed $17,629,357, paid $10,011,265, denied 919 overall.

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
| 2026-09 | 2233 | $5,503,704 | $4,224,005 | $3,199,678 | 13.2% |
| 2026-10 | 2244 | $5,301,645 | $4,009,824 | $2,948,780 | 13.8% |
| 2026-11 | 1569 | $4,260,628 | $3,264,974 | $2,344,745 | 12.9% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.6% |
| 2026-01 | 31 | 0.4% |
| 2026-02 | 32 | 0.4% |
| 2026-03 | 45 | 0.6% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 640 | 9.1% |
| 2026-09 | 2233 | 31.7% |
| 2026-10 (largest) | 2244 | 31.9% |
| 2026-11 | 1569 | 22.3% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1236 | $2,579 | $1,837,680 | 12.2% |
| R51 | Headache | 1266 | $2,595 | $1,753,206 | 13.3% |
| Z00.00 | General adult medical exam | 917 | $3,056 | $1,681,389 | 13.6% |
| E11.9 | Type 2 diabetes without complications | 1186 | $2,378 | $1,598,509 | 13.2% |
| J06.9 | Acute upper respiratory infection | 1224 | $2,328 | $1,578,162 | 13.3% |
| M54.5 | Low back pain | 1211 | $2,216 | $1,562,318 | 12.8% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| J06.9 | 93000 | 150 | 13.3% | $8,774 |
| R51 | 80053 | 149 | 12.1% | $7,039 |
| R51 | 93000 | 148 | 8.1% | $8,863 |
| R51 | 43239 | 140 | 17.1% | $157,808 |
| M54.5 | 80053 | 139 | 11.5% | $6,252 |
| E11.9 | 93000 | 135 | 16.3% | $7,558 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5432 | 77.2% | $13,293,995 | $8,719,159 |
| adjusted | 689 | 9.8% | $2,025,084 | $1,292,106 |
| denied | 919 | 13.1% | $2,310,277 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 294 | missing prior authorization | 26.5% |
| 2026-10 | 310 | missing prior authorization | 28.4% |
| 2026-11 | 203 | out-of-network provider | 25.1% |

## Denial reasons

- out-of-network provider (221)
- missing prior authorization (220)
- not medically necessary (214)
- timely filing exceeded (213)
- duplicate claim (51)

## Plan mix

- EPO: 1807
- HMO: 1748
- HDHP: 1744
- PPO: 1741

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1807 | 13.1% | 55.4% |
| HMO | 1748 | 13.7% | 56.8% |
| HDHP | 1744 | 13.0% | 60.4% |
| PPO | 1741 | 12.5% | 54.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1524 | 23.7% | 15.7% |
| HMO | 1509 | 22.8% | 15.5% |
| EPO | 1571 | 23.9% | 15.1% |
| HDHP | 1517 | 21.6% | 14.6% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 7040 claims: chi2 = 1.126, df = 3, p = 0.7709. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1741 | 12.5% | 700,035.78 | 15.8% |
| EPO | 1807 | 13.1% | 610,857.39 | 14.2% |
| HMO | 1748 | 13.7% | 515,434.32 | 13.0% |
| HDHP | 1744 | 13.0% | 483,949.76 | 9.8% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 433 | 47.1% | 1,137,457.76 |
| network / coverage | 221 | 24.1% | 513,522.78 |
| clinical review | 214 | 23.3% | 523,891.83 |
| billing error | 51 | 5.5% | 135,404.88 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5432 | 5432 | 84.9% | 77.5% |
| adjusted | 689 | 689 | 84.6% | 77.8% |
| denied | 919 | 869 | 0.0% | 77.3% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 220 | $583,222 | 25.2% | $2,651 |
| timely filing exceeded | 213 | $554,236 | 24.0% | $2,602 |
| not medically necessary | 214 | $523,892 | 22.7% | $2,448 |
| out-of-network provider | 221 | $513,523 | 22.2% | $2,324 |
| duplicate claim | 51 | $135,405 | 5.9% | $2,655 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 161 (170 later claims)
- Later claims denied as duplicate: 51
- Later claims still paid: 109 ($215,137 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 229 | 11.9% | $278,150 | 2.8% |
| 2 claims | 358 | 18.5% | $810,681 | 8.1% |
| 3 claims | 406 | 21.0% | $1,824,226 | 18.2% |
| 4+ claims | 938 | 48.6% | $7,098,207 | 70.9% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2069 | 29.4% | $81,007 | 0.8% | 13.0% |
| $100-$999 | 3258 | 46.3% | $590,979 | 5.9% | 13.2% |
| $1,000-$9,999 | 1130 | 16.1% | $1,136,833 | 11.4% | 12.7% |
| $10,000+ | 583 | 8.3% | $8,202,446 | 81.9% | 13.2% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 7,040 | 7,040 | yes |
| claims: plan mix | 7,040 | 7,040 | yes |
| claims: plan performance | 7,040 | 7,040 | yes |
| claims: age bands | 7,040 | 7,040 | yes |
| claims: cost per member | 7,040 | 7,040 | yes |
| paid $: monthly view | 10,011,264.52 | 10,011,264.52 | yes |
| paid $: age bands | 10,011,267.15 | 10,011,264.52 | yes |
| denied claims: reasons | 919 | 919 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1903 |
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
| HDHP | 459 | 1744 | 3.80 | $6,480 |
| PPO | 488 | 1741 | 3.57 | $4,910 |
| EPO | 495 | 1807 | 3.65 | $4,830 |
| HMO | 489 | 1748 | 3.57 | $4,601 |

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
| 27447 | 506 | $12,554,562 | $9,667,624 | 77.0% |
| 43239 | 631 | $1,295,835 | $1,001,279 | 77.3% |
| 85025 | 603 | $31,958 | $24,717 | 77.3% |
| 97110 | 578 | $69,423 | $53,698 | 77.3% |
| 99214 | 603 | $100,873 | $78,073 | 77.4% |
| 99213 | 630 | $75,830 | $58,738 | 77.5% |

## Paid-amount concentration

Share of total paid (7040 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 71 | 17.2% |
| top 5% | 352 | 64.8% |
| top 10% | 704 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 221 | 80053 (14%), 93000 (14%), 99285 (11%) |
| missing prior authorization | 220 | 70450 (12%), 85025 (12%), 97110 (11%) |
| not medically necessary | 214 | 43239 (14%), 93000 (14%), 99285 (13%) |

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
| 27447 | 583 | $24,814 | $8,202,446 | 13.2% |
| 43239 | 727 | $2,043 | $844,249 | 13.2% |
| 99285 | 727 | $1,057 | $440,266 | 13.2% |
| 70450 | 694 | $650 | $262,773 | 12.1% |
| 99214 | 692 | $168 | $66,304 | 12.9% |

## Member utilization

1344 of 1931 synthetic members have 3+ claims and account for 89.1% of paid dollars.

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
| EPO | 236 | not medically necessary | 59 |
| HDHP | 227 | missing prior authorization | 61 |
| HMO | 239 | not medically necessary | 60 |
| PPO | 217 | missing prior authorization | 55 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1807 | 13.1% | 11.6% to 14.7% | no |
| HMO | 1748 | 13.7% | 12.1% to 15.4% | no |
| HDHP | 1744 | 13.0% | 11.5% to 14.7% | no |
| PPO | 1741 | 12.5% | 11.0% to 14.1% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $229 | $1,300 | $1,419 | $1,631 | $1,626 | $1,812 |
| HDHP | $335 | $2,027 | $1,658 | $1,563 | $2,011 | $2,650 |
| HMO | $270 | $1,824 | $1,620 | $1,466 | $1,358 | $1,395 |
| PPO | $260 | $1,399 | $1,742 | $1,345 | $1,612 | $1,780 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1344). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 746 | 55.5% |
| 1 denial | 426 | 31.7% |
| 2+ denials | 172 | 12.8% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1202 | 129 | 10.7% | out-of-network provider |
| 18-29 | 1074 | 135 | 12.6% | timely filing exceeded |
| 30-44 | 1182 | 164 | 13.9% | not medically necessary |
| 45-59 | 1165 | 149 | 12.8% | out-of-network provider |
| 60-74 | 1216 | 159 | 13.1% | not medically necessary |
| 75+ | 1201 | 183 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1261.7% | +1215.0% | +3.52 pp |
| 2026-09 | +248.9% | +240.5% | +1.14 pp |
| 2026-10 | +0.5% | -7.8% | +0.64 pp |

## Potential duplicate services

161 groups share a member, procedure and service date (review queue, not a quality failure).

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
