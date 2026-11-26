# Healthcare Data - claims pipeline report

Generated 2026-11-26 07:52 UTC. All data is synthetic - no real member, patient or plan information.

**6680 claims** in store. Billed $16,592,527, paid $9,355,820, denied 873 overall.

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
| 2026-08 | 632 | $1,632,476 | $1,250,604 | $920,890 | 12.2% |
| 2026-09 | 2095 | $5,090,013 | $3,894,984 | $2,942,044 | 13.5% |
| 2026-10 | 2122 | $4,993,306 | $3,768,518 | $2,756,700 | 13.8% |
| 2026-11 | 1477 | $3,975,222 | $3,036,959 | $2,157,823 | 12.7% |

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
| 2026-08 | 632 | 9.5% |
| 2026-09 | 2095 | 31.4% |
| 2026-10 (largest) | 2122 | 31.8% |
| 2026-11 | 1477 | 22.1% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1166 | $2,629 | $1,759,826 | 12.5% |
| R51 | Headache | 1205 | $2,594 | $1,674,266 | 13.2% |
| Z00.00 | General adult medical exam | 866 | $2,984 | $1,530,271 | 13.7% |
| E11.9 | Type 2 diabetes without complications | 1128 | $2,335 | $1,503,708 | 13.1% |
| M54.5 | Low back pain | 1155 | $2,192 | $1,454,030 | 13.0% |
| J06.9 | Acute upper respiratory infection | 1160 | $2,286 | $1,433,720 | 13.1% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| J06.9 | 93000 | 139 | 14.4% | $8,084 |
| R51 | 80053 | 139 | 10.8% | $6,662 |
| R51 | 93000 | 139 | 7.9% | $8,298 |
| R51 | 43239 | 134 | 16.4% | $150,304 |
| M54.5 | 80053 | 133 | 12.0% | $5,958 |
| M54.5 | 99285 | 128 | 15.6% | $78,862 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5149 | 77.1% | $12,438,841 | $8,133,495 |
| adjusted | 657 | 9.8% | $1,908,956 | $1,222,324 |
| denied | 874 | 13.1% | $2,244,730 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 283 | missing prior authorization | 27.2% |
| 2026-10 | 292 | missing prior authorization | 27.7% |
| 2026-11 | 187 | out-of-network provider | 24.6% |

## Denial reasons

- missing prior authorization (210)
- out-of-network provider (209)
- timely filing exceeded (204)
- not medically necessary (204)
- duplicate claim (47)

## Plan mix

- EPO: 1708
- HMO: 1661
- PPO: 1656
- HDHP: 1655

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1708 | 13.1% | 55.4% |
| HMO | 1661 | 13.7% | 56.6% |
| PPO | 1656 | 12.4% | 54.0% |
| HDHP | 1655 | 13.1% | 59.4% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1433 | 23.1% | 15.7% |
| PPO | 1451 | 23.7% | 15.6% |
| HDHP | 1438 | 22.0% | 14.9% |
| EPO | 1484 | 23.5% | 14.8% |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1656 | 12.4% | 694,138.61 | 16.1% |
| EPO | 1708 | 13.1% | 605,000.51 | 14.9% |
| HDHP | 1655 | 13.1% | 480,603.63 | 10.5% |
| HMO | 1661 | 13.7% | 464,986.89 | 12.8% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 414 | 47.4% | 1,087,014.95 |
| network / coverage | 209 | 23.9% | 508,412.57 |
| clinical review | 204 | 23.3% | 516,229.46 |
| billing error | 47 | 5.4% | 133,072.66 |

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5149 | 5149 | 84.9% | 77.5% |
| adjusted | 657 | 657 | 84.6% | 77.8% |
| denied | 874 | 828 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 210 | $581,626 | 25.9% | $2,770 |
| not medically necessary | 204 | $516,229 | 23.0% | $2,531 |
| out-of-network provider | 209 | $508,413 | 22.7% | $2,433 |
| timely filing exceeded | 204 | $505,389 | 22.5% | $2,477 |
| duplicate claim | 47 | $133,073 | 5.9% | $2,831 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 154 (163 later claims)
- Later claims denied as duplicate: 47
- Later claims still paid: 106 ($214,378 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 245 | 12.8% | $283,813 | 3.0% |
| 2 claims | 395 | 20.6% | $1,066,018 | 11.4% |
| 3 claims | 414 | 21.6% | $1,700,981 | 18.2% |
| 4+ claims | 862 | 45.0% | $6,305,007 | 67.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1964 | 29.4% | $76,963 | 0.8% | 13.0% |
| $100-$999 | 3095 | 46.3% | $560,199 | 6.0% | 13.2% |
| $1,000-$9,999 | 1075 | 16.1% | $1,080,702 | 11.6% | 12.7% |
| $10,000+ | 546 | 8.2% | $7,637,956 | 81.6% | 13.7% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,680 | 6,680 | yes |
| claims: plan mix | 6,680 | 6,680 | yes |
| claims: plan performance | 6,680 | 6,680 | yes |
| claims: age bands | 6,680 | 6,680 | yes |
| claims: cost per member | 6,680 | 6,680 | yes |
| paid $: monthly view | 9,355,819.77 | 9,355,819.77 | yes |
| paid $: age bands | 9,355,819.25 | 9,355,819.77 | yes |
| denied claims: reasons | 874 | 874 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1543 |
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
| HDHP | 456 | 1655 | 3.63 | $5,960 |
| PPO | 485 | 1656 | 3.41 | $4,790 |
| EPO | 492 | 1708 | 3.47 | $4,577 |
| HMO | 483 | 1661 | 3.44 | $4,272 |

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
| 27447 | 471 | $11,719,090 | $9,005,776 | 76.8% |
| 43239 | 599 | $1,230,439 | $948,086 | 77.0% |
| 85025 | 575 | $30,516 | $23,629 | 77.4% |
| 99213 | 601 | $72,350 | $56,036 | 77.5% |
| 97110 | 546 | $65,480 | $50,729 | 77.5% |
| 99214 | 581 | $97,159 | $75,347 | 77.5% |

## Paid-amount concentration

Share of total paid (6680 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 67 | 17.2% |
| top 5% | 334 | 65.4% |
| top 10% | 668 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 210 | 70450 (12%), 85025 (12%), 97110 (11%) |
| out-of-network provider | 209 | 93000 (14%), 80053 (13%), 99285 (12%) |
| not medically necessary | 204 | 93000 (14%), 43239 (13%), 99285 (12%) |

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
| 27447 | 546 | $24,881 | $7,637,956 | 13.7% |
| 43239 | 689 | $2,045 | $799,644 | 13.1% |
| 99285 | 692 | $1,060 | $419,817 | 13.4% |
| 70450 | 662 | $650 | $249,495 | 12.2% |
| 99214 | 665 | $168 | $63,964 | 12.6% |

## Member utilization

1276 of 1916 synthetic members have 3+ claims and account for 85.6% of paid dollars.

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
| EPO | 224 | out-of-network provider | 55 |
| HDHP | 217 | missing prior authorization | 57 |
| HMO | 228 | not medically necessary | 58 |
| PPO | 205 | missing prior authorization | 53 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1708 | 13.1% | 11.6% to 14.8% | no |
| HMO | 1661 | 13.7% | 12.2% to 15.5% | no |
| PPO | 1656 | 12.4% | 10.9% to 14.1% | no |
| HDHP | 1655 | 13.1% | 11.6% to 14.8% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $230 | $1,348 | $1,351 | $1,590 | $1,618 | $1,867 |
| HDHP | $331 | $1,813 | $1,519 | $1,530 | $2,047 | $2,617 |
| HMO | $268 | $1,745 | $1,548 | $1,303 | $1,383 | $1,405 |
| PPO | $258 | $1,395 | $1,727 | $1,406 | $1,645 | $1,860 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1276). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 708 | 55.5% |
| 1 denial | 411 | 32.2% |
| 2+ denials | 157 | 12.3% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1143 | 121 | 10.6% | missing prior authorization |
| 18-29 | 1025 | 134 | 13.1% | timely filing exceeded |
| 30-44 | 1133 | 157 | 13.9% | not medically necessary |
| 45-59 | 1101 | 141 | 12.8% | out-of-network provider |
| 60-74 | 1154 | 153 | 13.3% | not medically necessary |
| 75+ | 1124 | 168 | 14.9% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1244.7% | +1188.7% | +3.67 pp |
| 2026-09 | +231.5% | +219.5% | +1.33 pp |
| 2026-10 | +1.3% | -6.3% | +0.25 pp |

## Potential duplicate services

154 groups share a member, procedure and service date (review queue, not a quality failure).

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
