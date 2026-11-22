# Healthcare Data - claims pipeline report

Generated 2026-11-22 08:20 UTC. All data is synthetic - no real member, patient or plan information.

**4040 claims** in store. Billed $10,112,054, paid $5,804,243, denied 497 overall.

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
| 2026-11 | 3561 | $8,996,775 | $6,931,287 | $5,107,635 | 12.6% |

## Denial reasons

- duplicate claim (114)
- timely filing exceeded (100)
- missing prior authorization (98)
- out-of-network provider (94)
- not medically necessary (92)

## Plan mix

- EPO: 1021
- PPO: 1009
- HDHP: 1006
- HMO: 1004

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1021 | 12.4% | 56.8% |
| PPO | 1009 | 10.6% | 54.7% |
| HDHP | 1006 | 11.4% | 62.0% |
| HMO | 1004 | 14.8% | 55.6% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 855 | 22.0% | 16.4% |
| PPO | 902 | 24.5% | 16.2% |
| HDHP | 891 | 21.4% | 15.3% |
| EPO | 894 | 23.8% | 13.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 876 | 15.4% | 12.3% | +2.78 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 100 | $274,827 | 22.8% | $2,748 |
| not medically necessary | 92 | $268,609 | 22.3% | $2,920 |
| missing prior authorization | 98 | $258,128 | 21.4% | $2,634 |
| duplicate claim | 114 | $251,219 | 20.8% | $2,204 |
| out-of-network provider | 94 | $153,798 | 12.8% | $1,636 |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1195 | 29.6% | $47,408 | 0.8% | 12.2% |
| $100-$999 | 1862 | 46.1% | $344,531 | 5.9% | 12.0% |
| $1,000-$9,999 | 648 | 16.0% | $631,928 | 10.9% | 13.9% |
| $10,000+ | 335 | 8.3% | $4,780,376 | 82.4% | 11.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,040 | 4,040 | yes |
| claims: plan mix | 4,040 | 4,040 | yes |
| claims: plan performance | 4,040 | 4,040 | yes |
| claims: age bands | 4,040 | 4,040 | yes |
| claims: cost per member | 4,040 | 4,040 | yes |
| paid $: monthly view | 5,804,242.93 | 5,804,242.93 | yes |
| paid $: age bands | 5,804,244.05 | 5,804,242.93 | yes |
| denied claims: reasons | 498 | 498 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 737 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 429 | 1006 | 2.34 | $4,034 |
| PPO | 433 | 1009 | 2.33 | $3,541 |
| HMO | 432 | 1004 | 2.32 | $2,918 |
| EPO | 442 | 1021 | 2.31 | $2,896 |

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
| 27447 | 296 | $7,340,842 | $5,653,696 | 77.0% |
| 99214 | 355 | $59,351 | $45,765 | 77.1% |
| 43239 | 342 | $695,838 | $537,664 | 77.3% |
| 93000 | 383 | $38,385 | $29,703 | 77.4% |
| 99213 | 369 | $44,333 | $34,315 | 77.4% |
| 97110 | 310 | $37,010 | $28,689 | 77.5% |

## Paid-amount concentration

Share of total paid (4040 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 41 | 16.7% |
| top 5% | 202 | 64.2% |
| top 10% | 404 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 114 | 99285 (18%), 93000 (16%), 85025 (12%) |
| timely filing exceeded | 100 | 93000 (13%), 80053 (11%), 99213 (11%) |
| missing prior authorization | 98 | 99214 (15%), 99285 (13%), 85025 (12%) |

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
| 27447 | 335 | $24,799 | $4,780,376 | 11.6% |
| 43239 | 397 | $2,034 | $453,084 | 13.9% |
| 99285 | 446 | $1,064 | $267,244 | 15.0% |
| 70450 | 401 | $654 | $152,548 | 11.7% |
| 99214 | 405 | $167 | $38,819 | 12.3% |

## Member utilization

657 of 1736 synthetic members have 3+ claims and account for 66.5% of paid dollars.

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
| EPO | 127 | out-of-network provider | 29 |
| HDHP | 115 | duplicate claim | 31 |
| HMO | 149 | duplicate claim | 36 |
| PPO | 107 | duplicate claim | 26 |

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
