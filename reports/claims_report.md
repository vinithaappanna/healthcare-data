# Healthcare Data - claims pipeline report

Generated 2026-11-20 06:14 UTC. All data is synthetic - no real member, patient or plan information.

**2600 claims** in store. Billed $8,247,347, paid $4,791,445, denied 299 overall.

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
| 2026-11 | 2121 | $6,977,385 | $5,403,944 | $3,999,995 | 11.7% |

## Denial reasons

- duplicate claim (67)
- out-of-network provider (59)
- missing prior authorization (58)
- not medically necessary (58)
- timely filing exceeded (57)

## Plan mix

- HMO: 687
- PPO: 668
- HDHP: 629
- EPO: 616

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 687 | 9.6% | 60.9% |
| PPO | 668 | 12.0% | 56.9% |
| HDHP | 629 | 10.0% | 59.3% |
| EPO | 616 | 14.6% | 55.1% |

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 588 | 22.5% | 15.7% |
| HDHP | 566 | 22.6% | 15.6% |
| EPO | 526 | 23.6% | 15.2% |
| HMO | 621 | 21.7% | 15.2% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| EPO | 2026-11 | 496 | 15.3% | 11.5% | +2.67 |

## Paid-amount concentration

Share of total paid (2600 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 26 | 13.2% |
| top 5% | 130 | 54.2% |
| top 10% | 260 | 86.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 67 | 99285 (21%), 93000 (13%), 43239 (10%) |
| out-of-network provider | 59 | 99285 (15%), 43239 (14%), 70450 (12%) |
| missing prior authorization | 58 | 99214 (19%), 85025 (12%), 99285 (12%) |

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
| 27447 | 285 | $24,884 | $4,135,143 | 10.9% |
| 43239 | 267 | $2,044 | $308,626 | 13.1% |
| 99285 | 260 | $1,066 | $152,519 | 15.8% |
| 70450 | 263 | $655 | $101,133 | 10.3% |
| 99214 | 254 | $166 | $23,930 | 13.4% |

## Member utilization

291 of 1442 synthetic members have 3+ claims and account for 38.0% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-1062 | 6 | $9,989 |
| MBR-0136 | 6 | $1,569 |
| MBR-0849 | 6 | $763 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 90 | missing prior authorization | 24 |
| HDHP | 63 | out-of-network provider | 17 |
| HMO | 66 | duplicate claim | 15 |
| PPO | 80 | timely filing exceeded | 23 |

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

32 groups share a member, procedure and service date (review queue, not a quality failure).

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
