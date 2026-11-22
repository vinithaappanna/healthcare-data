# Healthcare Data - claims pipeline report

Generated 2026-11-22 18:22 UTC. All data is synthetic - no real member, patient or plan information.

**4400 claims** in store. Billed $10,966,274, paid $6,242,553, denied 547 overall.

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
| 2026-11 | 3921 | $9,850,995 | $7,562,151 | $5,545,946 | 12.7% |

## Denial reasons

- out-of-network provider (140)
- timely filing exceeded (140)
- missing prior authorization (134)
- not medically necessary (130)
- duplicate claim (3)

## Plan mix

- PPO: 1121
- EPO: 1106
- HDHP: 1089
- HMO: 1084

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1121 | 11.2% | 54.0% |
| EPO | 1106 | 12.7% | 56.7% |
| HDHP | 1089 | 11.4% | 61.6% |
| HMO | 1084 | 14.6% | 55.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 926 | 22.1% | 16.3% |
| PPO | 996 | 24.5% | 16.1% |
| HDHP | 965 | 21.7% | 15.2% |
| EPO | 966 | 23.8% | 13.5% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 956 | 15.1% | 12.4% | +2.47 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 134 | $429,683 | 31.0% | $3,207 |
| timely filing exceeded | 140 | $386,426 | 27.9% | $2,760 |
| not medically necessary | 130 | $326,427 | 23.5% | $2,511 |
| out-of-network provider | 140 | $241,827 | 17.4% | $1,727 |
| duplicate claim | 3 | $2,106 | 0.1% | $702 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 73 (77 later claims)
- Later claims denied as duplicate: 3
- Later claims still paid: 65 ($137,412 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 516 | 29.0% | $569,551 | 9.1% |
| 2 claims | 498 | 28.0% | $1,286,193 | 20.6% |
| 3 claims | 389 | 21.9% | $1,777,685 | 28.5% |
| 4+ claims | 375 | 21.1% | $2,609,125 | 41.8% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1287 | 29.2% | $50,901 | 0.8% | 12.0% |
| $100-$999 | 2036 | 46.3% | $375,622 | 6.0% | 12.2% |
| $1,000-$9,999 | 715 | 16.2% | $696,845 | 11.2% | 13.7% |
| $10,000+ | 362 | 8.2% | $5,119,186 | 82.0% | 12.4% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,400 | 4,400 | yes |
| claims: plan mix | 4,400 | 4,400 | yes |
| claims: plan performance | 4,400 | 4,400 | yes |
| claims: age bands | 4,400 | 4,400 | yes |
| claims: cost per member | 4,400 | 4,400 | yes |
| paid $: monthly view | 6,242,553.47 | 6,242,553.47 | yes |
| paid $: age bands | 6,242,551.79 | 6,242,553.47 | yes |
| denied claims: reasons | 547 | 547 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 1063 |
| regenerated-2026-11-21 | 3220 |
| regenerated-2026-11-21+2026-11-22 | 83 |
| regenerated-2026-11-22 | 34 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 435 | 1089 | 2.50 | $4,334 |
| PPO | 446 | 1121 | 2.51 | $3,831 |
| EPO | 453 | 1106 | 2.44 | $2,977 |
| HMO | 444 | 1084 | 2.44 | $2,927 |

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
| 27447 | 317 | $7,859,401 | $6,043,789 | 76.9% |
| 43239 | 385 | $777,221 | $598,412 | 77.0% |
| 99214 | 394 | $65,941 | $50,817 | 77.1% |
| 85025 | 384 | $20,590 | $15,921 | 77.3% |
| 93000 | 410 | $40,845 | $31,590 | 77.3% |
| 99213 | 400 | $48,314 | $37,402 | 77.4% |

## Paid-amount concentration

Share of total paid (4400 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 44 | 16.7% |
| top 5% | 220 | 64.7% |
| top 10% | 440 | 85.5% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 140 | 99285 (15%), 43239 (12%), 70450 (12%) |
| timely filing exceeded | 140 | 85025 (12%), 93000 (12%), 80053 (11%) |
| missing prior authorization | 134 | 99285 (13%), 99214 (13%), 43239 (11%) |

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
| 27447 | 362 | $24,824 | $5,119,186 | 12.4% |
| 43239 | 446 | $2,014 | $504,829 | 13.7% |
| 99285 | 478 | $1,064 | $286,952 | 14.6% |
| 70450 | 441 | $655 | $167,497 | 11.8% |
| 99214 | 448 | $168 | $43,083 | 12.0% |

## Member utilization

764 of 1778 synthetic members have 3+ claims and account for 70.3% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-0124 | 9 | $16,460 |
| MBR-1200 | 9 | $542 |
| MBR-1219 | 7 | $49,745 |
| MBR-1787 | 7 | $21,621 |
| MBR-1765 | 7 | $18,717 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 140 | out-of-network provider | 37 |
| HDHP | 124 | missing prior authorization | 37 |
| HMO | 158 | not medically necessary | 41 |
| PPO | 125 | not medically necessary | 34 |

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

73 groups share a member, procedure and service date (review queue, not a quality failure).

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
