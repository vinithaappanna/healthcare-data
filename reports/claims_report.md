# Healthcare Data - claims pipeline report

Generated 2026-11-22 23:23 UTC. All data is synthetic - no real member, patient or plan information.

**4520 claims** in store. Billed $11,251,005, paid $6,427,611, denied 564 overall.

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
| 2026-11 | 4041 | $10,135,726 | $7,781,331 | $5,731,003 | 12.7% |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3499 | 77.4% | $8,513,097 | $5,572,992 |
| adjusted | 456 | 10.1% | $1,342,501 | $854,619 |
| denied | 565 | 12.5% | $1,395,407 | $0 |

## Denial reasons

- timely filing exceeded (143)
- out-of-network provider (141)
- missing prior authorization (138)
- not medically necessary (136)
- duplicate claim (7)

## Plan mix

- PPO: 1153
- EPO: 1142
- HDHP: 1114
- HMO: 1111

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1153 | 11.4% | 54.5% |
| EPO | 1142 | 12.7% | 56.9% |
| HDHP | 1114 | 11.4% | 61.6% |
| HMO | 1111 | 14.6% | 55.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 949 | 22.3% | 16.2% |
| PPO | 1022 | 24.3% | 16.0% |
| HDHP | 987 | 21.9% | 15.2% |
| EPO | 997 | 23.8% | 13.4% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 983 | 15.1% | 12.5% | +2.42 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 138 | $429,980 | 30.8% | $3,116 |
| timely filing exceeded | 143 | $388,923 | 27.9% | $2,720 |
| not medically necessary | 136 | $331,963 | 23.8% | $2,441 |
| out-of-network provider | 141 | $241,874 | 17.3% | $1,715 |
| duplicate claim | 7 | $2,666 | 0.2% | $381 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 81 (85 later claims)
- Later claims denied as duplicate: 7
- Later claims still paid: 69 ($153,484 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 482 | 27.0% | $438,629 | 6.8% |
| 2 claims | 521 | 29.2% | $1,432,763 | 22.3% |
| 3 claims | 373 | 20.9% | $1,752,784 | 27.3% |
| 4+ claims | 408 | 22.9% | $2,803,435 | 43.6% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1318 | 29.2% | $52,114 | 0.8% | 12.1% |
| $100-$999 | 2089 | 46.2% | $385,476 | 6.0% | 12.3% |
| $1,000-$9,999 | 741 | 16.4% | $723,199 | 11.2% | 13.9% |
| $10,000+ | 372 | 8.2% | $5,266,822 | 81.9% | 12.1% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,520 | 4,520 | yes |
| claims: plan mix | 4,520 | 4,520 | yes |
| claims: plan performance | 4,520 | 4,520 | yes |
| claims: age bands | 4,520 | 4,520 | yes |
| claims: cost per member | 4,520 | 4,520 | yes |
| paid $: monthly view | 6,427,610.72 | 6,427,610.72 | yes |
| paid $: age bands | 6,427,609.03 | 6,427,610.72 | yes |
| denied claims: reasons | 565 | 565 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1183 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 436 | 1114 | 2.56 | $4,431 |
| PPO | 447 | 1153 | 2.58 | $3,984 |
| EPO | 456 | 1142 | 2.50 | $3,015 |
| HMO | 445 | 1111 | 2.50 | $3,012 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 7 | 4 | 57.1% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0255 | 4 | 3 | 75.0% |
| MBR-0912 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 327 | $8,079,488 | $6,212,369 | 76.9% |
| 99214 | 400 | $67,031 | $51,646 | 77.0% |
| 43239 | 399 | $806,640 | $622,317 | 77.1% |
| 85025 | 393 | $21,039 | $16,250 | 77.2% |
| 99213 | 410 | $49,450 | $38,306 | 77.5% |
| 93000 | 419 | $41,823 | $32,402 | 77.5% |

## Paid-amount concentration

Share of total paid (4520 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 46 | 16.9% |
| top 5% | 226 | 64.4% |
| top 10% | 452 | 85.4% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| timely filing exceeded | 143 | 85025 (12%), 93000 (12%), 99285 (11%) |
| out-of-network provider | 141 | 99285 (15%), 43239 (12%), 70450 (12%) |
| missing prior authorization | 138 | 99285 (13%), 85025 (12%), 99214 (12%) |

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
| 27447 | 372 | $24,749 | $5,266,822 | 12.1% |
| 43239 | 463 | $2,013 | $524,459 | 13.8% |
| 99285 | 494 | $1,063 | $296,210 | 15.0% |
| 70450 | 452 | $656 | $172,153 | 11.5% |
| 99214 | 455 | $168 | $43,801 | 12.1% |

## Member utilization

781 of 1784 synthetic members have 3+ claims and account for 70.9% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-0124 | 9 | $16,460 |
| MBR-1200 | 9 | $542 |
| MBR-0136 | 8 | $3,545 |
| MBR-1595 | 8 | $2,560 |
| MBR-1219 | 7 | $49,745 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 145 | out-of-network provider | 37 |
| HDHP | 127 | missing prior authorization | 38 |
| HMO | 162 | not medically necessary | 41 |
| PPO | 131 | not medically necessary | 36 |

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

81 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |
| MBR-1175 | 27447 | 2026-11-22 | 2 | $28,226 |
| MBR-1257 | 27447 | 2026-11-21 | 2 | $27,445 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
