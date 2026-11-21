# Healthcare Data - claims pipeline report

Generated 2026-11-21 17:19 UTC. All data is synthetic - no real member, patient or plan information.

**3500 claims** in store. Billed $10,719,414, paid $6,304,339, denied 417 overall.

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
| 2026-11 | 3021 | $9,449,452 | $7,312,577 | $5,512,889 | 12.2% |

## Denial reasons

- duplicate claim (90)
- timely filing exceeded (86)
- missing prior authorization (81)
- out-of-network provider (81)
- not medically necessary (80)

## Plan mix

- HMO: 889
- EPO: 878
- HDHP: 868
- PPO: 865

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 889 | 14.6% | 55.6% |
| EPO | 878 | 12.1% | 58.2% |
| HDHP | 868 | 10.7% | 64.1% |
| PPO | 865 | 10.3% | 56.9% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 759 | 21.7% | 16.0% |
| PPO | 776 | 24.8% | 15.6% |
| HDHP | 775 | 20.9% | 14.7% |
| EPO | 772 | 22.9% | 13.7% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 761 | 15.2% | 11.9% | +2.81 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 86 | $326,940 | 28.6% | $3,802 |
| not medically necessary | 80 | $241,339 | 21.1% | $3,017 |
| duplicate claim | 90 | $210,403 | 18.4% | $2,338 |
| missing prior authorization | 81 | $200,753 | 17.6% | $2,478 |
| out-of-network provider | 81 | $164,078 | 14.3% | $2,026 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 410 | 868 | 2.12 | $4,486 |
| PPO | 408 | 865 | 2.12 | $3,919 |
| HMO | 415 | 889 | 2.14 | $3,551 |
| EPO | 421 | 878 | 2.09 | $3,308 |

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
| 99214 | 298 | $49,592 | $38,205 | 77.0% |
| 99213 | 316 | $37,970 | $29,328 | 77.2% |
| 43239 | 295 | $602,856 | $465,730 | 77.2% |
| 93000 | 321 | $32,328 | $25,034 | 77.4% |
| 27447 | 331 | $8,230,433 | $6,374,687 | 77.5% |
| 85025 | 292 | $15,662 | $12,142 | 77.5% |

## Paid-amount concentration

Share of total paid (3500 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 35 | 13.6% |
| top 5% | 175 | 55.2% |
| top 10% | 350 | 86.8% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 90 | 99285 (20%), 93000 (14%), 70450 (10%) |
| timely filing exceeded | 86 | 27447 (14%), 93000 (12%), 99214 (12%) |
| missing prior authorization | 81 | 99214 (17%), 43239 (14%), 99285 (12%) |

## Data quality gates

7 of 7 checks passed on this run.

| Check | Issues | Result |
| --- | ---: | --- |
| amount consistency | 0 | pass |
| denial reasons | 0 | pass |
| one member per claim | 0 | pass |
| billed within procedure range | 0 | pass |
| known diagnosis codes | 0 | pass |
| service dates | 0 | pass |
| member consistency | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 368 | $24,916 | $5,427,426 | 10.1% |
| 43239 | 344 | $2,037 | $390,697 | 14.2% |
| 99285 | 377 | $1,072 | $227,010 | 14.6% |
| 70450 | 345 | $654 | $131,660 | 11.3% |
| 99214 | 345 | $167 | $32,350 | 13.6% |

## Member utilization

523 of 1654 synthetic members have 3+ claims and account for 57.0% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 7 | $49,745 |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-0154 | 6 | $27,628 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 106 | out-of-network provider | 24 |
| HDHP | 93 | duplicate claim | 23 |
| HMO | 130 | duplicate claim | 29 |
| PPO | 89 | duplicate claim | 22 |

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

50 groups share a member, procedure and service date (review queue, not a quality failure).

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
