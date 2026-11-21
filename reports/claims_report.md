# Healthcare Data - claims pipeline report

Generated 2026-11-21 22:19 UTC. All data is synthetic - no real member, patient or plan information.

**3800 claims** in store. Billed $9,526,178, paid $5,538,798, denied 462 overall.

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
| 2026-11 | 3321 | $8,410,899 | $6,495,847 | $4,842,190 | 12.4% |

## Denial reasons

- duplicate claim (103)
- timely filing exceeded (93)
- missing prior authorization (90)
- out-of-network provider (90)
- not medically necessary (86)

## Plan mix

- HMO: 959
- EPO: 951
- HDHP: 948
- PPO: 942

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| HMO | 959 | 14.9% | 55.5% |
| EPO | 951 | 12.3% | 57.3% |
| HDHP | 948 | 11.1% | 62.9% |
| PPO | 942 | 10.3% | 56.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 816 | 22.0% | 16.3% |
| PPO | 845 | 24.4% | 16.0% |
| HDHP | 843 | 21.5% | 15.3% |
| EPO | 834 | 23.3% | 13.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding.

| Plan | Month | Claims | Denial rate | Overall | z |
| --- | --- | ---: | ---: | ---: | ---: |
| HMO | 2026-11 | 831 | 15.5% | 12.2% | +2.97 |

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| timely filing exceeded | 93 | $273,050 | 26.0% | $2,936 |
| not medically necessary | 86 | $242,826 | 23.1% | $2,824 |
| missing prior authorization | 90 | $205,748 | 19.6% | $2,286 |
| duplicate claim | 103 | $176,711 | 16.8% | $1,716 |
| out-of-network provider | 90 | $153,335 | 14.6% | $1,704 |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 3,800 | 3,800 | yes |
| claims: plan mix | 3,800 | 3,800 | yes |
| claims: plan performance | 3,800 | 3,800 | yes |
| claims: age bands | 3,800 | 3,800 | yes |
| claims: cost per member | 3,800 | 3,800 | yes |
| paid $: monthly view | 5,538,798.23 | 5,538,798.23 | yes |
| paid $: age bands | 5,538,802.29 | 5,538,798.23 | yes |
| denied claims: reasons | 462 | 462 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 497 |
| regenerated-2026-11-21 | 3303 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 424 | 948 | 2.24 | $3,941 |
| PPO | 421 | 942 | 2.24 | $3,478 |
| HMO | 428 | 959 | 2.24 | $2,881 |
| EPO | 432 | 951 | 2.20 | $2,710 |

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
| 99214 | 337 | $56,423 | $43,394 | 76.9% |
| 27447 | 282 | $6,993,842 | $5,397,280 | 77.2% |
| 43239 | 325 | $661,201 | $510,606 | 77.2% |
| 99213 | 346 | $41,675 | $32,237 | 77.3% |
| 93000 | 355 | $35,624 | $27,586 | 77.4% |
| 97110 | 295 | $35,078 | $27,183 | 77.5% |

## Paid-amount concentration

Share of total paid (3800 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 38 | 16.3% |
| top 5% | 190 | 63.7% |
| top 10% | 380 | 85.8% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| duplicate claim | 103 | 99285 (19%), 93000 (16%), 85025 (12%) |
| timely filing exceeded | 93 | 93000 (13%), 27447 (11%), 85025 (11%) |
| missing prior authorization | 90 | 99214 (17%), 99285 (13%), 43239 (12%) |

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
| 27447 | 315 | $24,808 | $4,572,006 | 10.5% |
| 43239 | 379 | $2,034 | $429,352 | 14.2% |
| 99285 | 421 | $1,062 | $249,454 | 15.2% |
| 70450 | 382 | $653 | $145,968 | 11.3% |
| 99214 | 386 | $168 | $36,814 | 12.7% |

## Member utilization

603 of 1705 synthetic members have 3+ claims and account for 63.1% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 8 | $473 |
| MBR-1219 | 7 | $49,745 |
| MBR-0856 | 7 | $18,174 |
| MBR-1062 | 7 | $9,989 |
| MBR-0693 | 6 | $30,518 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 117 | out-of-network provider | 28 |
| HDHP | 105 | duplicate claim | 28 |
| HMO | 143 | duplicate claim | 35 |
| PPO | 97 | duplicate claim | 23 |

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

60 groups share a member, procedure and service date (review queue, not a quality failure).

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
