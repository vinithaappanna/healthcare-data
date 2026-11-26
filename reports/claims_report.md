# Healthcare Data - claims pipeline report

Generated 2026-11-26 02:51 UTC. All data is synthetic - no real member, patient or plan information.

**6620 claims** in store. Billed $16,483,537, paid $9,275,717, denied 864 overall.

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
| 2026-08 | 629 | $1,609,444 | $1,231,697 | $904,445 | 12.1% |
| 2026-09 | 2071 | $5,051,748 | $3,861,515 | $2,913,069 | 13.5% |
| 2026-10 | 2105 | $4,968,523 | $3,748,659 | $2,739,843 | 13.8% |
| 2026-11 | 1461 | $3,952,312 | $3,017,171 | $2,139,996 | 12.6% |

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
| 2026-08 | 629 | 9.5% |
| 2026-09 | 2071 | 31.3% |
| 2026-10 (largest) | 2105 | 31.8% |
| 2026-11 | 1461 | 22.1% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1157 | $2,647 | $1,758,100 | 12.5% |
| R51 | Headache | 1192 | $2,580 | $1,636,788 | 13.3% |
| Z00.00 | General adult medical exam | 861 | $2,981 | $1,517,751 | 13.7% |
| E11.9 | Type 2 diabetes without complications | 1113 | $2,338 | $1,477,618 | 13.0% |
| M54.5 | Low back pain | 1147 | $2,204 | $1,452,637 | 12.9% |
| J06.9 | Acute upper respiratory infection | 1150 | $2,304 | $1,432,824 | 13.0% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 138 | 8.0% | $8,229 |
| J06.9 | 93000 | 137 | 14.6% | $7,963 |
| R51 | 80053 | 136 | 11.0% | $6,535 |
| M54.5 | 80053 | 133 | 12.0% | $5,958 |
| R51 | 43239 | 132 | 16.7% | $146,688 |
| M54.5 | 99285 | 128 | 15.6% | $78,862 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 5104 | 77.1% | $12,378,069 | $8,089,180 |
| adjusted | 651 | 9.8% | $1,863,498 | $1,186,537 |
| denied | 865 | 13.1% | $2,241,970 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 76 | not medically necessary | 27.6% |
| 2026-09 | 279 | missing prior authorization | 27.2% |
| 2026-10 | 291 | missing prior authorization | 27.8% |
| 2026-11 | 184 | out-of-network provider | 25.0% |

## Denial reasons

- missing prior authorization (208)
- out-of-network provider (208)
- not medically necessary (202)
- timely filing exceeded (201)
- duplicate claim (46)

## Plan mix

- EPO: 1691
- HMO: 1646
- HDHP: 1645
- PPO: 1638

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1691 | 13.2% | 55.4% |
| HMO | 1646 | 13.8% | 56.3% |
| HDHP | 1645 | 13.1% | 59.2% |
| PPO | 1638 | 12.2% | 54.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1419 | 23.3% | 15.8% |
| PPO | 1439 | 23.8% | 15.6% |
| HDHP | 1429 | 22.1% | 15.0% |
| EPO | 1468 | 23.5% | 14.8% |

## Denied dollars by plan

Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.

| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |
| --- | ---: | ---: | ---: | ---: |
| PPO | 1638 | 12.2% | 693,459.58 | 16.1% |
| EPO | 1691 | 13.2% | 603,061.63 | 14.9% |
| HDHP | 1645 | 13.1% | 480,575.85 | 10.6% |
| HMO | 1646 | 13.8% | 464,873.03 | 12.9% |

## Denials by broad category

Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.

| Category | Denied claims | Share | Billed ($) |
| --- | ---: | ---: | ---: |
| administrative process | 409 | 47.3% | 1,086,576.37 |
| network / coverage | 208 | 24.1% | 508,298.71 |
| clinical review | 202 | 23.4% | 514,210.75 |
| billing error | 46 | 5.3% | 132,884.26 |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 208 | $581,380 | 25.9% | $2,795 |
| not medically necessary | 202 | $514,211 | 22.9% | $2,546 |
| out-of-network provider | 208 | $508,299 | 22.7% | $2,444 |
| timely filing exceeded | 201 | $505,197 | 22.5% | $2,513 |
| duplicate claim | 46 | $132,884 | 5.9% | $2,889 |

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
| 1 claim | 249 | 13.0% | $284,724 | 3.1% |
| 2 claims | 397 | 20.8% | $1,053,869 | 11.4% |
| 3 claims | 418 | 21.9% | $1,689,043 | 18.2% |
| 4+ claims | 849 | 44.4% | $6,248,081 | 67.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1945 | 29.4% | $76,319 | 0.8% | 12.9% |
| $100-$999 | 3063 | 46.3% | $554,760 | 6.0% | 13.2% |
| $1,000-$9,999 | 1070 | 16.2% | $1,075,242 | 11.6% | 12.6% |
| $10,000+ | 542 | 8.2% | $7,569,396 | 81.6% | 13.8% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 6,620 | 6,620 | yes |
| claims: plan mix | 6,620 | 6,620 | yes |
| claims: plan performance | 6,620 | 6,620 | yes |
| claims: age bands | 6,620 | 6,620 | yes |
| claims: cost per member | 6,620 | 6,620 | yes |
| paid $: monthly view | 9,275,717.17 | 9,275,717.17 | yes |
| paid $: age bands | 9,275,708.7 | 9,275,717.17 | yes |
| denied claims: reasons | 865 | 865 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1483 |
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
| HDHP | 455 | 1645 | 3.62 | $5,907 |
| PPO | 484 | 1638 | 3.38 | $4,789 |
| EPO | 491 | 1691 | 3.44 | $4,580 |
| HMO | 483 | 1646 | 3.41 | $4,185 |

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
| 27447 | 467 | $11,630,384 | $8,929,529 | 76.8% |
| 43239 | 596 | $1,223,909 | $942,388 | 77.0% |
| 85025 | 572 | $30,402 | $23,539 | 77.4% |
| 97110 | 537 | $64,420 | $49,878 | 77.4% |
| 99213 | 596 | $71,789 | $55,625 | 77.5% |
| 70450 | 575 | $375,946 | $291,620 | 77.6% |

## Paid-amount concentration

Share of total paid (6620 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 67 | 17.3% |
| top 5% | 331 | 65.3% |
| top 10% | 662 | 85.4% |

Gini coefficient of paid per claim: **0.872** (0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0).

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| missing prior authorization | 208 | 70450 (12%), 85025 (12%), 99285 (11%) |
| out-of-network provider | 208 | 93000 (14%), 80053 (13%), 99285 (12%) |
| not medically necessary | 202 | 93000 (14%), 43239 (13%), 99285 (12%) |

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
| 27447 | 542 | $24,901 | $7,569,396 | 13.8% |
| 43239 | 685 | $2,044 | $795,057 | 13.0% |
| 99285 | 689 | $1,061 | $418,034 | 13.5% |
| 70450 | 656 | $649 | $246,593 | 12.3% |
| 99214 | 660 | $168 | $63,571 | 12.6% |

## Member utilization

1267 of 1913 synthetic members have 3+ claims and account for 85.6% of paid dollars.

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
| EPO | 223 | out-of-network provider | 55 |
| HDHP | 216 | missing prior authorization | 57 |
| HMO | 227 | not medically necessary | 58 |
| PPO | 199 | missing prior authorization | 51 |

## Plan denial rates with 95% intervals

Wilson score intervals. The generator draws denials at the same rate for every plan, so overlap with the overall rate is expected; plan labels carry no benefit realism.

| Plan | Claims | Denial rate | 95% interval | Differs from overall |
| --- | ---: | ---: | --- | --- |
| EPO | 1691 | 13.2% | 11.7% to 14.9% | no |
| HMO | 1646 | 13.8% | 12.2% to 15.5% | no |
| HDHP | 1645 | 13.1% | 11.6% to 14.8% | no |
| PPO | 1638 | 12.2% | 10.7% to 13.8% | no |

## Average paid per claim: plan x age band

Denied claims count as 0; cells under 20 claims show '-'. Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).

| Plan | 0-17 | 18-29 | 30-44 | 45-59 | 60-74 | 75+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EPO | $233 | $1,349 | $1,360 | $1,616 | $1,634 | $1,871 |
| HDHP | $333 | $1,820 | $1,522 | $1,483 | $2,015 | $2,617 |
| HMO | $268 | $1,583 | $1,562 | $1,308 | $1,383 | $1,428 |
| PPO | $262 | $1,405 | $1,733 | $1,427 | $1,651 | $1,876 |

## Procedure denial-rate screen

10 procedure codes with 30+ claims tested against the overall denial rate (13.1%) using 95% Wilson intervals. With this many tests an occasional hit is expected by chance, and the generator uses one denial rate for every code: leads for review, not findings.

No procedure's interval excludes the overall rate.

## Member denial experience

Members with 3+ claims (1267). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 705 | 55.6% |
| 1 denial | 408 | 32.2% |
| 2+ denials | 154 | 12.2% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 1126 | 119 | 10.6% | missing prior authorization |
| 18-29 | 1019 | 133 | 13.1% | timely filing exceeded |
| 30-44 | 1126 | 156 | 13.9% | not medically necessary |
| 45-59 | 1086 | 139 | 12.8% | out-of-network provider |
| 60-74 | 1149 | 151 | 13.1% | not medically necessary |
| 75+ | 1114 | 167 | 15.0% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1238.3% | +1165.7% | +3.57 pp |
| 2026-09 | +229.2% | +222.1% | +1.39 pp |
| 2026-10 | +1.6% | -5.9% | +0.35 pp |

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
