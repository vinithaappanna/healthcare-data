# Healthcare Data - claims pipeline report

Generated 2026-11-22 13:24 UTC. All data is synthetic - no real member, patient or plan information.

**4280 claims** in store. Billed $10,650,585, paid $6,061,805, denied 535 overall.

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
| 2026-11 | 3801 | $9,535,306 | $7,326,962 | $5,365,198 | 12.8% |

## Denial reasons

- timely filing exceeded (138)
- out-of-network provider (135)
- missing prior authorization (132)
- not medically necessary (128)
- duplicate claim (2)

## Plan mix

- PPO: 1084
- EPO: 1077
- HMO: 1060
- HDHP: 1059

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1084 | 11.2% | 53.4% |
| EPO | 1077 | 12.6% | 56.6% |
| HMO | 1060 | 14.9% | 55.0% |
| HDHP | 1059 | 11.3% | 62.3% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 902 | 22.0% | 16.2% |
| PPO | 963 | 24.5% | 16.2% |
| HDHP | 939 | 21.5% | 15.1% |
| EPO | 941 | 23.8% | 13.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 932 | 15.4% | 12.5% | +2.72 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 132 | $429,513 | 31.6% | $3,254 |
| timely filing exceeded | 138 | $386,158 | 28.4% | $2,798 |
| not medically necessary | 128 | $326,311 | 24.0% | $2,549 |
| out-of-network provider | 135 | $215,280 | 15.8% | $1,595 |
| duplicate claim | 2 | $1,435 | 0.1% | $718 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 70 (74 later claims)
- Later claims denied as duplicate: 2
- Later claims still paid: 63 ($135,864 to review)
- Claims denied as duplicate with no matching original: 0

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1258 | 29.4% | $49,884 | 0.8% | 11.9% |
| $100-$999 | 1978 | 46.2% | $364,641 | 6.0% | 12.3% |
| $1,000-$9,999 | 692 | 16.2% | $671,012 | 11.1% | 14.2% |
| $10,000+ | 352 | 8.2% | $4,976,268 | 82.1% | 12.5% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,280 | 4,280 | yes |
| claims: plan mix | 4,280 | 4,280 | yes |
| claims: plan performance | 4,280 | 4,280 | yes |
| claims: age bands | 4,280 | 4,280 | yes |
| claims: cost per member | 4,280 | 4,280 | yes |
| paid $: monthly view | 6,061,805.41 | 6,061,805.41 | yes |
| paid $: age bands | 6,061,801.06 | 6,061,805.41 | yes |
| denied claims: reasons | 535 | 535 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 943 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 434 | 1059 | 2.44 | $4,214 |
| PPO | 442 | 1084 | 2.45 | $3,639 |
| EPO | 450 | 1077 | 2.39 | $2,959 |
| HMO | 441 | 1060 | 2.40 | $2,932 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 7 | 4 | 57.1% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0912 | 4 | 3 | 75.0% |
| MBR-0358 | 6 | 3 | 50.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 308 | $7,630,700 | $5,873,070 | 77.0% |
| 99214 | 378 | $63,143 | $48,613 | 77.0% |
| 43239 | 370 | $746,738 | $576,019 | 77.1% |
| 93000 | 402 | $40,085 | $30,987 | 77.3% |
| 99213 | 394 | $47,495 | $36,730 | 77.3% |
| 85025 | 375 | $20,109 | $15,560 | 77.4% |

## Paid-amount concentration

Share of total paid (4280 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 43 | 16.8% |
| top 5% | 214 | 64.9% |
| top 10% | 428 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| timely filing exceeded | 138 | 85025 (12%), 93000 (12%), 80053 (11%) |
| out-of-network provider | 135 | 99285 (16%), 43239 (13%), 93000 (13%) |
| missing prior authorization | 132 | 99285 (14%), 99214 (13%), 43239 (11%) |

## Data quality gates

9 of 9 checks passed on this run.

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
| duplicate denials supported | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 352 | $24,807 | $4,976,268 | 12.5% |
| 43239 | 431 | $2,014 | $485,425 | 14.1% |
| 99285 | 466 | $1,063 | $278,563 | 15.0% |
| 70450 | 426 | $655 | $161,998 | 11.7% |
| 99214 | 431 | $167 | $41,235 | 12.3% |

## Member utilization

723 of 1767 synthetic members have 3+ claims and account for 68.4% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 9 | $542 |
| MBR-1219 | 7 | $49,745 |
| MBR-0856 | 7 | $18,174 |
| MBR-1062 | 7 | $9,989 |
| MBR-1595 | 7 | $2,228 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 136 | out-of-network provider | 36 |
| HDHP | 120 | missing prior authorization | 36 |
| HMO | 158 | not medically necessary | 41 |
| PPO | 121 | not medically necessary | 33 |

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

70 groups share a member, procedure and service date (review queue, not a quality failure).

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
