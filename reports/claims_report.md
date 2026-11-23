# Healthcare Data - claims pipeline report

Generated 2026-11-23 09:24 UTC. All data is synthetic - no real member, patient or plan information.

**4820 claims** in store. Billed $12,019,569, paid $6,841,202, denied 615 overall.

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
| 2026-11 | 4341 | $10,904,290 | $8,352,288 | $6,144,594 | 13.0% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 838 | $2,606 | $1,241,806 | 11.9% |
| R51 | Headache | 871 | $2,545 | $1,170,993 | 14.3% |
| J06.9 | Acute upper respiratory infection | 822 | $2,503 | $1,163,866 | 12.5% |
| Z00.00 | General adult medical exam | 654 | $2,864 | $1,163,001 | 13.0% |
| M54.5 | Low back pain | 824 | $2,286 | $1,079,344 | 12.4% |
| E11.9 | Type 2 diabetes without complications | 811 | $2,225 | $1,022,192 | 12.3% |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 3719 | 77.2% | $9,092,573 | $5,963,113 |
| adjusted | 486 | 10.1% | $1,380,139 | $878,089 |
| denied | 615 | 12.8% | $1,546,857 | $0 |

## Denial reasons

- out-of-network provider (154)
- missing prior authorization (151)
- not medically necessary (149)
- timely filing exceeded (146)
- duplicate claim (15)

## Plan mix

- PPO: 1232
- EPO: 1226
- HDHP: 1182
- HMO: 1180

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1232 | 11.7% | 54.5% |
| EPO | 1226 | 13.3% | 55.9% |
| HDHP | 1182 | 11.7% | 61.3% |
| HMO | 1180 | 14.4% | 55.4% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1010 | 22.3% | 16.0% |
| PPO | 1088 | 23.9% | 15.7% |
| HDHP | 1044 | 21.9% | 15.2% |
| EPO | 1063 | 23.9% | 13.7% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 1052 | 14.8% | 12.8% | +2.01 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 151 | $485,532 | 31.4% | $3,215 |
| not medically necessary | 149 | $391,349 | 25.3% | $2,626 |
| timely filing exceeded | 146 | $390,814 | 25.3% | $2,677 |
| out-of-network provider | 154 | $245,918 | 15.9% | $1,597 |
| duplicate claim | 15 | $33,245 | 2.1% | $2,216 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 99 (106 later claims)
- Later claims denied as duplicate: 15
- Later claims still paid: 82 ($177,403 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 447 | 24.7% | $401,858 | 5.9% |
| 2 claims | 495 | 27.4% | $1,442,039 | 21.1% |
| 3 claims | 398 | 22.0% | $1,810,342 | 26.5% |
| 4+ claims | 467 | 25.8% | $3,186,964 | 46.6% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1401 | 29.1% | $55,241 | 0.8% | 12.5% |
| $100-$999 | 2235 | 46.4% | $412,069 | 6.0% | 12.5% |
| $1,000-$9,999 | 787 | 16.3% | $770,106 | 11.3% | 14.0% |
| $10,000+ | 397 | 8.2% | $5,603,787 | 81.9% | 12.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,820 | 4,820 | yes |
| claims: plan mix | 4,820 | 4,820 | yes |
| claims: plan performance | 4,820 | 4,820 | yes |
| claims: age bands | 4,820 | 4,820 | yes |
| claims: cost per member | 4,820 | 4,820 | yes |
| paid $: monthly view | 6,841,202.08 | 6,841,202.08 | yes |
| paid $: age bands | 6,841,203.26 | 6,841,202.08 | yes |
| denied claims: reasons | 615 | 615 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1483 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 439 | 1182 | 2.69 | $4,771 |
| PPO | 453 | 1232 | 2.72 | $4,157 |
| EPO | 463 | 1226 | 2.65 | $3,177 |
| HMO | 452 | 1180 | 2.61 | $3,081 |

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
| 27447 | 347 | $8,578,996 | $6,602,576 | 77.0% |
| 43239 | 425 | $863,546 | $665,302 | 77.0% |
| 85025 | 419 | $22,422 | $17,309 | 77.2% |
| 99214 | 427 | $71,599 | $55,412 | 77.4% |
| 99285 | 446 | $476,258 | $368,839 | 77.5% |
| 99213 | 436 | $52,444 | $40,630 | 77.5% |

## Paid-amount concentration

Share of total paid (4820 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 49 | 16.9% |
| top 5% | 241 | 64.6% |
| top 10% | 482 | 85.5% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 154 | 99285 (14%), 93000 (12%), 43239 (12%) |
| missing prior authorization | 151 | 99285 (13%), 85025 (12%), 99214 (11%) |
| not medically necessary | 149 | 43239 (15%), 99285 (14%), 93000 (12%) |

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
| 27447 | 397 | $24,782 | $5,603,787 | 12.6% |
| 43239 | 494 | $2,022 | $560,601 | 14.0% |
| 99285 | 524 | $1,060 | $313,231 | 14.9% |
| 70450 | 486 | $650 | $184,935 | 11.1% |
| 99214 | 487 | $168 | $47,051 | 12.3% |

## Member utilization

865 of 1807 synthetic members have 3+ claims and account for 73.0% of paid dollars.

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
| EPO | 163 | out-of-network provider | 42 |
| HDHP | 138 | missing prior authorization | 39 |
| HMO | 170 | out-of-network provider | 44 |
| PPO | 144 | not medically necessary | 41 |

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

99 groups share a member, procedure and service date (review queue, not a quality failure).

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
