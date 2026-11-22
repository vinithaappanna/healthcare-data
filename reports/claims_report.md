# Healthcare Data - claims pipeline report

Generated 2026-11-22 13:21 UTC. All data is synthetic - no real member, patient or plan information.

**4160 claims** in store. Billed $10,407,151, paid $5,928,346, denied 517 overall.

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
| 2026-11 | 3681 | $9,291,872 | $7,150,584 | $5,231,738 | 12.7% |

## Denial reasons

- duplicate claim (118)
- missing prior authorization (104)
- timely filing exceeded (103)
- out-of-network provider (99)
- not medically necessary (93)

## Plan mix

- PPO: 1051
- EPO: 1049
- HMO: 1031
- HDHP: 1029

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| PPO | 1051 | 10.8% | 53.8% |
| EPO | 1049 | 12.4% | 56.3% |
| HMO | 1031 | 14.9% | 55.0% |
| HDHP | 1029 | 11.6% | 62.3% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| PPO | 937 | 24.5% | 16.3% |
| HMO | 877 | 22.0% | 16.3% |
| HDHP | 910 | 21.3% | 15.2% |
| EPO | 919 | 23.8% | 13.8% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 903 | 15.5% | 12.4% | +2.80 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 104 | $329,544 | 25.0% | $3,169 |
| timely filing exceeded | 103 | $276,363 | 21.0% | $2,683 |
| not medically necessary | 93 | $268,793 | 20.4% | $2,890 |
| duplicate claim | 118 | $252,917 | 19.2% | $2,143 |
| out-of-network provider | 99 | $190,248 | 14.4% | $1,922 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate, and this synthetic data is random.

- Groups with repeats: 65 (68 later claims)
- Later claims denied as duplicate: 1
- Later claims still paid: 58 ($133,096 to review)
- Claims denied as duplicate with no matching original: 115

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1228 | 29.5% | $48,692 | 0.8% | 12.0% |
| $100-$999 | 1919 | 46.1% | $353,899 | 6.0% | 12.1% |
| $1,000-$9,999 | 668 | 16.1% | $649,298 | 10.9% | 14.1% |
| $10,000+ | 345 | 8.3% | $4,876,456 | 82.3% | 12.5% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 4,160 | 4,160 | yes |
| claims: plan mix | 4,160 | 4,160 | yes |
| claims: plan performance | 4,160 | 4,160 | yes |
| claims: age bands | 4,160 | 4,160 | yes |
| claims: cost per member | 4,160 | 4,160 | yes |
| paid $: monthly view | 5,928,345.62 | 5,928,345.62 | yes |
| paid $: age bands | 5,928,341.89 | 5,928,345.62 | yes |
| denied claims: reasons | 517 | 517 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 857 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 432 | 1029 | 2.38 | $4,141 |
| PPO | 437 | 1051 | 2.41 | $3,585 |
| HMO | 437 | 1031 | 2.36 | $2,941 |
| EPO | 444 | 1049 | 2.36 | $2,900 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 7 | 4 | 57.1% |
| MBR-0912 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 99214 | 363 | $60,620 | $46,644 | 76.9% |
| 27447 | 302 | $7,481,615 | $5,765,099 | 77.1% |
| 43239 | 355 | $718,180 | $554,500 | 77.2% |
| 93000 | 394 | $39,319 | $30,408 | 77.3% |
| 85025 | 369 | $19,806 | $15,325 | 77.4% |
| 99213 | 384 | $46,198 | $35,747 | 77.4% |

## Paid-amount concentration

Share of total paid (4160 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 42 | 16.7% |
| top 5% | 208 | 64.6% |
| top 10% | 416 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 118 | 99285 (18%), 93000 (15%), 85025 (12%) |
| missing prior authorization | 104 | 99214 (14%), 99285 (13%), 43239 (12%) |
| timely filing exceeded | 103 | 80053 (13%), 93000 (13%), 99213 (11%) |

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
| 27447 | 345 | $24,786 | $4,876,456 | 12.5% |
| 43239 | 413 | $2,021 | $467,907 | 14.0% |
| 99285 | 455 | $1,063 | $271,705 | 15.2% |
| 70450 | 413 | $653 | $157,156 | 11.6% |
| 99214 | 414 | $167 | $39,557 | 12.3% |

## Member utilization

692 of 1750 synthetic members have 3+ claims and account for 67.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 9 | $542 |
| MBR-1219 | 7 | $49,745 |
| MBR-0856 | 7 | $18,174 |
| MBR-1062 | 7 | $9,989 |
| MBR-0961 | 7 | $2,171 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 130 | out-of-network provider | 29 |
| HDHP | 119 | duplicate claim | 33 |
| HMO | 154 | duplicate claim | 38 |
| PPO | 114 | duplicate claim | 26 |

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

65 groups share a member, procedure and service date (review queue, not a quality failure).

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
