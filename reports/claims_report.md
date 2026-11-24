# Healthcare Data - claims pipeline report

Generated 2026-11-24 10:44 UTC. All data is synthetic - no real member, patient or plan information.

**5600 claims** in store. Billed $14,101,053, paid $8,036,359, denied 729 overall.

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
| 2026-08 | 572 | $1,514,231 | $1,160,009 | $847,822 | 12.1% |
| 2026-09 | 1733 | $4,375,858 | $3,358,812 | $2,534,490 | 13.6% |
| 2026-10 | 1743 | $4,045,665 | $3,076,325 | $2,289,793 | 13.7% |
| 2026-11 | 1198 | $3,263,788 | $2,469,381 | $1,785,891 | 12.6% |

## Service-date distribution

Share of stored claims per service month. Generator-shaped: new batches spread dates over 90 days and older single-date batches were redistributed, so months before the spread are thin backfill. A quality gate caps any month at 50%.

| Month | Claims | Share |
| --- | ---: | ---: |
| 2025-11 | 18 | 0.3% |
| 2025-12 | 44 | 0.8% |
| 2026-01 | 31 | 0.5% |
| 2026-02 | 32 | 0.6% |
| 2026-03 | 45 | 0.8% |
| 2026-04 | 48 | 0.9% |
| 2026-05 | 43 | 0.8% |
| 2026-06 | 46 | 0.8% |
| 2026-07 | 47 | 0.8% |
| 2026-08 | 572 | 10.2% |
| 2026-09 | 1733 | 30.9% |
| 2026-10 (largest) | 1743 | 31.1% |
| 2026-11 | 1198 | 21.4% |

## Top diagnoses by paid amount

Illustrative code list, not authoritative coding; synthetic data.

| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |
| --- | --- | ---: | ---: | ---: | ---: |
| I10 | Essential hypertension | 979 | $2,635 | $1,491,774 | 12.6% |
| R51 | Headache | 1011 | $2,559 | $1,380,878 | 13.7% |
| Z00.00 | General adult medical exam | 731 | $3,033 | $1,366,051 | 13.5% |
| J06.9 | Acute upper respiratory infection | 975 | $2,439 | $1,305,331 | 12.8% |
| M54.5 | Low back pain | 964 | $2,278 | $1,271,489 | 12.7% |
| E11.9 | Type 2 diabetes without complications | 940 | $2,281 | $1,220,836 | 13.1% |

## Most common diagnosis/procedure pairs

Pairs come from independent synthetic draws: this shows the generator's mix, not clinical practice. Illustrative codes.

| Diagnosis | Procedure | Claims | Denial rate | Paid |
| --- | --- | ---: | ---: | ---: |
| R51 | 93000 | 121 | 8.3% | $6,994 |
| M54.5 | 99285 | 116 | 16.4% | $70,070 |
| R51 | 80053 | 116 | 12.1% | $5,523 |
| J06.9 | 93000 | 113 | 15.9% | $6,332 |
| M54.5 | 80053 | 109 | 11.9% | $4,905 |
| R51 | 43239 | 109 | 17.4% | $118,799 |

## Claim status breakdown

| Status | Claims | Share | Billed | Paid |
| --- | ---: | ---: | ---: | ---: |
| paid | 4317 | 77.1% | $10,626,595 | $6,968,273 |
| adjusted | 553 | 9.9% | $1,675,351 | $1,068,087 |
| denied | 730 | 13.0% | $1,799,106 | $0 |

## Leading denial reason by month

Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.

| Month | Denials | Leading reason | Share of denials |
| --- | ---: | --- | ---: |
| 2026-08 | 69 | not medically necessary | 29.0% |
| 2026-09 | 236 | missing prior authorization | 27.1% |
| 2026-10 | 239 | missing prior authorization | 26.4% |
| 2026-11 | 151 | not medically necessary | 24.5% |

## Denial reasons

- not medically necessary (176)
- out-of-network provider (175)
- timely filing exceeded (175)
- missing prior authorization (173)
- duplicate claim (31)

## Plan mix

- EPO: 1421
- PPO: 1400
- HMO: 1394
- HDHP: 1385

## Plan performance

| Plan | Claims | Denial rate | Paid / billed |
| --- | ---: | ---: | ---: |
| EPO | 1421 | 13.4% | 55.3% |
| PPO | 1400 | 12.1% | 54.9% |
| HMO | 1394 | 14.1% | 56.5% |
| HDHP | 1385 | 12.6% | 61.0% |

![Denial rate by plan type](plan_denial_rates.png)

## Cost sharing by plan (non-denied claims)

Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. Illustrative synthetic rules, not real benefit design.

| Plan | Claims | Network discount | Member cost share |
| --- | ---: | ---: | ---: |
| HMO | 1197 | 22.5% | 15.7% |
| PPO | 1231 | 24.2% | 15.4% |
| HDHP | 1211 | 22.2% | 14.7% |
| EPO | 1231 | 23.5% | 14.6% |

## Denial-rate outliers (plan x month)

Cells whose denial rate is at least 2 standard errors from the overall rate (cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

No plan/month cells outside the screen.

## Denied dollars by reason

Billed amount on denied claims. A reason with few claims can still carry a large share when it lands on expensive procedures. Synthetic, illustrative.

| Reason | Claims | Billed | Share | Avg billed |
| --- | ---: | ---: | ---: | ---: |
| missing prior authorization | 173 | $496,552 | 27.6% | $2,870 |
| not medically necessary | 176 | $466,354 | 25.9% | $2,650 |
| timely filing exceeded | 175 | $424,919 | 23.6% | $2,428 |
| out-of-network provider | 175 | $322,815 | 17.9% | $1,845 |
| duplicate claim | 31 | $88,466 | 4.9% | $2,854 |

## Duplicate-claim leakage screen

In each same member/procedure/date group the first claim is the original. A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.

- Groups with repeats: 126 (135 later claims)
- Later claims denied as duplicate: 31
- Later claims still paid: 94 ($209,028 to review)
- Claims denied as duplicate with no matching original: 0

## Members by number of claims

How many claims each synthetic member has, and where paid dollars sit. Members with no claims are not visible (no enrollment data). Illustrative.

| Claims per member | Members | % of members | Paid | % of paid |
| --- | ---: | ---: | ---: | ---: |
| 1 claim | 340 | 18.3% | $315,559 | 3.9% |
| 2 claims | 457 | 24.6% | $1,245,077 | 15.5% |
| 3 claims | 429 | 23.1% | $2,001,006 | 24.9% |
| 4+ claims | 630 | 33.9% | $4,474,718 | 55.7% |

## Claims by billed-amount band

Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.

![Claims vs paid by billed band](size_bands.png)

| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| under $100 | 1626 | 29.0% | $64,123 | 0.8% | 12.6% |
| $100-$999 | 2603 | 46.5% | $473,322 | 5.9% | 13.4% |
| $1,000-$9,999 | 903 | 16.1% | $895,291 | 11.1% | 13.2% |
| $10,000+ | 468 | 8.4% | $6,603,623 | 82.2% | 12.6% |

## Aggregate reconciliation

Every view accounts for the whole store.

| Check | View | Store | Match |
| --- | ---: | ---: | :---: |
| claims: monthly view | 5,600 | 5,600 | yes |
| claims: plan mix | 5,600 | 5,600 | yes |
| claims: plan performance | 5,600 | 5,600 | yes |
| claims: age bands | 5,600 | 5,600 | yes |
| claims: cost per member | 5,600 | 5,600 | yes |
| paid $: monthly view | 8,036,359.43 | 8,036,359.43 | yes |
| paid $: age bands | 8,036,369.0 | 8,036,359.43 | yes |
| denied claims: reasons | 730 | 730 | yes |

## Data provenance

`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are older synthetic history that was repaired in place (one plan and age band per member, no age-implausible procedure or diagnosis, and "duplicate claim" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the current rules. Tagged counts are conservative, not an exact count of changed rows: the whole B05 batch is tagged even if a few of its rows already matched. Plan and age band are labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks service dates redistributed over the trailing 90 days (only service_date moved; see docs/service-date-redistribution.md). All of it is synthetic.

| Origin | Claims |
| --- | ---: |
| generated | 463 |
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
| HDHP | 448 | 1385 | 3.09 | $5,338 |
| PPO | 469 | 1400 | 2.99 | $4,448 |
| EPO | 475 | 1421 | 2.99 | $4,067 |
| HMO | 464 | 1394 | 3.00 | $3,506 |

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
| 43239 | 492 | $1,009,277 | $774,868 | 76.8% |
| 27447 | 409 | $10,105,614 | $7,764,907 | 76.8% |
| 85025 | 479 | $25,615 | $19,761 | 77.1% |
| 99213 | 503 | $60,559 | $46,872 | 77.4% |
| 99214 | 497 | $83,119 | $64,353 | 77.4% |
| 70450 | 491 | $321,407 | $248,946 | 77.5% |

## Paid-amount concentration

Share of total paid (5600 claims) held by the largest claims. Synthetic data, illustrative.

![Paid concentration curve](paid_concentration.png)

| Top claims | Count | Share of paid |
| --- | ---: | ---: |
| top 1% | 56 | 16.7% |
| top 5% | 280 | 64.2% |
| top 10% | 560 | 85.6% |

## Procedures behind the top denial reasons

| Denial reason | Denials | Top procedures (share of that reason) |
| --- | ---: | --- |
| not medically necessary | 176 | 43239 (14%), 99285 (13%), 93000 (12%) |
| out-of-network provider | 175 | 80053 (13%), 99285 (13%), 93000 (13%) |
| timely filing exceeded | 175 | 93000 (13%), 99213 (13%), 97110 (11%) |

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
| 27447 | 468 | $24,744 | $6,603,623 | 12.6% |
| 43239 | 568 | $2,042 | $653,417 | 13.4% |
| 99285 | 601 | $1,059 | $361,470 | 14.3% |
| 70450 | 556 | $650 | $210,287 | 11.7% |
| 99214 | 565 | $168 | $54,732 | 12.0% |

## Member utilization

1059 of 1856 synthetic members have 3+ claims and account for 80.6% of paid dollars.

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
| EPO | 190 | out-of-network provider | 48 |
| HDHP | 174 | missing prior authorization | 48 |
| HMO | 197 | not medically necessary | 51 |
| PPO | 169 | not medically necessary | 45 |

## Denials by age band

Age band is a synthetic per-member label with no clinical or benefit realism; differences come from the generator's random draws.

| Age band | Claims | Denied | Denial rate | Top reason |
| --- | ---: | ---: | ---: | --- |
| 0-17 | 958 | 106 | 11.1% | missing prior authorization |
| 18-29 | 861 | 108 | 12.5% | not medically necessary |
| 30-44 | 945 | 130 | 13.8% | not medically necessary |
| 45-59 | 923 | 124 | 13.4% | out-of-network provider |
| 60-74 | 970 | 118 | 12.2% | not medically necessary |
| 75+ | 943 | 144 | 15.3% | missing prior authorization |

## Month-over-month trend (last 6 complete months)

Monthly counts here are shaped by the synthetic generator (daily batches spread service dates over the trailing 90 days; months before that are a sparse backfill), not evidence of utilization trends.

| Month | Claims | Paid | Denial rate |
| --- | ---: | ---: | ---: |
| 2026-05 | -10.4% | +48.8% | +3.30 pp |
| 2026-06 | +7.0% | +7.8% | +3.59 pp |
| 2026-07 | +2.2% | -41.4% | -6.71 pp |
| 2026-08 | +1117.0% | +1086.4% | +3.55 pp |
| 2026-09 | +203.0% | +198.9% | +1.56 pp |
| 2026-10 | +0.6% | -9.7% | +0.09 pp |

## Potential duplicate services

126 groups share a member, procedure and service date (review queue, not a quality failure).

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
