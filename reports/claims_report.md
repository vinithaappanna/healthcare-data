# Healthcare Data - claims pipeline report

Generated 2026-11-27 03:54 UTC. All data is synthetic - no real member, patient or plan information.

**6920 claims** in store. Billed $17,239,219, paid $9,771,532, denied 905 overall.

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
| 2026-08 | 638 | $1,661,712 | $1,274,449 | $939,596 | 12.1% |
| 2026-09 | 2184 | $5,341,946 | $4,101,366 | $3,120,575 | 13.3% |
| 2026-10 | 2206 | $5,217,836 | $3,946,565 | $2,897,458 | 13.8% |
| 2026-11 | 1538 | $4,116,214 | $3,139,264 | $2,235,540 | 12.8% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.6% |
| 2026-01 | 31 | 0.4% |
| 2026-02 | 32 | 0.5% |
| 2026-03 | 45 | 0.7% |
| 2026-04 | 48 | 0.7% |
| 2026-05 | 43 | 0.6% |
| 2026-06 | 46 | 0.7% |
| 2026-07 | 47 | 0.7% |
| 2026-08 | 638 | 9.2% |
| 2026-09 | 2184 | 31.6% |
| 2026-10 (largest) | 2206 | 31.9% |
| 2026-11 | 1538 | 22.2% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1211 | $2,606 | $1,818,796 | 12.3% |
| R51 | Headache | 1244 | $2,588 | $1,718,605 | 13.3% |
| Z00.00 | General adult medical exam | 901 | $2,995 | $1,594,220 | 13.9% |
| E11.9 | Type 2 diabetes without complications | 1165 | $2,368 | $1,579,735 | 13.1% |
| M54.5 | Low back pain | 1195 | $2,218 | $1,544,110 | 12.9% |
| J06.9 | Acute upper respiratory infection | 1204 | $2,290 | $1,516,066 | 13.2% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 148 | 12.2% | $7,004 |
| J06.9 | 93000 | 146 | 13.7% | $8,535 |
| R51 | 93000 | 146 | 8.2% | $8,735 |
| M54.5 | 80053 | 137 | 11.7% | $6,167 |
| R51 | 43239 | 137 | 16.1% | $155,832 |
| E11.9 | 93000 | 133 | 16.5% | $7,334 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5335 | 77.1% | $12,941,990 | $8,482,535 |
| adjusted | 680 | 9.8% | $2,020,551 | $1,288,997 |
| denied | 905 | 13.1% | $2,276,677 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 291 | missing prior authorization | 26.8% |
| 2026-10 | 305 | missing prior authorization | 28.2% |
| 2026-11 | 197 | out-of-network provider | 24.9% |

## Denial reasons

- missing prior authorization (217)
- out-of-network provider (217)
- timely filing exceeded (211)
- not medically necessary (210)
- duplicate claim (50)

## Plan mix

- EPO: 1779
- HDHP: 1716
- HMO: 1716
- PPO: 1709

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1779 | 13.0% | 55.5% |
| HDHP | 1716 | 13.1% | 60.2% |
| HMO | 1716 | 13.7% | 56.5% |
| PPO | 1709 | 12.5% | 54.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1481 | 23.1% | 15.7% |
| PPO | 1496 | 23.7% | 15.6% |
| EPO | 1547 | 23.7% | 15.1% |
| HDHP | 1491 | 21.6% | 14.7% |

## Plan vs denial: independence test

Chi-square test of plan type against denied/not denied over 6920 claims: chi2 = 1.146, df = 3, p = 0.7661. Plan is a synthetic label drawn independently of denial status, so a small p-value would point to a generator or data problem, not real plan behavior. A large p-value is the expected result and is not evidence of fairness or equal treatment.

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1709 | 12.5% | 697,815.75 | 16.0% |
| EPO | 1779 | 13.0% | 607,219.42 | 14.3% |
| HMO | 1716 | 13.7% | 487,984.48 | 12.8% |
| HDHP | 1716 | 13.1% | 483,657.53 | 10.0% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 428 | 47.3% | 1,109,743.97 |
| network / coverage | 217 | 24.0% | 511,331.68 |
| clinical review | 210 | 23.2% | 520,241.64 |
| billing error | 50 | 5.5% | 135,359.89 |

![Denials by broad category](denial_categories.png)

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5335 | 5335 | 84.9% | 77.5% |
| adjusted | 680 | 680 | 84.6% | 77.8% |
| denied | 905 | 856 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 217 | $582,968 | 25.6% | $2,686 |
| timely filing exceeded | 211 | $526,776 | 23.1% | $2,497 |
| not medically necessary | 210 | $520,242 | 22.9% | $2,477 |
| out-of-network provider | 217 | $511,332 | 22.5% | $2,356 |
| duplicate claim | 50 | $135,360 | 5.9% | $2,707 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 158 (167 later claims)
- Later claims denied as duplicate: 50
- Later claims still paid: 107 ($214,506 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 235 | 12.2% | $280,023 | 2.9% |
| 2 claims | 367 | 19.1% | $872,286 | 8.9% |
| 3 claims | 410 | 21.3% | $1,736,651 | 17.8% |
| 4+ claims | 914 | 47.5% | $6,882,572 | 70.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 2037 | 29.4% | $79,802 | 0.8% | 13.0% |
| $100-$999 | 3207 | 46.3% | $580,650 | 5.9% | 13.2% |
| $1,000-$9,999 | 1108 | 16.0% | $1,115,709 | 11.4% | 12.7% |
| $10,000+ | 568 | 8.2% | $7,995,372 | 81.8% | 13.4% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,920 | 6,920 | yes |
| claims: plan mix | 6,920 | 6,920 | yes |
| claims: plan performance | 6,920 | 6,920 | yes |
| claims: age bands | 6,920 | 6,920 | yes |
| claims: cost per member | 6,920 | 6,920 | yes |
| paid $: monthly view | 9,771,532.05 | 9,771,532.05 | yes |
| paid $: age bands | 9,771,533.27 | 9,771,532.05 | yes |
| denied claims: reasons | 905 | 905 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1783 |
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
| HDHP | 457 | 1716 | 3.75 | $6,339 |
| PPO | 487 | 1709 | 3.51 | $4,864 |
| EPO | 494 | 1779 | 3.60 | $4,764 |
| HMO | 488 | 1716 | 3.52 | $4,410 |

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
| 27447 | 492 | $12,247,146 | $9,424,012 | 77.0% |
| 43239 | 620 | $1,274,155 | $983,156 | 77.2% |
| 85025 | 599 | $31,720 | $24,536 | 77.3% |
| 97110 | 567 | $67,927 | $52,632 | 77.5% |
| 99213 | 623 | $75,066 | $58,160 | 77.5% |
| 99214 | 595 | $99,617 | $77,183 | 77.5% |

## Paid-amount concentration

Share of total paid (6920 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 70 | 17.3% |
| top 5% | 346 | 65.1% |
| top 10% | 692 | 85.5% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 217 | 70450 (12%), 85025 (12%), 97110 (12%) |
| out-of-network provider | 217 | 93000 (14%), 80053 (13%), 99285 (12%) |
| timely filing exceeded | 211 | 93000 (13%), 99213 (11%), 85025 (11%) |

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
| 27447 | 568 | $24,880 | $7,995,372 | 13.4% |
| 43239 | 714 | $2,045 | $828,867 | 13.2% |
| 99285 | 710 | $1,058 | $430,991 | 13.2% |
| 70450 | 686 | $649 | $258,672 | 12.2% |
| 99214 | 682 | $168 | $65,528 | 12.8% |

## Member utilization

1324 of 1926 synthetic members have 3+ claims and account for 88.2% of paid dollars.

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
| EPO | 232 | out-of-network provider | 58 |
| HDHP | 225 | missing prior authorization | 61 |
| HMO | 235 | not medically necessary | 60 |
| PPO | 213 | missing prior authorization | 55 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1779 | 13.0% | 11.6% to 14.7% | no |
| HDHP | 1716 | 13.1% | 11.6% to 14.8% | no |
| HMO | 1716 | 13.7% | 12.2% to 15.4% | no |
| PPO | 1709 | 12.5% | 11.0% to 14.1% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $231 | $1,314 | $1,437 | $1,621 | $1,575 | $1,850 |
| HDHP | $334 | $1,925 | $1,671 | $1,577 | $2,013 | $2,616 |
| HMO | $272 | $1,749 | $1,637 | $1,345 | $1,338 | $1,372 |
| PPO | $261 | $1,414 | $1,762 | $1,358 | $1,639 | $1,789 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1324). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 737 | 55.7% |
| 1 denial | 417 | 31.5% |
| 2+ denials | 170 | 12.8% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1186 | 127 | 10.7% | missing prior authorization |
| 18-29 | 1057 | 134 | 12.7% | timely filing exceeded |
| 30-44 | 1163 | 161 | 13.8% | not medically necessary |
| 45-59 | 1149 | 148 | 12.9% | out-of-network provider |
| 60-74 | 1193 | 158 | 13.2% | not medically necessary |
| 75+ | 1172 | 177 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1257.5% | +1214.9% | +3.56 pp |
| 2026-09 | +242.3% | +232.1% | +1.25 pp |
| 2026-10 | +1.0% | -7.1% | +0.51 pp |

## Potential duplicate services

158 groups share a member, procedure and service date (review queue, not a quality failure).

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
