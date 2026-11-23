# Healthcare Data - claims pipeline report

Generated 2026-11-23 04:24 UTC. All data is synthetic - no real member, patient or plan information.

**4700 claims** in store. Billed $11,723,293, paid $6,666,739, denied 594 overall.

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
| 2026-11 | 4221 | $10,608,015 | $8,114,006 | $5,970,131 | 12.9% |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3632 | 77.3% | $8,837,569 | $5,790,820 |
| adjusted | 474 | 10.1% | $1,376,812 | $875,919 |
| denied | 594 | 12.6% | $1,508,912 | $0 |

## Denial reasons

- out-of-network provider (149)
- timely filing exceeded (146)
- missing prior authorization (145)
- not medically necessary (144)
- duplicate claim (10)

## Plan mix

- PPO: 1204
- EPO: 1193
- HDHP: 1154
- HMO: 1149

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1204 | 11.5% | 53.7% |
| EPO | 1193 | 13.1% | 56.4% |
| HDHP | 1154 | 11.5% | 61.4% |
| HMO | 1149 | 14.4% | 55.5% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 983 | 22.3% | 16.0% |
| PPO | 1065 | 24.3% | 16.0% |
| HDHP | 1021 | 21.8% | 15.0% |
| EPO | 1037 | 24.0% | 13.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 1021 | 14.9% | 12.6% | +2.16 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 145 | $456,741 | 30.3% | $3,150 |
| timely filing exceeded | 146 | $390,814 | 25.9% | $2,677 |
| not medically necessary | 144 | $387,174 | 25.7% | $2,689 |
| out-of-network provider | 149 | $242,863 | 16.1% | $1,630 |
| duplicate claim | 10 | $31,321 | 2.1% | $3,132 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 91 (97 later claims)
- Later claims denied as duplicate: 10
- Later claims still paid: 78 ($175,362 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 460 | 25.6% | $405,646 | 6.1% |
| 2 claims | 507 | 28.2% | $1,442,615 | 21.6% |
| 3 claims | 393 | 21.9% | $1,804,254 | 27.1% |
| 4+ claims | 439 | 24.4% | $3,014,224 | 45.2% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1366 | 29.1% | $53,826 | 0.8% | 12.4% |
| $100-$999 | 2178 | 46.3% | $402,138 | 6.0% | 12.3% |
| $1,000-$9,999 | 768 | 16.3% | $751,197 | 11.3% | 13.9% |
| $10,000+ | 388 | 8.3% | $5,459,579 | 81.9% | 12.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,700 | 4,700 | yes |
| claims: plan mix | 4,700 | 4,700 | yes |
| claims: plan performance | 4,700 | 4,700 | yes |
| claims: age bands | 4,700 | 4,700 | yes |
| claims: cost per member | 4,700 | 4,700 | yes |
| paid $: monthly view | 6,666,738.98 | 6,666,738.98 | yes |
| paid $: age bands | 6,666,738.9 | 6,666,738.98 | yes |
| denied claims: reasons | 594 | 594 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1363 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 438 | 1154 | 2.63 | $4,655 |
| PPO | 450 | 1204 | 2.68 | $3,986 |
| EPO | 462 | 1193 | 2.58 | $3,136 |
| HMO | 449 | 1149 | 2.56 | $3,085 |

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
| 27447 | 339 | $8,368,841 | $6,431,739 | 76.8% |
| 43239 | 413 | $837,221 | $645,780 | 77.1% |
| 85025 | 411 | $22,038 | $17,018 | 77.2% |
| 99214 | 421 | $70,546 | $54,598 | 77.4% |
| 99213 | 427 | $51,479 | $39,846 | 77.4% |
| 93000 | 430 | $42,949 | $33,270 | 77.5% |

## Paid-amount concentration

Share of total paid (4700 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 47 | 16.6% |
| top 5% | 235 | 64.5% |
| top 10% | 470 | 85.5% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 149 | 99285 (14%), 93000 (12%), 43239 (11%) |
| timely filing exceeded | 146 | 93000 (13%), 85025 (12%), 99285 (11%) |
| missing prior authorization | 145 | 85025 (12%), 99285 (12%), 99214 (12%) |

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
| 27447 | 388 | $24,745 | $5,459,579 | 12.6% |
| 43239 | 480 | $2,015 | $545,210 | 14.0% |
| 99285 | 514 | $1,060 | $308,432 | 14.6% |
| 70450 | 470 | $653 | $178,845 | 11.3% |
| 99214 | 478 | $168 | $46,339 | 11.9% |

## Member utilization

832 of 1799 synthetic members have 3+ claims and account for 72.3% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 11 | $588 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-1595 | 8 | $2,560 |
| MBR-0979 | 8 | $381 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 156 | out-of-network provider | 40 |
| HDHP | 133 | missing prior authorization | 38 |
| HMO | 166 | not medically necessary | 43 |
| PPO | 139 | not medically necessary | 39 |

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

91 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-22 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |
| MBR-1175 | 27447 | 2026-11-22 | 2 | $28,226 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
