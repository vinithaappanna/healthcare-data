# Healthcare Data - claims pipeline report

Generated 2026-11-22 03:20 UTC. All data is synthetic - no real member, patient or plan information.

**3920 claims** in store. Billed $9,883,105, paid $5,684,634, denied 478 overall.

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
| 2026-11 | 3441 | $8,767,826 | $6,755,966 | $4,988,027 | 12.4% |

## Denial reasons

- duplicate claim (108)
- timely filing exceeded (96)
- missing prior authorization (94)
- out-of-network provider (91)
- not medically necessary (89)

## Plan mix

- EPO: 986
- HMO: 983
- PPO: 977
- HDHP: 974

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 986 | 12.5% | 56.7% |
| HMO | 983 | 14.5% | 55.6% |
| PPO | 977 | 10.4% | 54.8% |
| HDHP | 974 | 11.3% | 62.5% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 840 | 22.0% | 16.4% |
| PPO | 875 | 24.4% | 16.2% |
| HDHP | 864 | 21.5% | 15.2% |
| EPO | 863 | 23.6% | 13.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 855 | 15.1% | 12.2% | +2.59 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 96 | $273,714 | 23.3% | $2,851 |
| not medically necessary | 89 | $268,287 | 22.9% | $3,014 |
| missing prior authorization | 94 | $257,232 | 21.9% | $2,737 |
| duplicate claim | 108 | $220,043 | 18.8% | $2,037 |
| out-of-network provider | 91 | $153,449 | 13.1% | $1,686 |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1155 | 29.5% | $45,968 | 0.8% | 12.1% |
| $100-$999 | 1803 | 46.0% | $334,921 | 5.9% | 11.7% |
| $1,000-$9,999 | 634 | 16.2% | $615,629 | 10.8% | 14.2% |
| $10,000+ | 328 | 8.4% | $4,688,116 | 82.5% | 11.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 3,920 | 3,920 | yes |
| claims: plan mix | 3,920 | 3,920 | yes |
| claims: plan performance | 3,920 | 3,920 | yes |
| claims: age bands | 3,920 | 3,920 | yes |
| claims: cost per member | 3,920 | 3,920 | yes |
| paid $: monthly view | 5,684,634.5 | 5,684,634.5 | yes |
| paid $: age bands | 5,684,627.34 | 5,684,634.5 | yes |
| denied claims: reasons | 478 | 478 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 617 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 427 | 974 | 2.28 | $3,962 |
| PPO | 424 | 977 | 2.30 | $3,577 |
| HMO | 430 | 983 | 2.29 | $2,914 |
| EPO | 437 | 986 | 2.26 | $2,800 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 7 | 4 | 57.1% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 99214 | 341 | $57,104 | $43,955 | 77.0% |
| 27447 | 290 | $7,185,963 | $5,539,205 | 77.1% |
| 43239 | 336 | $682,295 | $527,241 | 77.3% |
| 99213 | 356 | $42,845 | $33,131 | 77.3% |
| 93000 | 371 | $37,271 | $28,836 | 77.4% |
| 99285 | 367 | $392,952 | $304,543 | 77.5% |

## Paid-amount concentration

Share of total paid (3920 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 40 | 16.6% |
| top 5% | 196 | 63.8% |
| top 10% | 392 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 108 | 99285 (19%), 93000 (17%), 85025 (11%) |
| timely filing exceeded | 96 | 93000 (12%), 99213 (11%), 27447 (10%) |
| missing prior authorization | 94 | 99214 (16%), 99285 (13%), 43239 (12%) |

## Data quality gates

8 of 8 checks passed on this run.

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

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 328 | $24,766 | $4,688,116 | 11.6% |
| 43239 | 391 | $2,031 | $443,862 | 14.1% |
| 99285 | 431 | $1,065 | $257,694 | 14.8% |
| 70450 | 390 | $654 | $148,408 | 11.8% |
| 99214 | 391 | $168 | $37,320 | 12.8% |

## Member utilization

628 of 1718 synthetic members have 3+ claims and account for 64.2% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 7 | $49,745 |
| MBR-0856 | 7 | $18,174 |
| MBR-1062 | 7 | $9,989 |
| MBR-0961 | 7 | $2,171 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 123 | out-of-network provider | 28 |
| HDHP | 110 | duplicate claim | 29 |
| HMO | 143 | duplicate claim | 35 |
| PPO | 102 | duplicate claim | 25 |

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

65 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |
| MBR-1257 | 27447 | 2026-11-21 | 2 | $27,445 |
| MBR-1695 | 27447 | 2026-11-18 | 2 | $25,258 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
