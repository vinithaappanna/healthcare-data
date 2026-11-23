# Healthcare Data - claims pipeline report

Generated 2026-11-23 19:38 UTC. All data is synthetic - no real member, patient or plan information.

**5000 claims** in store. Billed $12,494,837, paid $7,123,926, denied 644 overall.

## Monthly financials

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
| 2026-08 | 50 | $87,251 | $70,911 | $55,220 | 18.0% |
| 2026-09 | 28 | $74,375 | $60,854 | $33,931 | 7.1% |
| 2026-10 | 47 | $52,142 | $37,586 | $29,094 | 8.5% |
| 2026-11 | 4521 | $11,379,559 | $8,694,335 | $6,427,318 | 13.1% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 868 | $2,640 | $1,324,473 | 12.2% |
| Z00.00 | General adult medical exam | 677 | $2,868 | $1,212,704 | 12.8% |
| R51 | Headache | 906 | $2,547 | $1,207,994 | 14.5% |
| J06.9 | Acute upper respiratory infection | 854 | $2,497 | $1,195,263 | 12.9% |
| M54.5 | Low back pain | 859 | $2,282 | $1,121,590 | 12.3% |
| E11.9 | Type 2 diabetes without complications | 836 | $2,227 | $1,061,901 | 12.4% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 108 | 8.3% | $6,262 |
| M54.5 | 99285 | 103 | 17.5% | $61,861 |
| R51 | 43239 | 102 | 18.6% | $110,395 |
| R51 | 80053 | 102 | 13.7% | $4,762 |
| I10 | 93000 | 100 | 16.0% | $5,409 |
| M54.5 | 80053 | 100 | 12.0% | $4,553 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3853 | 77.1% | $9,430,948 | $6,185,592 |
| adjusted | 503 | 10.1% | $1,467,111 | $938,333 |
| denied | 644 | 12.9% | $1,596,778 | $0 |

## Denial reasons

- out-of-network provider (158)
- not medically necessary (157)
- missing prior authorization (156)
- timely filing exceeded (152)
- duplicate claim (21)

## Plan mix

- PPO: 1271
- EPO: 1267
- HDHP: 1235
- HMO: 1227

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1271 | 11.9% | 54.5% |
| EPO | 1267 | 13.6% | 55.3% |
| HDHP | 1235 | 11.8% | 61.8% |
| HMO | 1227 | 14.3% | 55.8% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1052 | 22.4% | 15.8% |
| PPO | 1120 | 23.9% | 15.7% |
| HDHP | 1089 | 21.8% | 14.9% |
| EPO | 1095 | 24.3% | 13.9% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 156 | $488,106 | 30.6% | $3,129 |
| not medically necessary | 157 | $412,220 | 25.8% | $2,626 |
| timely filing exceeded | 152 | $392,481 | 24.6% | $2,582 |
| out-of-network provider | 158 | $246,803 | 15.5% | $1,562 |
| duplicate claim | 21 | $57,168 | 3.6% | $2,722 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 107 (115 later claims)
- Later claims denied as duplicate: 21
- Later claims still paid: 85 ($206,148 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 428 | 23.5% | $394,219 | 5.5% |
| 2 claims | 488 | 26.8% | $1,409,799 | 19.8% |
| 3 claims | 403 | 22.1% | $1,733,912 | 24.3% |
| 4+ claims | 505 | 27.7% | $3,585,996 | 50.3% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1454 | 29.1% | $57,175 | 0.8% | 12.7% |
| $100-$999 | 2325 | 46.5% | $425,089 | 6.0% | 12.7% |
| $1,000-$9,999 | 808 | 16.2% | $792,743 | 11.1% | 13.7% |
| $10,000+ | 413 | 8.3% | $5,848,919 | 82.1% | 12.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,000 | 5,000 | yes |
| claims: plan mix | 5,000 | 5,000 | yes |
| claims: plan performance | 5,000 | 5,000 | yes |
| claims: age bands | 5,000 | 5,000 | yes |
| claims: cost per member | 5,000 | 5,000 | yes |
| paid $: monthly view | 7,123,925.69 | 7,123,925.69 | yes |
| paid $: age bands | 7,123,933.75 | 7,123,925.69 | yes |
| denied claims: reasons | 644 | 644 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1663 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 443 | 1235 | 2.79 | $4,953 |
| PPO | 459 | 1271 | 2.77 | $4,119 |
| EPO | 466 | 1267 | 2.72 | $3,392 |
| HMO | 456 | 1227 | 2.69 | $3,198 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 8 | 4 | 50.0% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0912 | 4 | 3 | 75.0% |
| MBR-0255 | 5 | 3 | 60.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 43239 | 436 | $889,385 | $683,255 | 76.8% |
| 27447 | 361 | $8,944,653 | $6,879,858 | 76.9% |
| 85025 | 434 | $23,129 | $17,877 | 77.3% |
| 99214 | 446 | $74,662 | $57,765 | 77.4% |
| 97110 | 393 | $47,016 | $36,383 | 77.4% |
| 99213 | 455 | $54,924 | $42,511 | 77.4% |

## Paid-amount concentration

Share of total paid (5000 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 50 | 16.7% |
| top 5% | 250 | 64.7% |
| top 10% | 500 | 85.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 158 | 99285 (13%), 93000 (12%), 43239 (11%) |
| not medically necessary | 157 | 43239 (14%), 99285 (13%), 93000 (13%) |
| missing prior authorization | 156 | 99285 (13%), 85025 (12%), 99214 (11%) |

## Data quality gates

9 of 9 checks passed on this run.

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

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 413 | $24,813 | $5,848,919 | 12.6% |
| 43239 | 505 | $2,029 | $575,781 | 13.7% |
| 99285 | 541 | $1,061 | $323,937 | 14.8% |
| 70450 | 498 | $651 | $189,080 | 11.5% |
| 99214 | 508 | $168 | $49,057 | 12.2% |

## Member utilization

908 of 1824 synthetic members have 3+ claims and account for 74.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 11 | $588 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-0154 | 8 | $27,766 |
| MBR-1062 | 8 | $9,989 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 172 | out-of-network provider | 43 |
| HDHP | 146 | missing prior authorization | 41 |
| HMO | 175 | not medically necessary | 45 |
| PPO | 151 | not medically necessary | 42 |

## Month-over-month trend (last 6 complete months)

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +6.4% | -22.7% | +9.49 pp |
| 2026-09 | -44.0% | -38.6% | -10.86 pp |
| 2026-10 | +67.9% | -14.2% | +1.37 pp |

## Potential duplicate services

107 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0743 | 27447 | 2026-11-23 | 2 | $54,807 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-22 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
