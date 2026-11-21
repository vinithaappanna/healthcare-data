# Healthcare Data - claims pipeline report

Generated 2026-11-21 17:21 UTC. All data is synthetic - no real member, patient or plan information.

**3620 claims** in store. Billed $9,113,743, paid $5,309,364, denied 438 overall.

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
| 2026-11 | 3141 | $7,998,464 | $6,174,999 | $4,612,757 | 12.4% |

## Denial reasons

- duplicate claim (98)
- timely filing exceeded (88)
- out-of-network provider (85)
- not medically necessary (85)
- missing prior authorization (83)

## Plan mix

- HMO: 921
- EPO: 907
- HDHP: 903
- PPO: 889

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 921 | 15.0% | 55.4% |
| EPO | 907 | 12.3% | 58.1% |
| HDHP | 903 | 11.1% | 63.1% |
| PPO | 889 | 10.0% | 56.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 783 | 22.0% | 16.4% |
| PPO | 800 | 24.6% | 15.7% |
| HDHP | 803 | 21.5% | 15.5% |
| EPO | 795 | 23.2% | 13.7% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 793 | 15.6% | 12.1% | +3.03 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 88 | $245,623 | 25.0% | $2,791 |
| not medically necessary | 85 | $242,777 | 24.7% | $2,856 |
| duplicate claim | 98 | $174,073 | 17.7% | $1,776 |
| missing prior authorization | 83 | $170,062 | 17.3% | $2,049 |
| out-of-network provider | 85 | $149,866 | 15.3% | $1,763 |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 317 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 416 | 903 | 2.17 | $3,709 |
| PPO | 414 | 889 | 2.15 | $3,438 |
| HMO | 424 | 921 | 2.17 | $2,859 |
| EPO | 428 | 907 | 2.12 | $2,642 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 6 | 3 | 50.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 99214 | 324 | $54,262 | $41,755 | 77.0% |
| 27447 | 270 | $6,711,101 | $5,174,213 | 77.1% |
| 99213 | 328 | $39,371 | $30,432 | 77.3% |
| 43239 | 312 | $637,884 | $493,621 | 77.4% |
| 93000 | 339 | $34,039 | $26,340 | 77.4% |
| 85025 | 310 | $16,560 | $12,828 | 77.5% |

## Paid-amount concentration

Share of total paid (3620 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 37 | 16.5% |
| top 5% | 181 | 63.4% |
| top 10% | 362 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 98 | 99285 (19%), 93000 (14%), 85025 (12%) |
| timely filing exceeded | 88 | 93000 (12%), 85025 (11%), 99214 (11%) |
| not medically necessary | 85 | 43239 (15%), 93000 (15%), 85025 (13%) |

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
| 27447 | 301 | $24,833 | $4,380,718 | 10.3% |
| 43239 | 364 | $2,042 | $415,027 | 14.3% |
| 99285 | 399 | $1,066 | $238,760 | 14.8% |
| 70450 | 363 | $653 | $139,583 | 11.0% |
| 99214 | 373 | $168 | $35,428 | 13.1% |

## Member utilization

551 of 1682 synthetic members have 3+ claims and account for 60.6% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 7 | $49,745 |
| MBR-0693 | 6 | $30,518 |
| MBR-0154 | 6 | $27,628 |
| MBR-0298 | 6 | $22,374 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 112 | out-of-network provider | 25 |
| HDHP | 100 | duplicate claim | 27 |
| HMO | 138 | duplicate claim | 32 |
| PPO | 89 | duplicate claim | 22 |

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

54 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |
| MBR-1695 | 27447 | 2026-11-18 | 2 | $25,258 |
| MBR-1025 | 27447 | 2026-11-17 | 2 | $23,763 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
