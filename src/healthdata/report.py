"""Render the markdown report and charts from pipeline marts."""
from __future__ import annotations

import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


MONTH_NOTE = ("Monthly counts here are shaped by the synthetic generator (daily batches spread service "
              "dates over the trailing 90 days; months before that are a sparse backfill), not evidence "
              "of utilization trends.")


def render_markdown(monthly: list[dict], denial_reasons: list[tuple[str, int]],
                    plan_mix: list[tuple[str, int]], total_claims: int,
                    generated_at: dt.datetime | None = None,
                    plan_perf: list[dict] | None = None,
                    procedures: list[dict] | None = None,
                    utilization: dict | None = None,
                    age_bands: list[dict] | None = None,
                    reasons_by_plan: dict | None = None,
                    duplicates: list[dict] | None = None,
                    trend: list[dict] | None = None,
                    cost_sharing: list[dict] | None = None,
                    independence: dict | None = None,
                    status_ratios: list[dict] | None = None,
                    denial_cats: list[dict] | None = None,
                    plan_denied_dollars: list[dict] | None = None,
                    outliers: list[dict] | None = None,
                    concentration: dict | None = None,
                    gates: list[tuple[str, int]] | None = None,
                    denial_procs: list[dict] | None = None,
                    discounts: list[dict] | None = None,
                    denied_dollars: list[dict] | None = None,
                    repeat_denials: list[dict] | None = None,
                    per_member: list[dict] | None = None,
                    origins: dict | None = None,
                    reconciliation: list[dict] | None = None,
                    size_bands: list[dict] | None = None,
                    dup_leakage: dict | None = None,
                    member_dist: list[dict] | None = None,
                    statuses: list[dict] | None = None,
                    diagnoses: list[dict] | None = None,
                    dx_proc_pairs: list[dict] | None = None,
                    reasons_by_month: list[dict] | None = None,
                    month_dist: list[dict] | None = None,
                    age_denials: list[dict] | None = None,
                    member_denials: dict | None = None,
                    plan_intervals: list[dict] | None = None,
                    plan_age: dict | None = None,
                    proc_screen: dict | None = None) -> str:
    generated_at = generated_at or dt.datetime.now(dt.timezone.utc)
    total_paid = sum(m["paid"] for m in monthly)
    total_billed = sum(m["billed"] for m in monthly)
    denied = sum(m["denial_rate"] * m["claims"] for m in monthly)
    lines = [
        "# Healthcare Data - claims pipeline report",
        "",
        f"Generated {generated_at:%Y-%m-%d %H:%M} UTC. "
        "All data is synthetic - no real member, patient or plan information.",
        "",
        f"**{total_claims} claims** in store. "
        f"Billed ${total_billed:,.0f}, paid ${total_paid:,.0f}, "
        f"denied {int(denied)} overall.",
        "",
        "## Monthly financials",
        "",
        MONTH_NOTE,
        "",
        "| Month | Claims | Billed | Allowed | Paid | Denial rate |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for m in monthly:
        lines.append(
            f"| {m['month']} | {m['claims']} | ${m['billed']:,.0f} | "
            f"${m['allowed']:,.0f} | ${m['paid']:,.0f} | {m['denial_rate']:.1%} |"
        )
    if month_dist:
        lines += ["", "## Service-date distribution", "",
                  "Share of stored claims per service month. Generator-shaped: new batches spread dates over "
                  "90 days and older single-date batches were redistributed, so months before the spread are thin "
                  "backfill. A quality gate caps any month at 50%.", "",
                  "| Month | Claims | Share |", "| --- | ---: | ---: |"]
        for m in month_dist:
            star = " (largest)" if m["largest"] else ""
            lines.append(f"| {m['month']}{star} | {m['claims']} | {m['share']:.1%} |")
    if diagnoses:
        lines += ["", "## Top diagnoses by paid amount", "",
                  "Illustrative code list, not authoritative coding; synthetic data.", "",
                  "| Diagnosis | Description | Claims | Avg billed | Paid | Denial rate |",
                  "| --- | --- | ---: | ---: | ---: | ---: |"]
        for d in diagnoses:
            lines.append(f"| {d['code']} | {d['description']} | {d['claims']} | "
                         f"${d['avg_billed']:,.0f} | ${d['paid']:,.0f} | {d['denial_rate']:.1%} |")
    if dx_proc_pairs:
        lines += ["", "## Most common diagnosis/procedure pairs", "",
                  "Pairs come from independent synthetic draws: this shows the generator's mix, "
                  "not clinical practice. Illustrative codes.", "",
                  "| Diagnosis | Procedure | Claims | Denial rate | Paid |",
                  "| --- | --- | ---: | ---: | ---: |"]
        for d in dx_proc_pairs:
            lines.append(f"| {d['diagnosis']} | {d['procedure']} | {d['claims']} | "
                         f"{d['denial_rate']:.1%} | ${d['paid']:,.0f} |")
    if statuses:
        lines += ["", "## Claim status breakdown", "",
                  "| Status | Claims | Share | Billed | Paid |", "| --- | ---: | ---: | ---: | ---: |"]
        for st in statuses:
            lines.append(f"| {st['status']} | {st['claims']} | {st['share']:.1%} | "
                         f"${st['billed']:,.0f} | ${st['paid']:,.0f} |")
    if reasons_by_month:
        lines += ["", "## Leading denial reason by month", "",
                  "Months with fewer than 10 denials are omitted. Most synthetic claims fall in the latest service month, so older months are sparse. Synthetic data.", "",
                  "| Month | Denials | Leading reason | Share of denials |",
                  "| --- | ---: | --- | ---: |"]
        for m in reasons_by_month:
            lines.append(f"| {m['month']} | {m['denials']} | {m['top_reason']} | {m['top_share']:.1%} |")
    lines += ["", "## Denial reasons", ""]
    for reason, count in denial_reasons:
        lines.append(f"- {reason} ({count})")
    lines += ["", "## Plan mix", ""]
    for plan, count in plan_mix:
        lines.append(f"- {plan}: {count}")
    if plan_perf:
        lines += ["", "## Plan performance", "",
                  "| Plan | Claims | Denial rate | Paid / billed |",
                  "| --- | ---: | ---: | ---: |"]
        for r in plan_perf:
            lines.append(f"| {r['plan']} | {r['claims']} | {r['denial_rate']:.1%} | "
                         f"{r['paid_to_billed']:.1%} |")
        lines += ["", "![Denial rate by plan type](plan_denial_rates.png)"]
    if cost_sharing:
        lines += ["", "## Cost sharing by plan (non-denied claims)", "",
                  "Network discount = 1 - allowed/billed. Member cost share = (allowed - paid)/allowed. "
                  "Illustrative synthetic rules, not real benefit design.", "",
                  "| Plan | Claims | Network discount | Member cost share |",
                  "| --- | ---: | ---: | ---: |"]
        for r in cost_sharing:
            lines.append(f"| {r['plan']} | {r['claims']} | {r['network_discount']:.1%} | "
                         f"{r['member_cost_share']:.1%} |")
    if independence and "chi2" in independence:
        i = independence
        lines += ["", "## Plan vs denial: independence test", "",
                  f"Chi-square test of plan type against denied/not denied over {i['claims']} claims: "
                  f"chi2 = {i['chi2']}, df = {i['df']}, p = {i['p_value']}. Plan is a synthetic label drawn independently of "
                  "denial status, so a small p-value would point to a generator or data problem, not real plan behavior. "
                  "A large p-value is the expected result and is not evidence of fairness or equal treatment."]
    if plan_denied_dollars:
        lines += ["", "## Denied dollars by plan", "",
                  "Denial rate counts claims; denied-dollar share is billed dollars on denied claims over all billed dollars. "
                  "A dollar share below the claim rate means denials fall on cheaper claims. Plan is a synthetic label only.", "",
                  "| Plan | Claims | Denial rate | Denied billed ($) | Denied-dollar share |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for r in plan_denied_dollars:
            lines.append(f"| {r['plan']} | {r['claims']} | {r['denial_rate']:.1%} | "
                         f"{r['denied_billed']:,.2f} | {r['denied_dollar_share']:.1%} |")
    if denial_cats:
        lines += ["", "## Denials by broad category", "",
                  "Denial reasons grouped with a simplified teaching taxonomy (not an industry standard, not coding advice). "
                  "Illustrative synthetic data: reasons are drawn by the generator, so the mix says nothing about real payers.", "",
                  "| Category | Denied claims | Share | Billed ($) |", "| --- | ---: | ---: | ---: |"]
        for r in denial_cats:
            lines.append(f"| {r['category']} | {r['claims']} | {r['share']:.1%} | {r['billed']:,.2f} |")
        lines += ["", "![Denials by broad category](denial_categories.png)"]
    if status_ratios:
        lines += ["", "## Payment ratios by claim status", "",
                  "Mean claim-level paid/allowed and allowed/billed among claims with a positive allowed amount. "
                  "In this synthetic generator 'adjusted' is only a status label with no separate adjustment logic, so "
                  "it is expected to match 'paid'. Denied claims pay zero; most still carry a nominal allowed amount from the generator (duplicate denials carry none), so their allowed/billed is not a payer decision.", "",
                  "| Status | Claims | Priced | Paid/allowed | Allowed/billed |", "| --- | ---: | ---: | ---: | ---: |"]
        for r in status_ratios:
            lines.append(f"| {r['status']} | {r['claims']} | {r['priced']} | {r['paid_to_allowed']:.1%} | {r['allowed_to_billed']:.1%} |")
    if outliers is not None:
        lines += ["", "## Denial-rate outliers (plan x month)", "",
                  "Cells whose denial rate is at least 2 standard errors from the overall rate "
                  "(cells under 20 claims skipped). A statistical screen on synthetic data, not a finding. " + MONTH_NOTE]
        if outliers:
            lines += ["", "| Plan | Month | Claims | Denial rate | Overall | z |",
                      "| --- | --- | ---: | ---: | ---: | ---: |"]
            for o in outliers:
                lines.append(f"| {o['plan']} | {o['month']} | {o['claims']} | {o['denial_rate']:.1%} | "
                             f"{o['overall_rate']:.1%} | {o['z']:+.2f} |")
        else:
            lines += ["", "No plan/month cells outside the screen."]
    if denied_dollars:
        lines += ["", "## Denied dollars by reason", "",
                  "Billed amount on denied claims. A reason with few claims can still "
                  "carry a large share when it lands on expensive procedures. Synthetic, illustrative.", "",
                  "| Reason | Claims | Billed | Share | Avg billed |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for d in denied_dollars:
            lines.append(f"| {d['reason']} | {d['claims']} | ${d['billed']:,.0f} | "
                         f"{d['share']:.1%} | ${d['avg_billed']:,.0f} |")
    if dup_leakage and (dup_leakage["groups"] or dup_leakage["unsupported_duplicate_denials"]):
        d = dup_leakage
        lines += ["", "## Duplicate-claim leakage screen", "",
                  "In each same member/procedure/date group the first claim is the original. "
                  "A review queue, not proof: repeat services can be legitimate. In this synthetic data older repeats are "
                  "chance collisions of random fields (mostly paid), while newer batches add deliberate repeats, "
                  "most denied as duplicate and some paid. Illustrative, not real payment-integrity rates.", "",
                  f"- Groups with repeats: {d['groups']} ({d['later_claims']} later claims)",
                  f"- Later claims denied as duplicate: {d['caught']}",
                  f"- Later claims still paid: {d['leaked_claims']} (${d['leaked_paid']:,.0f} to review)",
                  f"- Claims denied as duplicate with no matching original: {d['unsupported_duplicate_denials']}"]
    if member_dist and any(b["members"] for b in member_dist):
        lines += ["", "## Members by number of claims", "",
                  "How many claims each synthetic member has, and where paid dollars sit. "
                  "Members with no claims are not visible (no enrollment data). Illustrative.", "",
                  "| Claims per member | Members | % of members | Paid | % of paid |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for b in member_dist:
            lines.append(f"| {b['bucket']} | {b['members']} | {b['member_share']:.1%} | "
                         f"${b['paid']:,.0f} | {b['paid_share']:.1%} |")
    if size_bands and any(b["claims"] for b in size_bands):
        lines += ["", "## Claims by billed-amount band", "",
                  "Share of claims versus share of paid dollars. Band edges are illustrative; synthetic data.", "",
                  "![Claims vs paid by billed band](size_bands.png)", "",
                  "| Billed band | Claims | % of claims | Paid | % of paid | Denial rate |",
                  "| --- | ---: | ---: | ---: | ---: | ---: |"]
        for b in size_bands:
            lines.append(f"| {b['band']} | {b['claims']} | {b['claim_share']:.1%} | ${b['paid']:,.0f} | "
                         f"{b['paid_share']:.1%} | {b['denial_rate']:.1%} |")
    if reconciliation:
        bad = [r for r in reconciliation if not r["ok"]]
        lines += ["", "## Aggregate reconciliation", "",
                  ("Every view accounts for the whole store." if not bad else
                   f"**{len(bad)} view(s) do not match the store.**"), "",
                  "| Check | View | Store | Match |", "| --- | ---: | ---: | :---: |"]
        for r in reconciliation:
            lines.append(f"| {r['check']} | {r['view']:,} | {r['store']:,} | {'yes' if r['ok'] else '**NO**'} |")
    if origins and any(k != "generated" for k in origins):
        lines += ["", "## Data provenance", "",
                  "`data_origin` marks how each stored claim came to be. Rows tagged `regenerated-*` are "
                  "older synthetic history that was repaired in place (one plan and age band per member, "
                  "no age-implausible procedure or diagnosis, and \"duplicate claim\" denials without an earlier matching claim given another reason; a `+2026-11-22` suffix marks the second repair); `generated` rows were produced under the "
                  "current rules. Tagged counts are conservative, not an exact count of changed rows: the whole "
                  "B05 batch is tagged even if a few of its rows already matched. Plan and age band are "
                  "labels only, with no plan-specific benefits or clinical realism. A `+2026-11-23` suffix marks "
                  "service dates redistributed over the trailing 90 days (only service_date moved; see "
                  "docs/service-date-redistribution.md). All of it is synthetic.", "",
                  "| Origin | Claims |", "| --- | ---: |"]
        for k, n in origins.items():
            lines.append(f"| {k} | {n} |")
    if per_member:
        lines += ["", "## Cost per member by plan", "",
                  "Distinct synthetic members, claims and paid dollars per member in the store. "
                  "Not a true PMPM: there is no enrollment data. Illustrative only.", "",
                  "| Plan | Members | Claims | Claims / member | Paid / member |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for d in per_member:
            lines.append(f"| {d['plan']} | {d['members']} | {d['claims']} | "
                         f"{d['claims_per_member']:.2f} | ${d['paid_per_member']:,.0f} |")
    if repeat_denials:
        lines += ["", "## Members with repeated denials", "",
                  "Synthetic member ids with the most denied claims. Illustrative only: "
                  "the data is random, so this shows the report shape, not a real pattern.", "",
                  "| Member | Claims | Denied | Denial rate |", "| --- | ---: | ---: | ---: |"]
        for d in repeat_denials:
            lines.append(f"| {d['member']} | {d['claims']} | {d['denied']} | {d['denial_rate']:.1%} |")
    if discounts:
        lines += ["", "## Allowed-to-billed ratio by procedure", "",
                  "Lowest ratios first (non-denied claims, procedures with enough volume). "
                  "A lower ratio means a bigger gap between billed charges and the allowed amount. "
                  "Synthetic and illustrative, not real contract rates.", "",
                  "| Procedure | Claims | Billed | Allowed | Allowed / billed |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for d in discounts:
            lines.append(f"| {d['procedure']} | {d['claims']} | ${d['billed']:,.0f} | "
                         f"${d['allowed']:,.0f} | {d['allowed_to_billed']:.1%} |")
    if concentration and concentration.get("tiers"):
        lines += ["", "## Paid-amount concentration", "",
                  f"Share of total paid ({concentration['claims']} claims) held by the largest claims. "
                  "Synthetic data, illustrative.", "",
                  "![Paid concentration curve](paid_concentration.png)", "",
                  "| Top claims | Count | Share of paid |", "| --- | ---: | ---: |"]
        for t in concentration["tiers"]:
            lines.append(f"| top {t['top_pct']:.0%} | {t['claims']} | {t['share_of_paid']:.1%} |")
        if concentration.get("gini") is not None:
            lines += ["", f"Gini coefficient of paid per claim: **{concentration['gini']:.3f}** "
                      "(0 = every claim paid the same, 1 = one claim holds all of it; denied claims count as 0)."]
    if denial_procs:
        lines += ["", "## Procedures behind the top denial reasons", "",
                  "| Denial reason | Denials | Top procedures (share of that reason) |",
                  "| --- | ---: | --- |"]
        for d in denial_procs:
            procs = ", ".join(f"{p['code']} ({p['share']:.0%})" for p in d["procedures"])
            lines.append(f"| {d['reason']} | {d['denials']} | {procs} |")
    if gates:
        failing = sum(1 for _n, c in gates if c)
        lines += ["", "## Data quality gates", "",
                  f"{len(gates) - failing} of {len(gates)} checks passed on this run.", "",
                  "| Check | Issues | Result |", "| --- | ---: | --- |"]
        for name, count in gates:
            lines.append(f"| {name} | {count} | {'pass' if not count else 'FAIL'} |")
    if procedures:
        lines += ["", "## Top procedures by paid amount", "",
                  "| Code | Claims | Avg billed | Paid | Denial rate |",
                  "| --- | ---: | ---: | ---: | ---: |"]
        for r in procedures:
            lines.append(f"| {r['code']} | {r['claims']} | ${r['avg_billed']:,.0f} | "
                         f"${r['paid']:,.0f} | {r['denial_rate']:.1%} |")
    if utilization and utilization.get("members_total"):
        lines += ["", "## Member utilization", "",
                  f"{utilization['high_utilizers']} of {utilization['members_total']} "
                  f"synthetic members have 3+ claims and account for "
                  f"{utilization['share_of_paid']:.1%} of paid dollars.", "",
                  "| Member | Claims | Paid |", "| --- | ---: | ---: |"]
        for r in utilization["top"]:
            lines.append(f"| {r['member_id']} | {r['claims']} | ${r['paid']:,.0f} |")
    if reasons_by_plan:
        lines += ["", "## Top denial reason by plan", "",
                  "| Plan | Denials | Top reason | Count |", "| --- | ---: | --- | ---: |"]
        for plan, reasons in reasons_by_plan.items():
            lines.append(f"| {plan} | {sum(c for _, c in reasons)} | {reasons[0][0]} | {reasons[0][1]} |")
    if plan_intervals:
        lines += ["", "## Plan denial rates with 95% intervals", "",
                  "Wilson score intervals. The generator draws denials at the same rate for every plan, so "
                  "overlap with the overall rate is expected; plan labels carry no benefit realism.", "",
                  "| Plan | Claims | Denial rate | 95% interval | Differs from overall |",
                  "| --- | ---: | ---: | --- | --- |"]
        for r in plan_intervals:
            lines.append(f"| {r['plan']} | {r['claims']} | {r['denial_rate']:.1%} | "
                         f"{r['low']:.1%} to {r['high']:.1%} | {'yes' if r['differs_from_overall'] else 'no'} |")
    if plan_age and plan_age["rows"]:
        lines += ["", "## Average paid per claim: plan x age band", "",
                  f"Denied claims count as 0; cells under {plan_age['min_claims']} claims show '-'. "
                  "Plan and age are synthetic labels with no benefit or clinical realism, so differences come from the generator (random draws, plus age-restricted procedures such as knee replacement, which lowers the 0-17 column).", "",
                  "| Plan | " + " | ".join(plan_age["bands"]) + " |",
                  "| --- |" + " ---: |" * len(plan_age["bands"])]
        for r in plan_age["rows"]:
            lines.append(f"| {r['plan']} | " + " | ".join("-" if v is None else f"${v:,.0f}" for v in r["avg_paid"]) + " |")
    if proc_screen and proc_screen["tested"]:
        lines += ["", "## Procedure denial-rate screen", "",
                  f"{proc_screen['tested']} procedure codes with {proc_screen['min_claims']}+ claims tested against the overall "
                  f"denial rate ({proc_screen['overall']:.1%}) using 95% Wilson intervals. With this many tests an occasional hit is "
                  "expected by chance, and the generator uses one denial rate for every code: leads for review, not findings."]
        if proc_screen["hits"]:
            lines += ["", "| Procedure | Claims | Denial rate | 95% interval | Gap vs overall |",
                      "| --- | ---: | ---: | --- | ---: |"]
            for h in proc_screen["hits"]:
                lines.append(f"| {h['procedure']} | {h['claims']} | {h['denial_rate']:.1%} | "
                             f"{h['low']:.1%} to {h['high']:.1%} | {h['gap_pp']:+.1f} pp |")
        else:
            lines += ["", "No procedure's interval excludes the overall rate."]
    if member_denials and member_denials["members"]:
        lines += ["", "## Member denial experience", "",
                  f"Members with {member_denials['min_claims']}+ claims ({member_denials['members']}). "
                  "Denials are random draws in the generator, so this is a profile of the synthetic data, not member behavior.", "",
                  "| Denials | Members | Share |", "| --- | ---: | ---: |"]
        for b in member_denials["buckets"]:
            lines.append(f"| {b['bucket']} | {b['members']} | {b['share']:.1%} |")
    if age_denials:
        lines += ["", "## Denials by age band", "",
                  "Age band is a synthetic per-member label with no clinical or benefit realism; "
                  "differences come from the generator's random draws.", "",
                  "| Age band | Claims | Denied | Denial rate | Top reason |",
                  "| --- | ---: | ---: | ---: | --- |"]
        for a in age_denials:
            lines.append(f"| {a['age_band']} | {a['claims']} | {a['denied']} | "
                         f"{a['denial_rate']:.1%} | {a['top_reason'] or '-'} |")
    if trend and len(trend) > 1:
        def fmt(v, suffix=""):
            return "-" if v is None else f"{v:+.1%}" if suffix == "%" else f"{v:+.2f} pp"
        lines += ["", "## Month-over-month trend (last 6 complete months)", "", MONTH_NOTE, "",
                  "| Month | Claims | Paid | Denial rate |", "| --- | ---: | ---: | ---: |"]
        for t in trend[-6:]:
            lines.append(f"| {t['month']} | {fmt(t['claims_change'], '%')} | "
                         f"{fmt(t['paid_change'], '%')} | {fmt(t['denial_rate_pp'])} |")
    if duplicates is not None:
        lines += ["", "## Potential duplicate services", "",
                  f"{len(duplicates)} groups share a member, procedure and service date "
                  "(review queue, not a quality failure)."]
        if duplicates:
            lines += ["", "| Member | Procedure | Date | Claims | Paid |",
                      "| --- | --- | --- | ---: | ---: |"]
            for g in duplicates[:5]:
                lines.append(f"| {g['member_id']} | {g['procedure_code']} | {g['service_date']} | "
                             f"{len(g['claim_ids'])} | ${g['paid']:,.0f} |")
    if age_bands:
        lines += ["", "## Cost by age band", "", "![Average paid by age band](age_band_costs.png)"]
    lines += [
        "",
        "![Monthly billed vs paid](monthly_financials.png)",
        "",
        "![Denial reasons](denial_reasons.png)",
        "",
        "Synthetic data generated by `healthdata.claims.ClaimGenerator`. "
        "Codes, plan types and payment rules are illustrative examples, not "
        "authoritative coding or adjudication logic. Not medical, financial "
        "or insurance advice.",
        "",
    ]
    return "\n".join(lines)


def plot_monthly_financials(monthly: list[dict], out_path) -> bool:
    if not monthly:
        return False
    months = [m["month"] for m in monthly]
    billed = [m["billed"] for m in monthly]
    paid = [m["paid"] for m in monthly]
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(months, billed, marker="o", markersize=3, label="billed")
    ax.plot(months, paid, marker="o", markersize=3, label="paid")
    ax.set_title("Monthly billed vs paid (synthetic, generator-shaped:\nmonths before the 90-day spread are sparse backfill)", fontsize=10)
    ax.set_ylabel("USD")
    ax.legend()
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_denial_categories(cats: list[dict], out_path) -> bool:
    """Grouped bars per broad denial category: share of denied claims next to
    share of denied billed dollars. Synthetic data, illustrative taxonomy."""
    if not cats:
        return False
    total_billed = sum(c["billed"] for c in cats)
    names = [c["category"] for c in cats]
    count_share = [c["share"] * 100 for c in cats]
    dollar_share = [(c["billed"] / total_billed * 100) if total_billed else 0.0 for c in cats]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ys = range(len(names))
    ax.barh([y - 0.2 for y in ys], count_share, height=0.38, color="#a61e4d", label="share of denied claims")
    ax.barh([y + 0.2 for y in ys], dollar_share, height=0.38, color="#364fc7", label="share of denied billed dollars")
    ax.set_yticks(list(ys))
    ax.set_yticklabels(names)
    ax.invert_yaxis()
    ax.set_xlabel("percent")
    ax.set_title("Denials by broad category (synthetic, illustrative taxonomy)")
    ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_denial_reasons(denial_reasons: list[tuple[str, int]], out_path) -> bool:
    if not denial_reasons:
        return False
    reasons = [r for r, _ in denial_reasons]
    counts = [c for _, c in denial_reasons]
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.barh(reasons, counts, color="#a61e4d")
    ax.set_title("Denial reasons (synthetic claims)")
    ax.set_xlabel("claims denied")
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_age_band_costs(age_bands: list[dict], out_path) -> bool:
    if not age_bands:
        return False
    names = [b["age_band"] for b in age_bands]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    bars = ax.bar(names, [b["avg_paid"] for b in age_bands], color="#1c7ed6")
    for bar, b in zip(bars, age_bands):
        ax.annotate(f"{b['denial_rate']:.0%} denied", (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha="center", va="bottom", fontsize=8)
    ax.set_title("Average paid per claim by age band (synthetic claims)")
    ax.set_ylabel("USD per claim")
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_paid_concentration(curve: list[tuple[float, float]], out_path) -> bool:
    """Cumulative paid share vs claim share (largest first) against the
    equal-spend diagonal. Synthetic data."""
    if not curve:
        return False
    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    ax.plot([p[0] * 100 for p in curve], [p[1] * 100 for p in curve], color="#1c7ed6", linewidth=2,
            label="largest claims first")
    ax.plot([0, 100], [0, 100], color="grey", linestyle="--", label="equal spend")
    ax.set_xlabel("% of claims (largest paid first)")
    ax.set_ylabel("% of total paid")
    ax.set_title("Paid-amount concentration (synthetic)", fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_plan_denial_rates(plan_perf: list[dict], out_path, min_claims: int = 1) -> bool:
    """Bar chart of denial rate per plan type with claim counts, plus the
    overall rate as a reference line. Synthetic data, illustrative."""
    rows = [r for r in plan_perf if r["claims"] >= min_claims]
    if not rows:
        return False
    total = sum(r["claims"] for r in rows)
    overall = sum(r["denial_rate"] * r["claims"] for r in rows) / total
    fig, ax = plt.subplots(figsize=(6.5, 4))
    bars = ax.bar([r["plan"] for r in rows], [r["denial_rate"] * 100 for r in rows], color="#e8590c")
    for bar, r in zip(bars, rows):
        ax.annotate(f"{r['denial_rate']:.1%}\n(n={r['claims']})",
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85), zorder=5)
    ax.axhline(overall * 100, color="grey", linestyle="--", label=f"overall {overall:.1%}")
    ax.set_ylabel("% of claims denied")
    ax.set_ylim(0, max(r["denial_rate"] for r in rows) * 100 * 1.3 + 1)
    ax.set_title("Denial rate by plan type (synthetic)", fontsize=11)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True


def plot_size_bands(size_bands: list[dict], out_path) -> bool:
    """Grouped bars: share of claims vs share of paid dollars per billed-amount
    band. Makes the concentration visible (many small claims, few large ones
    carrying most of the spend)."""
    if not size_bands or not any(b["claims"] for b in size_bands):
        return False
    # escape $ or matplotlib treats the labels as mathtext
    names = [b["band"].replace("$", "\\$") for b in size_bands]
    x = list(range(len(names)))
    width = 0.38
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.bar([i - width / 2 for i in x], [b["claim_share"] * 100 for b in size_bands],
           width, label="% of claims", color="#1c7ed6")
    ax.bar([i + width / 2 for i in x], [b["paid_share"] * 100 for b in size_bands],
           width, label="% of paid $", color="#e8590c")
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=9)
    ax.set_ylabel("share (%)")
    ax.set_title("Claim count vs paid dollars by billed-amount band (synthetic claims)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return True
