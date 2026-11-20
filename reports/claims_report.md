# Healthcare Data - claims pipeline report

Generated 2026-11-20 21:16 UTC. All data is synthetic - no real member, patient or plan information.

**3020 claims** in store. Billed $9,409,018, paid $5,511,564, denied 350 overall.

## Monthly financials

| Month | Claims | Billed | Allowed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2025-11 | 18 | $5,840 | $4,755 | $4,019 | 11.1% |
| 2025-12 | 44 | $45,779 | $36,033 | $31,423 | 9.1% |
| 2026-01 | 31 | $69,438 | $54,037 | $43,702 | 0.0% |
| 2026-02 | 32 | $106,824 | $80,818 | $51,105 | 12.5% |
| 2026-03 | 45 | $161,580 | $117,994 | $103,125 | 11.1% |
| 2026-04 | 48 | $109,782 | $90,132 | $76,083 | 8.3% |
| 2026-05 | 43 | $161,609 | $121,321 | $113,180 | 11.6% |
| 2026-06 | 46 | $209,778 | $171,530 | $122,054 | 15.2% |
| 2026-07 | 47 | $143,413 | $117,048 | $95,614 | 8.5% |
| 2026-08 | 50 | $87,251 | $70,911 | $55,220 | 18.0% |
| 2026-09 | 28 | $97,162 | $80,729 | $53,482 | 7.1% |
| 2026-10 | 47 | $71,505 | $55,063 | $42,442 | 8.5% |
| 2026-11 | 2541 | $8,139,056 | $6,285,380 | $4,720,115 | 11.8% |

## Denial reasons

- duplicate claim (77)
- timely filing exceeded (72)
- out-of-network provider (71)
- missing prior authorization (68)
- not medically necessary (62)

## Plan mix

- HMO: 804
- PPO: 756
- HDHP: 751
- EPO: 709

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 804 | 10.6% | 61.1% |
| PPO | 756 | 11.2% | 57.7% |
| HDHP | 751 | 10.7% | 59.7% |
| EPO | 709 | 14.1% | 55.7% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| EPO | 609 | 23.6% | 15.7% |
| PPO | 671 | 22.9% | 15.5% |
| HDHP | 671 | 22.3% | 15.1% |
| HMO | 719 | 22.1% | 14.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| EPO | 2026-11 | 589 | 14.6% | 11.6% | +2.28 |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 99214 | 258 | $43,062 | $33,143 | 77.0% |
| 99213 | 269 | $32,269 | $24,859 | 77.0% |
| 43239 | 263 | $538,987 | $415,453 | 77.1% |
| 27447 | 292 | $7,246,953 | $5,597,493 | 77.2% |
| 85025 | 255 | $13,641 | $10,565 | 77.5% |
| 93000 | 266 | $26,738 | $20,736 | 77.5% |

## Paid-amount concentration

Share of total paid (3020 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 31 | 13.7% |
| top 5% | 151 | 54.3% |
| top 10% | 302 | 86.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 77 | 99285 (22%), 93000 (13%), 85025 (10%) |
| timely filing exceeded | 72 | 27447 (15%), 85025 (12%), 93000 (11%) |
| out-of-network provider | 71 | 70450 (15%), 99285 (14%), 43239 (13%) |

## Data quality gates

6 of 6 checks passed on this run.

| Check | Issues | Result |
| --- | ---: | --- |
| amount consistency | 0 | pass |
| denial reasons | 0 | pass |
| one member per claim | 0 | pass |
| billed within procedure range | 0 | pass |
| known diagnosis codes | 0 | pass |
| service dates | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 324 | $24,895 | $4,749,106 | 9.9% |
| 43239 | 304 | $2,039 | $348,818 | 13.5% |
| 99285 | 314 | $1,072 | $188,544 | 15.0% |
| 70450 | 303 | $654 | $115,260 | 11.6% |
| 99214 | 298 | $167 | $28,078 | 13.4% |

## Member utilization

399 of 1549 synthetic members have 3+ claims and account for 44.8% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-0746 | 6 | $11,961 |
| MBR-1062 | 6 | $9,989 |
| MBR-0961 | 6 | $2,171 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 100 | missing prior authorization | 28 |
| HDHP | 80 | out-of-network provider | 21 |
| HMO | 85 | duplicate claim | 19 |
| PPO | 85 | timely filing exceeded | 23 |

## Month-over-month trend (last 6 complete months)

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -21.7% | -6.71 pp |
| 2026-08 | +6.4% | -42.2% | +9.49 pp |
| 2026-09 | -44.0% | -3.1% | -10.86 pp |
| 2026-10 | +67.9% | -20.6% | +1.37 pp |

## Potential duplicate services

41 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-1695 | 27447 | 2026-11-18 | 2 | $25,258 |
| MBR-1025 | 27447 | 2026-11-17 | 2 | $23,763 |
| MBR-1697 | 43239 | 2026-11-17 | 2 | $2,808 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
