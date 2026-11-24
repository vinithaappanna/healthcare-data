# Healthcare Data - claims pipeline report

Generated 2026-11-24 05:40 UTC. All data is synthetic - no real member, patient or plan information.

**5480 claims** in store. Billed $13,777,409, paid $7,893,535, denied 715 overall.

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
| 2026-08 | 568 | $1,510,897 | $1,157,512 | $845,920 | 12.2% |
| 2026-09 | 1684 | $4,225,822 | $3,248,306 | $2,478,555 | 13.7% |
| 2026-10 | 1708 | $3,986,767 | $3,031,043 | $2,263,260 | 13.6% |
| 2026-11 | 1166 | $3,152,413 | $2,381,353 | $1,727,437 | 12.7% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.8% |
| 2026-01 | 31 | 0.6% |
| 2026-02 | 32 | 0.6% |
| 2026-03 | 45 | 0.8% |
| 2026-04 | 48 | 0.9% |
| 2026-05 | 43 | 0.8% |
| 2026-06 | 46 | 0.8% |
| 2026-07 | 47 | 0.9% |
| 2026-08 | 568 | 10.4% |
| 2026-09 | 1684 | 30.7% |
| 2026-10 (largest) | 1708 | 31.2% |
| 2026-11 | 1166 | 21.3% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 957 | $2,685 | $1,485,228 | 12.8% |
| Z00.00 | General adult medical exam | 715 | $2,986 | $1,343,980 | 13.3% |
| R51 | Headache | 993 | $2,532 | $1,331,731 | 13.9% |
| J06.9 | Acute upper respiratory infection | 951 | $2,387 | $1,272,049 | 12.6% |
| M54.5 | Low back pain | 944 | $2,309 | $1,261,770 | 12.7% |
| E11.9 | Type 2 diabetes without complications | 920 | $2,292 | $1,198,777 | 13.0% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 118 | 8.5% | $6,784 |
| M54.5 | 99285 | 115 | 16.5% | $69,208 |
| R51 | 80053 | 114 | 12.3% | $5,437 |
| J06.9 | 93000 | 109 | 15.6% | $6,184 |
| R51 | 43239 | 109 | 17.4% | $118,799 |
| M54.5 | 80053 | 108 | 12.0% | $4,854 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4219 | 77.0% | $10,404,697 | $6,828,821 |
| adjusted | 545 | 10.0% | $1,670,209 | $1,064,714 |
| denied | 716 | 13.1% | $1,702,503 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 69 | not medically necessary | 29.0% |
| 2026-09 | 231 | missing prior authorization | 27.3% |
| 2026-10 | 233 | missing prior authorization | 26.2% |
| 2026-11 | 148 | not medically necessary | 25.0% |

## Denial reasons

- not medically necessary (175)
- out-of-network provider (171)
- timely filing exceeded (171)
- missing prior authorization (169)
- duplicate claim (30)

## Plan mix

- EPO: 1387
- PPO: 1377
- HMO: 1366
- HDHP: 1350

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1387 | 13.5% | 56.2% |
| PPO | 1377 | 12.1% | 54.8% |
| HMO | 1366 | 14.4% | 56.5% |
| HDHP | 1350 | 12.2% | 61.3% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1169 | 22.5% | 15.7% |
| PPO | 1210 | 24.2% | 15.4% |
| HDHP | 1185 | 22.2% | 14.7% |
| EPO | 1200 | 23.5% | 14.3% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 169 | $495,816 | 29.1% | $2,934 |
| not medically necessary | 175 | $449,801 | 26.4% | $2,570 |
| timely filing exceeded | 171 | $397,974 | 23.4% | $2,327 |
| out-of-network provider | 171 | $270,578 | 15.9% | $1,582 |
| duplicate claim | 30 | $88,335 | 5.2% | $2,944 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 124 (133 later claims)
- Later claims denied as duplicate: 30
- Later claims still paid: 93 ($208,931 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 356 | 19.3% | $350,010 | 4.4% |
| 2 claims | 462 | 25.0% | $1,209,095 | 15.3% |
| 3 claims | 418 | 22.6% | $1,993,201 | 25.2% |
| 4+ claims | 612 | 33.1% | $4,341,228 | 55.0% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1590 | 29.0% | $62,585 | 0.8% | 12.6% |
| $100-$999 | 2549 | 46.5% | $461,219 | 5.8% | 13.4% |
| $1,000-$9,999 | 884 | 16.1% | $871,403 | 11.0% | 13.5% |
| $10,000+ | 457 | 8.3% | $6,498,328 | 82.3% | 12.0% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,480 | 5,480 | yes |
| claims: plan mix | 5,480 | 5,480 | yes |
| claims: plan performance | 5,480 | 5,480 | yes |
| claims: age bands | 5,480 | 5,480 | yes |
| claims: cost per member | 5,480 | 5,480 | yes |
| paid $: monthly view | 7,893,534.68 | 7,893,534.68 | yes |
| paid $: age bands | 7,893,528.47 | 7,893,534.68 | yes |
| denied claims: reasons | 716 | 716 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 343 |
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
| HDHP | 447 | 1350 | 3.02 | $5,226 |
| PPO | 466 | 1377 | 2.95 | $4,466 |
| EPO | 472 | 1387 | 2.94 | $3,946 |
| HMO | 463 | 1366 | 2.95 | $3,486 |

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
| 43239 | 478 | $978,315 | $751,299 | 76.8% |
| 27447 | 402 | $9,936,273 | $7,634,651 | 76.8% |
| 85025 | 470 | $25,033 | $19,317 | 77.2% |
| 70450 | 472 | $309,375 | $239,468 | 77.4% |
| 99213 | 495 | $59,653 | $46,173 | 77.4% |
| 99285 | 507 | $541,335 | $419,476 | 77.5% |

## Paid-amount concentration

Share of total paid (5480 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 55 | 16.7% |
| top 5% | 274 | 64.2% |
| top 10% | 548 | 85.7% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| not medically necessary | 175 | 43239 (14%), 99285 (13%), 93000 (12%) |
| out-of-network provider | 171 | 99285 (13%), 80053 (13%), 93000 (13%) |
| timely filing exceeded | 171 | 93000 (13%), 99213 (13%), 80053 (11%) |

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
| 27447 | 457 | $24,760 | $6,498,328 | 12.0% |
| 43239 | 554 | $2,037 | $633,695 | 13.7% |
| 99285 | 593 | $1,059 | $355,594 | 14.5% |
| 70450 | 536 | $651 | $202,172 | 11.9% |
| 99214 | 556 | $168 | $53,852 | 12.2% |

## Member utilization

1030 of 1848 synthetic members have 3+ claims and account for 80.2% of paid dollars.

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
| EPO | 187 | out-of-network provider | 47 |
| HDHP | 165 | missing prior authorization | 45 |
| HMO | 197 | not medically necessary | 51 |
| PPO | 167 | not medically necessary | 45 |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1108.5% | +1083.8% | +3.64 pp |
| 2026-09 | +196.5% | +193.0% | +1.57 pp |
| 2026-10 | +1.4% | -8.7% | -0.08 pp |

## Potential duplicate services

124 groups share a member, procedure and service date (review queue, not a quality failure).

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
