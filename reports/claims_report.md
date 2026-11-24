# Healthcare Data - claims pipeline report

Generated 2026-11-24 00:40 UTC. All data is synthetic - no real member, patient or plan information.

**5180 claims** in store. Billed $12,773,619, paid $7,265,960, denied 678 overall.

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
| 2026-11 | 4701 | $11,658,340 | $8,892,310 | $6,569,353 | 13.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 899 | $2,631 | $1,350,614 | 12.6% |
| Z00.00 | General adult medical exam | 693 | $2,816 | $1,217,432 | 13.4% |
| R51 | Headache | 933 | $2,486 | $1,215,114 | 14.4% |
| J06.9 | Acute upper respiratory infection | 889 | $2,434 | $1,213,300 | 12.9% |
| M54.5 | Low back pain | 892 | $2,311 | $1,187,770 | 12.6% |
| E11.9 | Type 2 diabetes without complications | 874 | $2,188 | $1,081,731 | 12.8% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 113 | 8.8% | $6,494 |
| M54.5 | 99285 | 111 | 16.2% | $67,016 |
| R51 | 80053 | 106 | 13.2% | $5,009 |
| R51 | 43239 | 105 | 18.1% | $114,702 |
| M54.5 | 80053 | 103 | 12.6% | $4,631 |
| E11.9 | 80053 | 101 | 12.9% | $4,546 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3988 | 77.0% | $9,559,597 | $6,269,362 |
| adjusted | 513 | 9.9% | $1,552,013 | $996,599 |
| denied | 679 | 13.1% | $1,662,009 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-11 | 629 | missing prior authorization | 25.0% |

## Denial reasons

- out-of-network provider (167)
- not medically necessary (165)
- missing prior authorization (163)
- timely filing exceeded (160)
- duplicate claim (24)

## Plan mix

- EPO: 1319
- PPO: 1309
- HDHP: 1277
- HMO: 1275

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1319 | 13.7% | 54.9% |
| PPO | 1309 | 12.2% | 54.1% |
| HDHP | 1277 | 12.1% | 61.7% |
| HMO | 1275 | 14.4% | 56.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1091 | 22.2% | 15.8% |
| PPO | 1150 | 23.9% | 15.7% |
| HDHP | 1122 | 21.9% | 14.8% |
| EPO | 1138 | 24.2% | 14.0% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 163 | $492,150 | 29.6% | $3,019 |
| not medically necessary | 165 | $418,866 | 25.2% | $2,539 |
| timely filing exceeded | 160 | $394,203 | 23.7% | $2,464 |
| out-of-network provider | 167 | $269,360 | 16.2% | $1,613 |
| duplicate claim | 24 | $87,430 | 5.3% | $3,643 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 112 (120 later claims)
- Later claims denied as duplicate: 24
- Later claims still paid: 87 ($206,261 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 409 | 22.3% | $390,943 | 5.4% |
| 2 claims | 476 | 25.9% | $1,301,738 | 17.9% |
| 3 claims | 404 | 22.0% | $1,659,495 | 22.8% |
| 4+ claims | 548 | 29.8% | $3,913,784 | 53.9% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1511 | 29.2% | $59,298 | 0.8% | 12.8% |
| $100-$999 | 2412 | 46.6% | $438,884 | 6.0% | 13.1% |
| $1,000-$9,999 | 836 | 16.1% | $819,846 | 11.3% | 13.9% |
| $10,000+ | 421 | 8.1% | $5,947,931 | 81.9% | 12.8% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,180 | 5,180 | yes |
| claims: plan mix | 5,180 | 5,180 | yes |
| claims: plan performance | 5,180 | 5,180 | yes |
| claims: age bands | 5,180 | 5,180 | yes |
| claims: cost per member | 5,180 | 5,180 | yes |
| paid $: monthly view | 7,265,960.33 | 7,265,960.33 | yes |
| paid $: age bands | 7,265,961.21 | 7,265,960.33 | yes |
| denied claims: reasons | 679 | 679 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1843 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 445 | 1277 | 2.87 | $4,987 |
| PPO | 464 | 1309 | 2.82 | $4,094 |
| EPO | 469 | 1319 | 2.81 | $3,485 |
| HMO | 459 | 1275 | 2.78 | $3,296 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0912 | 4 | 3 | 75.0% |
| MBR-0255 | 6 | 3 | 50.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 43239 | 453 | $924,324 | $709,029 | 76.7% |
| 27447 | 367 | $9,090,570 | $6,996,204 | 77.0% |
| 85025 | 452 | $24,140 | $18,653 | 77.3% |
| 99213 | 473 | $56,869 | $43,969 | 77.3% |
| 99285 | 477 | $508,480 | $393,614 | 77.4% |
| 97110 | 404 | $48,417 | $37,528 | 77.5% |

## Paid-amount concentration

Share of total paid (5180 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 52 | 17.0% |
| top 5% | 259 | 65.4% |
| top 10% | 518 | 85.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 167 | 80053 (13%), 99285 (13%), 93000 (12%) |
| not medically necessary | 165 | 43239 (15%), 99285 (13%), 93000 (12%) |
| missing prior authorization | 163 | 99285 (14%), 85025 (12%), 99214 (11%) |

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
| 27447 | 421 | $24,804 | $5,947,931 | 12.8% |
| 43239 | 526 | $2,033 | $598,357 | 13.9% |
| 99285 | 560 | $1,058 | $333,685 | 14.8% |
| 70450 | 513 | $649 | $193,466 | 11.9% |
| 99214 | 523 | $168 | $50,622 | 12.0% |

## Member utilization

952 of 1837 synthetic members have 3+ claims and account for 76.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 11 | $588 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-0961 | 9 | $3,263 |
| MBR-0154 | 8 | $27,766 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 181 | out-of-network provider | 46 |
| HDHP | 155 | missing prior authorization | 44 |
| HMO | 184 | not medically necessary | 48 |
| PPO | 159 | not medically necessary | 43 |

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

112 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-11-18 | 3 | $55,302 |
| MBR-0743 | 27447 | 2026-11-23 | 2 | $54,807 |
| MBR-0076 | 27447 | 2026-11-17 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-22 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-11-21 | 2 | $33,395 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
