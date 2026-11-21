# Healthcare Data - claims pipeline report

Generated 2026-11-21 02:16 UTC. All data is synthetic - no real member, patient or plan information.

**3140 claims** in store. Billed $9,817,211, paid $5,780,255, denied 367 overall.

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
| 2026-11 | 2661 | $8,547,249 | $6,612,008 | $4,988,805 | 11.9% |

## Denial reasons

- duplicate claim (80)
- timely filing exceeded (78)
- out-of-network provider (75)
- missing prior authorization (70)
- not medically necessary (65)

## Plan mix

- HMO: 838
- PPO: 787
- HDHP: 778
- EPO: 737

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 838 | 10.7% | 61.1% |
| PPO | 787 | 11.3% | 58.2% |
| HDHP | 778 | 10.9% | 60.3% |
| EPO | 737 | 14.1% | 55.9% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| EPO | 633 | 23.5% | 15.5% |
| PPO | 698 | 22.7% | 15.2% |
| HDHP | 693 | 22.1% | 15.0% |
| HMO | 748 | 22.1% | 14.9% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| EPO | 2026-11 | 617 | 14.6% | 11.7% | +2.21 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 78 | $299,809 | 29.5% | $3,844 |
| not medically necessary | 65 | $206,758 | 20.4% | $3,181 |
| missing prior authorization | 70 | $188,702 | 18.6% | $2,696 |
| duplicate claim | 80 | $173,888 | 17.1% | $2,174 |
| out-of-network provider | 75 | $146,467 | 14.4% | $1,953 |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 99214 | 268 | $44,746 | $34,358 | 76.8% |
| 99213 | 280 | $33,644 | $25,884 | 76.9% |
| 43239 | 270 | $555,656 | $429,605 | 77.3% |
| 27447 | 305 | $7,587,589 | $5,871,115 | 77.4% |
| 93000 | 274 | $27,643 | $21,408 | 77.5% |
| 99285 | 281 | $303,485 | $235,508 | 77.6% |

## Paid-amount concentration

Share of total paid (3140 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 32 | 13.5% |
| top 5% | 157 | 54.1% |
| top 10% | 314 | 86.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 80 | 99285 (21%), 93000 (14%), 85025 (10%) |
| timely filing exceeded | 78 | 27447 (14%), 99214 (13%), 85025 (12%) |
| out-of-network provider | 75 | 70450 (15%), 43239 (13%), 99285 (13%) |

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
| 27447 | 338 | $24,928 | $4,987,959 | 9.8% |
| 43239 | 312 | $2,047 | $360,648 | 13.5% |
| 99285 | 329 | $1,074 | $199,063 | 14.6% |
| 70450 | 310 | $654 | $118,306 | 11.3% |
| 99214 | 314 | $167 | $29,078 | 14.6% |

## Member utilization

428 of 1574 synthetic members have 3+ claims and account for 48.1% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 6 | $35,318 |
| MBR-0693 | 6 | $30,518 |
| MBR-0471 | 6 | $28,114 |
| MBR-0884 | 6 | $16,003 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 104 | missing prior authorization | 28 |
| HDHP | 85 | timely filing exceeded | 22 |
| HMO | 90 | out-of-network provider | 20 |
| PPO | 89 | timely filing exceeded | 23 |

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

46 groups share a member, procedure and service date (review queue, not a quality failure).

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
