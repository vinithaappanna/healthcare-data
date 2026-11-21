"""Render the markdown report and charts from pipeline marts."""
from __future__ import annotations

import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


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
                    outliers: list[dict] | None = None,
                    concentration: dict | None = None,
                    gates: list[tuple[str, int]] | None = None,
                    denial_procs: list[dict] | None = None,
                    discounts: list[dict] | None = None,
                    denied_dollars: list[dict] | None = None,
                    repeat_denials: list[dict] | None = None) -> str:
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
        "| Month | Claims | Billed | Allowed | Paid | Denial rate |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for m in monthly:
        lines.append(
            f"| {m['month']} | {m['claims']} | ${m['billed']:,.0f} | "
            f"${m['allowed']:,.0f} | ${m['paid']:,.0f} | {m['denial_rate']:.1%} |"
        )
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
    if outliers is not None:
        lines += ["", "## Denial-rate outliers (plan x month)", "",
                  "Cells whose denial rate is at least 2 standard errors from the overall rate "
                  "(cells under 20 claims skipped). A statistical screen on synthetic data, not a finding."]
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
    if trend and len(trend) > 1:
        def fmt(v, suffix=""):
            return "-" if v is None else f"{v:+.1%}" if suffix == "%" else f"{v:+.2f} pp"
        lines += ["", "## Month-over-month trend (last 6 complete months)", "",
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
    ax.set_title("Monthly billed vs paid amounts (synthetic claims)")
    ax.set_ylabel("USD")
    ax.legend()
    fig.autofmt_xdate()
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
