# Healthcare Data - claims pipeline report

Generated 2026-11-21 17:22 UTC. All data is synthetic - no real member, patient or plan information.

**3680 claims** in store. Billed $9,271,692, paid $5,410,143, denied 445 overall.

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
| 2026-11 | 3201 | $8,156,413 | $6,297,042 | $4,713,535 | 12.4% |

## Denial reasons

- duplicate claim (100)
- timely filing exceeded (90)
- out-of-network provider (86)
- missing prior authorization (85)
- not medically necessary (85)

## Plan mix

- HMO: 933
- EPO: 919
- HDHP: 918
- PPO: 910

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 933 | 15.0% | 55.4% |
| EPO | 919 | 12.3% | 58.1% |
| HDHP | 918 | 10.9% | 63.3% |
| PPO | 910 | 10.2% | 56.1% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 793 | 22.0% | 16.4% |
| PPO | 817 | 24.6% | 15.8% |
| HDHP | 818 | 21.5% | 15.4% |
| EPO | 806 | 23.3% | 13.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 805 | 15.7% | 12.1% | +3.07 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 90 | $247,732 | 25.1% | $2,753 |
| not medically necessary | 85 | $242,777 | 24.6% | $2,856 |
| duplicate claim | 100 | $174,934 | 17.7% | $1,749 |
| missing prior authorization | 85 | $171,898 | 17.4% | $2,022 |
| out-of-network provider | 86 | $150,907 | 15.3% | $1,755 |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 377 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 419 | 918 | 2.19 | $3,860 |
| PPO | 420 | 910 | 2.17 | $3,401 |
| HMO | 425 | 933 | 2.20 | $2,856 |
| EPO | 429 | 919 | 2.14 | $2,681 |

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
| 99214 | 327 | $54,713 | $42,085 | 76.9% |
| 27447 | 275 | $6,842,478 | $5,275,506 | 77.1% |
| 99213 | 337 | $40,538 | $31,364 | 77.4% |
| 43239 | 317 | $646,144 | $500,017 | 77.4% |
| 93000 | 342 | $34,352 | $26,598 | 77.4% |
| 97110 | 292 | $34,810 | $26,964 | 77.5% |

## Paid-amount concentration

Share of total paid (3680 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 37 | 16.2% |
| top 5% | 184 | 63.4% |
| top 10% | 368 | 85.8% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 100 | 99285 (19%), 93000 (15%), 85025 (12%) |
| timely filing exceeded | 90 | 93000 (13%), 85025 (11%), 99214 (11%) |
| out-of-network provider | 86 | 99285 (15%), 70450 (14%), 43239 (12%) |

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
| 27447 | 306 | $24,856 | $4,468,135 | 10.1% |
| 43239 | 370 | $2,037 | $420,429 | 14.3% |
| 99285 | 408 | $1,063 | $242,540 | 15.2% |
| 70450 | 369 | $654 | $141,544 | 11.1% |
| 99214 | 376 | $168 | $35,711 | 13.0% |

## Member utilization

568 of 1693 synthetic members have 3+ claims and account for 60.4% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 7 | $49,745 |
| MBR-0856 | 7 | $18,174 |
| MBR-0693 | 6 | $30,518 |
| MBR-0154 | 6 | $27,628 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 113 | timely filing exceeded | 26 |
| HDHP | 100 | duplicate claim | 27 |
| HMO | 140 | duplicate claim | 33 |
| PPO | 93 | duplicate claim | 23 |

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

57 groups share a member, procedure and service date (review queue, not a quality failure).

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
