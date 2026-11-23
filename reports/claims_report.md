# Healthcare Data - claims pipeline report

Generated 2026-11-23 14:30 UTC. All data is synthetic - no real member, patient or plan information.

**4880 claims** in store. Billed $12,237,220, paid $6,965,319, denied 625 overall.

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
| 2026-11 | 4401 | $11,121,941 | $8,498,643 | $6,268,711 | 13.1% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 843 | $2,594 | $1,243,238 | 11.9% |
| Z00.00 | General adult medical exam | 661 | $2,899 | $1,196,619 | 12.9% |
| R51 | Headache | 886 | $2,562 | $1,188,244 | 14.6% |
| J06.9 | Acute upper respiratory infection | 829 | $2,521 | $1,182,765 | 12.6% |
| M54.5 | Low back pain | 838 | $2,290 | $1,096,976 | 12.4% |
| E11.9 | Type 2 diabetes without complications | 823 | $2,254 | $1,057,476 | 12.5% |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3765 | 77.1% | $9,284,749 | $6,087,009 |
| adjusted | 490 | 10.0% | $1,380,461 | $878,309 |
| denied | 625 | 12.8% | $1,572,010 | $0 |

## Denial reasons

- out-of-network provider (157)
- missing prior authorization (152)
- not medically necessary (152)
- timely filing exceeded (147)
- duplicate claim (17)

## Plan mix

- PPO: 1247
- EPO: 1242
- HDHP: 1199
- HMO: 1192

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1247 | 11.8% | 54.5% |
| EPO | 1242 | 13.4% | 55.5% |
| HDHP | 1199 | 11.8% | 61.4% |
| HMO | 1192 | 14.3% | 55.7% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1021 | 22.4% | 15.8% |
| PPO | 1100 | 23.9% | 15.7% |
| HDHP | 1058 | 21.9% | 15.2% |
| EPO | 1076 | 24.1% | 13.9% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 152 | $485,635 | 30.9% | $3,195 |
| not medically necessary | 152 | $391,591 | 24.9% | $2,576 |
| timely filing exceeded | 147 | $391,514 | 24.9% | $2,663 |
| out-of-network provider | 157 | $246,604 | 15.7% | $1,571 |
| duplicate claim | 17 | $56,666 | 3.6% | $3,333 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 101 (108 later claims)
- Later claims denied as duplicate: 17
- Later claims still paid: 82 ($177,403 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 436 | 24.1% | $398,248 | 5.7% |
| 2 claims | 493 | 27.3% | $1,456,864 | 20.9% |
| 3 claims | 396 | 21.9% | $1,727,006 | 24.8% |
| 4+ claims | 484 | 26.8% | $3,383,200 | 48.6% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1422 | 29.1% | $56,043 | 0.8% | 12.6% |
| $100-$999 | 2260 | 46.3% | $415,746 | 6.0% | 12.6% |
| $1,000-$9,999 | 793 | 16.2% | $776,559 | 11.2% | 13.9% |
| $10,000+ | 405 | 8.3% | $5,716,971 | 82.1% | 12.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,880 | 4,880 | yes |
| claims: plan mix | 4,880 | 4,880 | yes |
| claims: plan performance | 4,880 | 4,880 | yes |
| claims: age bands | 4,880 | 4,880 | yes |
| claims: cost per member | 4,880 | 4,880 | yes |
| paid $: monthly view | 6,965,318.51 | 6,965,318.51 | yes |
| paid $: age bands | 6,965,320.24 | 6,965,318.51 | yes |
| denied claims: reasons | 625 | 625 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1543 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 439 | 1199 | 2.73 | $4,825 |
| PPO | 454 | 1247 | 2.75 | $4,155 |
| EPO | 464 | 1242 | 2.68 | $3,319 |
| HMO | 452 | 1192 | 2.64 | $3,144 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 7 | 4 | 57.1% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0912 | 4 | 3 | 75.0% |
| MBR-0255 | 5 | 3 | 60.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 43239 | 428 | $871,877 | $670,752 | 76.9% |
| 27447 | 354 | $8,752,750 | $6,734,176 | 76.9% |
| 85025 | 425 | $22,720 | $17,549 | 77.2% |
| 99214 | 434 | $72,706 | $56,241 | 77.3% |
| 99213 | 441 | $53,123 | $41,137 | 77.4% |
| 99285 | 451 | $481,561 | $372,906 | 77.4% |

## Paid-amount concentration

Share of total paid (4880 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 49 | 16.6% |
| top 5% | 244 | 64.3% |
| top 10% | 488 | 85.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 157 | 99285 (13%), 93000 (12%), 43239 (11%) |
| missing prior authorization | 152 | 99285 (12%), 85025 (12%), 99214 (11%) |
| not medically necessary | 152 | 43239 (14%), 99285 (14%), 93000 (12%) |

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
| 27447 | 405 | $24,780 | $5,716,971 | 12.6% |
| 43239 | 497 | $2,027 | $564,965 | 13.9% |
| 99285 | 529 | $1,060 | $316,472 | 14.7% |
| 70450 | 491 | $650 | $186,067 | 11.4% |
| 99214 | 494 | $168 | $47,760 | 12.2% |

## Member utilization

880 of 1809 synthetic members have 3+ claims and account for 73.4% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 11 | $588 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-1595 | 8 | $2,560 |
| MBR-0979 | 8 | $381 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 166 | out-of-network provider | 43 |
| HDHP | 141 | missing prior authorization | 39 |
| HMO | 171 | not medically necessary | 44 |
| PPO | 147 | not medically necessary | 41 |

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

101 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-22 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |
| MBR-1175 | 27447 | 2026-11-22 | 2 | $28,226 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
