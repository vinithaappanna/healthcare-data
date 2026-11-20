# Healthcare Data - claims pipeline report

Generated 2026-11-20 11:15 UTC. All data is synthetic - no real member, patient or plan information.

**2720 claims** in store. Billed $8,454,380, paid $4,920,419, denied 313 overall.

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
| 2026-11 | 2241 | $7,184,417 | $5,557,147 | $4,128,969 | 11.8% |

## Denial reasons

- duplicate claim (69)
- missing prior authorization (64)
- out-of-network provider (62)
- timely filing exceeded (60)
- not medically necessary (59)

## Plan mix

- HMO: 723
- PPO: 694
- HDHP: 663
- EPO: 640

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 723 | 9.7% | 60.9% |
| PPO | 694 | 11.8% | 57.0% |
| HDHP | 663 | 10.3% | 59.9% |
| EPO | 640 | 14.7% | 55.1% |

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 612 | 22.6% | 15.8% |
| EPO | 546 | 23.7% | 15.3% |
| HMO | 653 | 21.7% | 15.2% |
| HDHP | 595 | 22.7% | 15.0% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| EPO | 2026-11 | 520 | 15.4% | 11.5% | +2.74 |

## Paid-amount concentration

Share of total paid (2720 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 28 | 13.8% |
| top 5% | 136 | 54.9% |
| top 10% | 272 | 86.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 69 | 99285 (20%), 93000 (13%), 85025 (12%) |
| missing prior authorization | 64 | 99214 (20%), 85025 (12%), 43239 (11%) |
| out-of-network provider | 62 | 70450 (15%), 99285 (15%), 43239 (13%) |

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
| 27447 | 291 | $24,899 | $4,233,412 | 10.7% |
| 43239 | 278 | $2,048 | $321,620 | 13.3% |
| 99285 | 268 | $1,070 | $158,381 | 15.3% |
| 70450 | 281 | $653 | $107,783 | 10.7% |
| 99214 | 272 | $167 | $25,672 | 13.6% |

## Member utilization

327 of 1473 synthetic members have 3+ claims and account for 41.5% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-0746 | 6 | $11,961 |
| MBR-1062 | 6 | $9,989 |
| MBR-0136 | 6 | $1,569 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 94 | missing prior authorization | 27 |
| HDHP | 68 | out-of-network provider | 18 |
| HMO | 70 | duplicate claim | 16 |
| PPO | 82 | timely filing exceeded | 23 |

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

33 groups share a member, procedure and service date (review queue, not a quality failure).

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
