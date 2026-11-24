# Healthcare Data - claims pipeline report

Generated 2026-11-24 15:45 UTC. All data is synthetic - no real member, patient or plan information.

**5720 claims** in store. Billed $14,439,909, paid $8,201,665, denied 748 overall.

## Monthly financials

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

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
| 2026-08 | 582 | $1,549,011 | $1,186,564 | $872,665 | 12.2% |
| 2026-09 | 1774 | $4,446,457 | $3,418,088 | $2,584,068 | 13.4% |
| 2026-10 | 1784 | $4,180,591 | $3,159,583 | $2,337,029 | 14.0% |
| 2026-11 | 1226 | $3,362,340 | $2,536,014 | $1,829,539 | 12.7% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.8% |
| 2026-01 | 31 | 0.5% |
| 2026-02 | 32 | 0.6% |
| 2026-03 | 45 | 0.8% |
| 2026-04 | 48 | 0.8% |
| 2026-05 | 43 | 0.8% |
| 2026-06 | 46 | 0.8% |
| 2026-07 | 47 | 0.8% |
| 2026-08 | 582 | 10.2% |
| 2026-09 | 1774 | 31.0% |
| 2026-10 (largest) | 1784 | 31.2% |
| 2026-11 | 1226 | 21.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 1001 | $2,621 | $1,522,455 | 12.4% |
| R51 | Headache | 1032 | $2,571 | $1,410,605 | 13.6% |
| Z00.00 | General adult medical exam | 744 | $3,036 | $1,369,540 | 13.8% |
| J06.9 | Acute upper respiratory infection | 994 | $2,434 | $1,325,340 | 13.1% |
| M54.5 | Low back pain | 983 | $2,284 | $1,307,576 | 12.6% |
| E11.9 | Type 2 diabetes without complications | 966 | $2,317 | $1,266,149 | 13.2% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 122 | 8.2% | $7,078 |
| R51 | 80053 | 118 | 11.9% | $5,633 |
| M54.5 | 99285 | 117 | 16.2% | $70,826 |
| J06.9 | 93000 | 115 | 15.7% | $6,443 |
| M54.5 | 80053 | 111 | 12.6% | $4,934 |
| R51 | 43239 | 110 | 17.3% | $119,646 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4406 | 77.0% | $10,831,082 | $7,102,699 |
| adjusted | 566 | 9.9% | $1,713,252 | $1,098,965 |
| denied | 748 | 13.1% | $1,895,575 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 71 | not medically necessary | 28.2% |
| 2026-09 | 237 | missing prior authorization | 27.4% |
| 2026-10 | 249 | missing prior authorization | 26.1% |
| 2026-11 | 156 | timely filing exceeded | 25.6% |

## Denial reasons

- out-of-network provider (180)
- timely filing exceeded (180)
- not medically necessary (178)
- missing prior authorization (176)
- duplicate claim (34)

## Plan mix

- EPO: 1457
- PPO: 1428
- HMO: 1419
- HDHP: 1416

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1457 | 13.4% | 55.3% |
| PPO | 1428 | 12.0% | 55.1% |
| HMO | 1419 | 14.2% | 56.1% |
| HDHP | 1416 | 12.7% | 60.2% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1218 | 22.5% | 15.6% |
| PPO | 1256 | 24.1% | 15.3% |
| HDHP | 1236 | 22.2% | 14.8% |
| EPO | 1262 | 23.4% | 14.7% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 176 | $500,132 | 26.4% | $2,842 |
| not medically necessary | 178 | $466,471 | 24.6% | $2,621 |
| timely filing exceeded | 180 | $443,341 | 23.4% | $2,463 |
| out-of-network provider | 180 | $355,392 | 18.8% | $1,974 |
| duplicate claim | 34 | $130,238 | 6.9% | $3,831 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 129 (138 later claims)
- Later claims denied as duplicate: 34
- Later claims still paid: 94 ($209,028 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 322 | 17.3% | $311,985 | 3.8% |
| 2 claims | 460 | 24.7% | $1,269,631 | 15.5% |
| 3 claims | 432 | 23.2% | $1,914,946 | 23.4% |
| 4+ claims | 651 | 34.9% | $4,705,103 | 57.4% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1674 | 29.3% | $66,066 | 0.8% | 12.5% |
| $100-$999 | 2645 | 46.2% | $482,120 | 5.9% | 13.4% |
| $1,000-$9,999 | 922 | 16.1% | $913,733 | 11.1% | 13.2% |
| $10,000+ | 479 | 8.4% | $6,739,746 | 82.2% | 13.2% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,720 | 5,720 | yes |
| claims: plan mix | 5,720 | 5,720 | yes |
| claims: plan performance | 5,720 | 5,720 | yes |
| claims: age bands | 5,720 | 5,720 | yes |
| claims: cost per member | 5,720 | 5,720 | yes |
| paid $: monthly view | 8,201,664.64 | 8,201,664.64 | yes |
| paid $: age bands | 8,201,663.76 | 8,201,664.64 | yes |
| denied claims: reasons | 748 | 748 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 583 |
| regenerated-2026-11-21 | 553 |
| regenerated-2026-11-21+2026-11-22 | 12 |
| regenerated-2026-11-21+2026-11-22+2026-11-23 | 71 |
| regenerated-2026-11-21+2026-11-23 | 2667 |
| regenerated-2026-11-22 | 1 |
| regenerated-2026-11-22+2026-11-23 | 33 |
| regenerated-2026-11-23 | 1800 |

## Cost per member by plan

Distinct synthetic members, claims and paid dollars per member in the store. Not a true PMPM: there is no enrollment data. Illustrative only.

| Plan | Members | Claims | Claims / member | Paid / member |
| --- | ---: | ---: | ---: | ---: |
| HDHP | 448 | 1416 | 3.16 | $5,494 |
| PPO | 473 | 1428 | 3.02 | $4,482 |
| EPO | 478 | 1457 | 3.05 | $4,109 |
| HMO | 466 | 1419 | 3.05 | $3,554 |

## Members with repeated denials

Synthetic member ids with the most denied claims. Illustrative only: the data is random, so this shows the report shape, not a real pattern.

| Member | Claims | Denied | Denial rate |
| --- | ---: | ---: | ---: |
| MBR-1168 | 5 | 4 | 80.0% |
| MBR-0961 | 9 | 4 | 44.4% |
| MBR-1023 | 3 | 3 | 100.0% |
| MBR-0825 | 4 | 3 | 75.0% |
| MBR-0912 | 4 | 3 | 75.0% |

## Allowed-to-billed ratio by procedure

Lowest ratios first (non-denied claims, procedures with enough volume). A lower ratio means a bigger gap between billed charges and the allowed amount. Synthetic and illustrative, not real contract rates.

| Procedure | Claims | Billed | Allowed | Allowed / billed |
| --- | ---: | ---: | ---: | ---: |
| 43239 | 503 | $1,032,649 | $791,975 | 76.7% |
| 27447 | 416 | $10,302,611 | $7,924,488 | 76.9% |
| 85025 | 494 | $26,419 | $20,428 | 77.3% |
| 99213 | 516 | $62,119 | $48,062 | 77.4% |
| 99214 | 503 | $84,212 | $65,243 | 77.5% |
| 70450 | 500 | $327,189 | $253,671 | 77.5% |

## Paid-amount concentration

Share of total paid (5720 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 58 | 17.0% |
| top 5% | 286 | 64.4% |
| top 10% | 572 | 85.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| out-of-network provider | 180 | 99285 (14%), 80053 (13%), 93000 (12%) |
| timely filing exceeded | 180 | 99213 (13%), 93000 (13%), 97110 (11%) |
| not medically necessary | 178 | 43239 (14%), 99285 (13%), 93000 (12%) |

## Data quality gates

10 of 10 checks passed on this run.

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
| service month concentration | 0 | pass |

## Top procedures by paid amount

| Code | Claims | Avg billed | Paid | Denial rate |
| --- | ---: | ---: | ---: | ---: |
| 27447 | 479 | $24,772 | $6,739,746 | 13.2% |
| 43239 | 580 | $2,045 | $667,820 | 13.3% |
| 99285 | 613 | $1,059 | $368,098 | 14.4% |
| 70450 | 567 | $650 | $214,292 | 11.8% |
| 99214 | 573 | $168 | $55,465 | 12.2% |

## Member utilization

1083 of 1865 synthetic members have 3+ claims and account for 80.7% of paid dollars.

| Member | Claims | Paid |
| --- | ---: | ---: |
| MBR-1200 | 12 | $1,453 |
| MBR-0124 | 10 | $16,536 |
| MBR-0136 | 9 | $4,111 |
| MBR-0961 | 9 | $3,263 |
| MBR-0154 | 8 | $27,766 |

## Top denial reason by plan

| Plan | Denials | Top reason | Count |
| --- | ---: | --- | ---: |
| EPO | 195 | out-of-network provider | 49 |
| HDHP | 180 | missing prior authorization | 48 |
| HMO | 201 | not medically necessary | 51 |
| PPO | 172 | not medically necessary | 45 |

## Member denial experience

Members with 3+ claims (1083). Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.

| Denials | Members | Share |
| --- | ---: | ---: |
| no denials | 632 | 58.4% |
| 1 denial | 341 | 31.5% |
| 2+ denials | 110 | 10.2% |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 973 | 107 | 11.0% | missing prior authorization |
| 18-29 | 882 | 114 | 12.9% | not medically necessary |
| 30-44 | 970 | 134 | 13.8% | not medically necessary |
| 45-59 | 940 | 127 | 13.5% | out-of-network provider |
| 60-74 | 991 | 119 | 12.0% | not medically necessary |
| 75+ | 964 | 147 | 15.2% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1138.3% | +1121.2% | +3.69 pp |
| 2026-09 | +204.8% | +196.1% | +1.16 pp |
| 2026-10 | +0.6% | -9.6% | +0.60 pp |

## Potential duplicate services

129 groups share a member, procedure and service date (review queue, not a quality failure).

| Member | Procedure | Date | Claims | Paid |
| --- | --- | --- | ---: | ---: |
| MBR-1973 | 27447 | 2026-10-13 | 3 | $55,302 |
| MBR-0743 | 27447 | 2026-08-29 | 2 | $54,807 |
| MBR-0076 | 27447 | 2026-10-19 | 2 | $35,616 |
| MBR-0200 | 27447 | 2026-11-02 | 2 | $35,600 |
| MBR-1150 | 27447 | 2026-08-30 | 2 | $33,395 |

## Cost by age band

![Average paid by age band](age_band_costs.png)

![Monthly billed vs paid](monthly_financials.png)

![Denial reasons](denial_reasons.png)

Synthetic data generated by `healthdata.claims.ClaimGenerator`. Codes, plan types and payment rules are illustrative examples, not authoritative coding or adjudication logic. Not medical, financial or insurance advice.
