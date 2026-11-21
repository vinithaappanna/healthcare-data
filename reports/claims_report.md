# Healthcare Data - claims pipeline report

Generated 2026-11-21 12:18 UTC. All data is synthetic - no real member, patient or plan information.

**3380 claims** in store. Billed $10,340,908, paid $6,071,093, denied 410 overall.

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
| 2026-11 | 2901 | $9,070,945 | $7,017,741 | $5,279,643 | 12.4% |

## Denial reasons

- duplicate claim (89)
- timely filing exceeded (85)
- out-of-network provider (81)
- missing prior authorization (80)
- not medically necessary (76)

## Plan mix

- HMO: 897
- PPO: 851
- HDHP: 840
- EPO: 792

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 897 | 11.0% | 60.9% |
| PPO | 851 | 11.8% | 58.6% |
| HDHP | 840 | 11.8% | 59.6% |
| EPO | 792 | 14.3% | 55.6% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 751 | 22.4% | 15.4% |
| EPO | 679 | 23.7% | 15.3% |
| HMO | 798 | 22.0% | 15.0% |
| HDHP | 741 | 22.1% | 14.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| EPO | 2026-11 | 672 | 14.7% | 12.2% | +2.04 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 85 | $326,191 | 29.4% | $3,838 |
| not medically necessary | 76 | $239,797 | 21.6% | $3,155 |
| missing prior authorization | 80 | $200,638 | 18.1% | $2,508 |
| duplicate claim | 89 | $176,807 | 16.0% | $1,987 |
| out-of-network provider | 81 | $164,078 | 14.8% | $2,026 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HMO | 718 | 897 | 1.25 | $2,406 |
| PPO | 685 | 851 | 1.24 | $2,242 |
| EPO | 663 | 792 | 1.19 | $2,154 |
| HDHP | 677 | 840 | 1.24 | $2,037 |

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
| 99214 | 291 | $48,508 | $37,284 | 76.9% |
| 99213 | 307 | $36,901 | $28,464 | 77.1% |
| 43239 | 286 | $585,370 | $452,096 | 77.2% |
| 27447 | 319 | $7,931,511 | $6,144,701 | 77.5% |
| 99285 | 313 | $338,238 | $262,397 | 77.6% |
| 85025 | 283 | $15,197 | $11,791 | 77.6% |

## Paid-amount concentration

Share of total paid (3380 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 34 | 13.7% |
| top 5% | 169 | 55.2% |
| top 10% | 338 | 86.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 89 | 99285 (20%), 93000 (15%), 70450 (10%) |
| timely filing exceeded | 85 | 27447 (14%), 93000 (12%), 99214 (12%) |
| out-of-network provider | 81 | 70450 (14%), 99285 (14%), 43239 (12%) |

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
| 27447 | 355 | $24,892 | $5,222,320 | 10.1% |
| 43239 | 335 | $2,040 | $379,549 | 14.6% |
| 99285 | 366 | $1,074 | $221,215 | 14.5% |
| 70450 | 329 | $655 | $125,030 | 11.8% |
| 99214 | 337 | $167 | $31,517 | 13.7% |

## Member utilization

487 of 1626 synthetic members have 3+ claims and account for 53.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 6 | $35,318 |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-0154 | 6 | $27,628 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 113 | duplicate claim | 29 |
| HDHP | 99 | timely filing exceeded | 24 |
| HMO | 99 | timely filing exceeded | 21 |
| PPO | 100 | timely filing exceeded | 24 |

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

49 groups share a member, procedure and service date (review queue, not a quality failure).

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
