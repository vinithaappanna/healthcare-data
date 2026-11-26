# Healthcare Data - claims pipeline report

Generated 2026-11-26 12:52 UTC. All data is synthetic - no real member, patient or plan information.

**6740 claims** in store. Billed $16,742,884, paid $9,451,197, denied 882 overall.

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
| 2026-09 | 2113 | $5,121,890 | $3,917,920 | $2,960,500 | 13.5% |
| 2026-10 | 2145 | $5,048,445 | $3,812,311 | $2,796,301 | 13.8% |
| 2026-11 | 1496 | $4,038,563 | $3,086,727 | $2,195,143 | 12.8% |

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
| 2026-08 | 632 | 9.4% |
| 2026-09 | 2113 | 31.4% |
| 2026-10 (largest) | 2145 | 31.8% |
| 2026-11 | 1496 | 22.2% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1179 | $2,607 | $1,764,840 | 12.5% |
| R51 | Headache | 1213 | $2,581 | $1,678,776 | 13.3% |
| E11.9 | Type 2 diabetes without complications | 1140 | $2,383 | $1,553,295 | 13.1% |
| Z00.00 | General adult medical exam | 873 | $2,984 | $1,540,646 | 13.9% |
| M54.5 | Low back pain | 1168 | $2,193 | $1,476,508 | 13.0% |
| J06.9 | Acute upper respiratory infection | 1167 | $2,276 | $1,437,132 | 13.1% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 80053 | 142 | 11.3% | $6,828 |
| R51 | 93000 | 141 | 8.5% | $8,354 |
| J06.9 | 93000 | 140 | 14.3% | $8,199 |
| M54.5 | 80053 | 136 | 11.8% | $6,103 |
| R51 | 43239 | 136 | 16.2% | $154,495 |
| M54.5 | 99285 | 129 | 15.5% | $79,305 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5190 | 77.0% | $12,516,756 | $8,184,833 |
| adjusted | 667 | 9.9% | $1,979,783 | $1,266,364 |
| denied | 883 | 13.1% | $2,246,345 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 77 | timely filing exceeded | 28.6% |
| 2026-09 | 285 | missing prior authorization | 27.0% |
| 2026-10 | 295 | missing prior authorization | 28.5% |
| 2026-11 | 191 | out-of-network provider | 24.6% |

## Denial reasons

- missing prior authorization (213)
- out-of-network provider (211)
- timely filing exceeded (206)
- not medically necessary (205)
- duplicate claim (48)

## Plan mix

- EPO: 1724
- HMO: 1679
- HDHP: 1671
- PPO: 1666

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1724 | 13.2% | 55.6% |
| HMO | 1679 | 13.7% | 56.6% |
| HDHP | 1671 | 13.1% | 59.4% |
| PPO | 1666 | 12.4% | 54.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 1459 | 23.7% | 15.7% |
| HMO | 1449 | 23.2% | 15.6% |
| HDHP | 1452 | 22.0% | 15.0% |
| EPO | 1497 | 23.5% | 14.9% |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1666 | 12.4% | 694,492.86 | 16.0% |
| EPO | 1724 | 13.2% | 605,274.14 | 14.7% |
| HDHP | 1671 | 13.1% | 480,805.52 | 10.4% |
| HMO | 1679 | 13.7% | 465,772.27 | 12.6% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 419 | 47.4% | 1,088,124.57 |
| network / coverage | 211 | 23.9% | 508,632.64 |
| clinical review | 205 | 23.2% | 516,395.45 |
| billing error | 48 | 5.4% | 133,192.13 |

## Payment ratios by claim status

Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.

| Status | Claims | Priced | Paid/allowed | Allowed/billed |
| --- | ---: | ---: | ---: | ---: |
| paid | 5190 | 5190 | 84.9% | 77.5% |
| adjusted | 667 | 667 | 84.5% | 77.8% |
| denied | 883 | 836 | 0.0% | 77.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 213 | $581,998 | 25.9% | $2,732 |
| not medically necessary | 205 | $516,395 | 23.0% | $2,519 |
| out-of-network provider | 211 | $508,633 | 22.6% | $2,411 |
| timely filing exceeded | 206 | $506,126 | 22.5% | $2,457 |
| duplicate claim | 48 | $133,192 | 5.9% | $2,775 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 155 (164 later claims)
- Later claims denied as duplicate: 48
- Later claims still paid: 106 ($214,378 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 242 | 12.6% | $282,128 | 3.0% |
| 2 claims | 393 | 20.5% | $1,079,539 | 11.4% |
| 3 claims | 409 | 21.3% | $1,621,473 | 17.2% |
| 4+ claims | 876 | 45.6% | $6,468,057 | 68.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1977 | 29.3% | $77,500 | 0.8% | 13.0% |
| $100-$999 | 3126 | 46.4% | $564,899 | 6.0% | 13.3% |
| $1,000-$9,999 | 1086 | 16.1% | $1,097,569 | 11.6% | 12.5% |
| $10,000+ | 551 | 8.2% | $7,711,229 | 81.6% | 13.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,740 | 6,740 | yes |
| claims: plan mix | 6,740 | 6,740 | yes |
| claims: plan performance | 6,740 | 6,740 | yes |
| claims: age bands | 6,740 | 6,740 | yes |
| claims: cost per member | 6,740 | 6,740 | yes |
| paid $: monthly view | 9,451,197.04 | 9,451,197.04 | yes |
| paid $: age bands | 9,451,191.56 | 9,451,197.04 | yes |
| denied claims: reasons | 883 | 883 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1603 |
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
| HDHP | 456 | 1671 | 3.66 | $5,994 |
| PPO | 486 | 1666 | 3.43 | $4,818 |
| EPO | 493 | 1724 | 3.50 | $4,644 |
| HMO | 485 | 1679 | 3.46 | $4,303 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1120 | 10 | 4 | 40.0% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0825 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 476 | $11,835,436 | $9,094,953 | 76.8% |
| 43239 | 609 | $1,253,106 | $966,866 | 77.2% |
| 99213 | 606 | $73,005 | $56,524 | 77.4% |
| 85025 | 578 | $30,681 | $23,762 | 77.5% |
| 97110 | 548 | $65,698 | $50,910 | 77.5% |
| 99214 | 585 | $97,779 | $75,796 | 77.5% |

## Paid-amount concentration

Share of total paid (6740 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 68 | 17.3% |
| top 5% | 337 | 65.2% |
| top 10% | 674 | 85.4% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 213 | 70450 (12%), 85025 (12%), 97110 (11%) |
| out-of-network provider | 211 | 93000 (14%), 80053 (13%), 99285 (12%) |
| timely filing exceeded | 206 | 93000 (13%), 99213 (12%), 85025 (11%) |

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
| 27447 | 551 | $24,866 | $7,711,229 | 13.6% |
| 43239 | 699 | $2,048 | $815,671 | 12.9% |
| 99285 | 696 | $1,060 | $422,078 | 13.4% |
| 70450 | 668 | $650 | $251,343 | 12.3% |
| 99214 | 671 | $168 | $64,343 | 12.8% |

## Member utilization

1285 of 1920 synthetic members have 3+ claims and account for 85.6% of paid dollars.

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
| EPO | 227 | out-of-network provider | 57 |
| HDHP | 219 | missing prior authorization | 58 |
| HMO | 230 | not medically necessary | 58 |
| PPO | 207 | missing prior authorization | 54 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1724 | 13.2% | 11.7% to 14.8% | no |
| HMO | 1679 | 13.7% | 12.1% to 15.4% | no |
| HDHP | 1671 | 13.1% | 11.6% to 14.8% | no |
| PPO | 1666 | 12.4% | 10.9% to 14.1% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $234 | $1,348 | $1,398 | $1,569 | $1,612 | $1,898 |
| HDHP | $341 | $1,803 | $1,519 | $1,519 | $2,050 | $2,590 |
| HMO | $268 | $1,738 | $1,601 | $1,296 | $1,357 | $1,393 |
| PPO | $263 | $1,429 | $1,721 | $1,402 | $1,645 | $1,853 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1285). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 714 | 55.6% |
| 1 denial | 411 | 32.0% |
| 2+ denials | 160 | 12.4% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1155 | 124 | 10.7% | missing prior authorization |
| 18-29 | 1032 | 134 | 13.0% | timely filing exceeded |
| 30-44 | 1140 | 158 | 13.9% | not medically necessary |
| 45-59 | 1110 | 141 | 12.7% | out-of-network provider |
| 60-74 | 1166 | 154 | 13.2% | not medically necessary |
| 75+ | 1137 | 172 | 15.1% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1244.7% | +1188.7% | +3.67 pp |
| 2026-09 | +234.3% | +221.5% | +1.31 pp |
| 2026-10 | +1.5% | -5.5% | +0.26 pp |

## Potential duplicate services

155 groups share a member, procedure and service date (review queue, not a quality failure).

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
