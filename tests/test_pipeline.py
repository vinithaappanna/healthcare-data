"""Pipeline: validation, idempotent ingest, and mart math."""
from healthdata.claims import ClaimGenerator
from healthdata.pipeline import Pipeline, validate


def make_valid(claim_id="CLM-T1", **overrides):
    claim = {
        "claim_id": claim_id, "member_id": "MBR-0001", "plan_type": "PPO",
        "age_band": "30-44", "service_date": "2026-11-01",
        "procedure_code": "99213", "diagnosis_code": "I10",
        "billed_amount": 100.0, "allowed_amount": 80.0,
        "paid_amount": 60.0, "status": "paid", "denial_reason": "",
    }
    claim.update(overrides)
    return claim


def test_validate_accepts_clean_claim():
    assert validate(make_valid()) == []


def test_validate_catches_problems():
    assert "missing member_id" in validate(make_valid(member_id=""))
    assert "negative billed_amount" in validate(make_valid(billed_amount=-1))
    assert "unknown status" in " ".join(validate(make_valid(status="lost")))
    assert "denied without denial_reason" in validate(
        make_valid(status="denied", denial_reason="", paid_amount=0.0))


def test_ingest_is_idempotent(tmp_path):
    pipe = Pipeline(tmp_path / "claims.csv")
    batch = ClaimGenerator(seed=9).claims(20)
    first = pipe.ingest(batch)
    second = pipe.ingest(batch)
    assert first["added"] == 20
    assert second["added"] == 0 and second["total"] == 20


def test_ingest_rejects_bad_rows_loudly(tmp_path):
    pipe = Pipeline(tmp_path / "claims.csv")
    stats = pipe.ingest([make_valid("CLM-OK"), make_valid("CLM-BAD", billed_amount=-5)])
    assert stats["added"] == 1
    assert stats["rejected"][0]["claim_id"] == "CLM-BAD"


def test_monthly_financials_math(tmp_path):
    pipe = Pipeline(tmp_path / "claims.csv")
    pipe.ingest([
        make_valid("CLM-A", billed_amount=100, allowed_amount=80, paid_amount=60),
        make_valid("CLM-B", billed_amount=200, allowed_amount=150, paid_amount=0,
                   status="denied", denial_reason="duplicate claim"),
    ])
    (m,) = pipe.monthly_financials()
    assert m["month"] == "2026-11"
    assert m["claims"] == 2
    assert m["billed"] == 300.0 and m["allowed"] == 230.0 and m["paid"] == 60.0
    assert m["denial_rate"] == 0.5


def test_denial_reasons_and_plan_mix(tmp_path):
    pipe = Pipeline(tmp_path / "claims.csv")
    pipe.ingest([
        make_valid("CLM-A", status="denied", paid_amount=0,
                   denial_reason="duplicate claim"),
        make_valid("CLM-B", status="denied", paid_amount=0,
                   denial_reason="duplicate claim"),
        make_valid("CLM-C", plan_type="HMO"),
    ])
    assert pipe.denial_reasons() == [("duplicate claim", 2)]
    assert dict(pipe.plan_mix()) == {"PPO": 2, "HMO": 1}


def test_plan_performance_rates(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([
        make_valid("CLM-A", plan_type="PPO", billed_amount=100, allowed_amount=80, paid_amount=60),
        make_valid("CLM-B", plan_type="PPO", billed_amount=100, allowed_amount=80, paid_amount=0,
                   status="denied", denial_reason="duplicate claim"),
        make_valid("CLM-C", plan_type="HMO", billed_amount=50, allowed_amount=40, paid_amount=40),
    ])
    perf = {r["plan"]: r for r in pipe.plan_performance()}
    assert perf["PPO"]["claims"] == 2
    assert perf["PPO"]["denial_rate"] == 0.5
    assert perf["PPO"]["paid_to_billed"] == 0.3
    assert perf["HMO"]["denial_rate"] == 0.0
    assert pipe.plan_performance()[0]["plan"] == "PPO"  # most claims first


def test_report_includes_plan_performance_table():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, plan_perf=[
        {"plan": "PPO", "claims": 2, "denial_rate": 0.5, "paid_to_billed": 0.3}])
    assert "## Plan performance" in md and "| PPO | 2 | 50.0% | 30.0% |" in md


def test_procedure_summary_ranks_by_paid(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([
        make_valid("CLM-A", procedure_code="27447", billed_amount=1000, allowed_amount=900, paid_amount=800),
        make_valid("CLM-B", procedure_code="99213", billed_amount=100, allowed_amount=80, paid_amount=70),
        make_valid("CLM-C", procedure_code="99213", billed_amount=200, allowed_amount=0, paid_amount=0,
                   status="denied", denial_reason="duplicate claim"),
    ])
    out = pipe.procedure_summary()
    assert [r["code"] for r in out] == ["27447", "99213"]
    assert out[1]["claims"] == 2 and out[1]["avg_billed"] == 150.0
    assert out[1]["denial_rate"] == 0.5
    assert len(pipe.procedure_summary(top=1)) == 1


def test_report_includes_procedure_table():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, procedures=[
        {"code": "99213", "claims": 2, "avg_billed": 150.0, "paid": 70.0, "denial_rate": 0.5}])
    assert "## Top procedures by paid amount" in md and "| 99213 | 2 |" in md


def test_high_utilizers_threshold_and_share(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest(
        [make_valid(f"CLM-H{i}", member_id="MBR-0001", billed_amount=100,
                    allowed_amount=80, paid_amount=60) for i in range(3)]
        + [make_valid("CLM-L1", member_id="MBR-0002", billed_amount=100,
                      allowed_amount=80, paid_amount=60)])
    out = pipe.high_utilizers(min_claims=3)
    assert out["members_total"] == 2 and out["high_utilizers"] == 1
    assert out["share_of_paid"] == 0.75  # 180 of 240
    assert out["top"] == [{"member_id": "MBR-0001", "claims": 3, "paid": 180.0}]
    assert pipe.high_utilizers(min_claims=4)["high_utilizers"] == 0


def test_high_utilizers_empty_store(tmp_path):
    out = Pipeline(tmp_path / "none.csv").high_utilizers()
    assert out["members_total"] == 0 and out["share_of_paid"] == 0.0


def test_report_includes_utilization_section():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, utilization={
        "members_total": 10, "high_utilizers": 2, "share_of_paid": 0.25,
        "top": [{"member_id": "MBR-0001", "claims": 4, "paid": 900.0}]})
    assert "## Member utilization" in md and "| MBR-0001 | 4 | $900 |" in md


def test_age_band_costs_order_and_math(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([
        make_valid("CLM-1", age_band="60-74", billed_amount=100, allowed_amount=80, paid_amount=60),
        make_valid("CLM-2", age_band="0-17", billed_amount=100, allowed_amount=80, paid_amount=40),
        make_valid("CLM-3", age_band="0-17", billed_amount=100, allowed_amount=0, paid_amount=0,
                   status="denied", denial_reason="duplicate claim"),
    ])
    out = pipe.age_band_costs()
    assert [b["age_band"] for b in out] == ["0-17", "60-74"]  # natural age order
    assert out[0]["avg_paid"] == 20.0 and out[0]["denial_rate"] == 0.5


def test_age_band_chart_written(tmp_path):
    from healthdata import report
    bands = [{"age_band": "0-17", "claims": 2, "avg_paid": 20.0, "denial_rate": 0.5}]
    assert report.plot_age_band_costs(bands, tmp_path / "a.png")
    assert (tmp_path / "a.png").stat().st_size > 1000
    assert report.plot_age_band_costs([], tmp_path / "b.png") is False


def test_denial_reasons_by_plan(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    den = dict(status="denied", paid_amount=0, allowed_amount=0, billed_amount=100)
    pipe.ingest([
        make_valid("CLM-1", plan_type="PPO", denial_reason="duplicate claim", **den),
        make_valid("CLM-2", plan_type="PPO", denial_reason="duplicate claim", **den),
        make_valid("CLM-3", plan_type="PPO", denial_reason="timely filing exceeded", **den),
        make_valid("CLM-4", plan_type="HMO", denial_reason="out-of-network provider", **den),
        make_valid("CLM-5", plan_type="HMO"),  # paid, ignored
    ])
    out = pipe.denial_reasons_by_plan()
    assert list(out) == ["HMO", "PPO"]
    assert out["PPO"] == [("duplicate claim", 2), ("timely filing exceeded", 1)]
    assert out["HMO"] == [("out-of-network provider", 1)]


def test_report_renders_reasons_by_plan():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, reasons_by_plan={
        "PPO": [("duplicate claim", 2), ("timely filing exceeded", 1)]})
    assert "| PPO | 3 | duplicate claim | 2 |" in md


def test_potential_duplicates_groups_same_service(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    same = dict(member_id="MBR-0001", procedure_code="99213", service_date="2026-11-01")
    pipe.ingest([
        make_valid("CLM-1", paid_amount=50, allowed_amount=60, billed_amount=100, **same),
        make_valid("CLM-2", paid_amount=40, allowed_amount=60, billed_amount=100, **same),
        make_valid("CLM-3", member_id="MBR-0001", procedure_code="99213",
                   service_date="2026-11-02"),  # different date
        make_valid("CLM-4", member_id="MBR-0002", procedure_code="99213",
                   service_date="2026-11-01"),  # different member
    ])
    out = pipe.potential_duplicates()
    assert len(out) == 1
    assert out[0]["claim_ids"] == ["CLM-1", "CLM-2"] and out[0]["paid"] == 90.0
    assert Pipeline(tmp_path / "empty.csv").potential_duplicates() == []


def test_report_renders_duplicates_section_even_when_empty():
    from healthdata import report
    assert "0 groups" in report.render_markdown([], [], [], 0, duplicates=[])
    md = report.render_markdown([], [], [], 0, duplicates=[{
        "member_id": "MBR-0001", "procedure_code": "99213", "service_date": "2026-11-01",
        "claim_ids": ["A", "B"], "paid": 90.0}])
    assert "| MBR-0001 | 99213 | 2026-11-01 | 2 | $90 |" in md


def test_monthly_trend_changes(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([
        make_valid("CLM-1", service_date="2026-09-05", paid_amount=100, allowed_amount=100, billed_amount=200),
        make_valid("CLM-2", service_date="2026-09-06", paid_amount=100, allowed_amount=100, billed_amount=200),
        make_valid("CLM-3", service_date="2026-10-05", paid_amount=300, allowed_amount=300, billed_amount=400),
        make_valid("CLM-4", service_date="2026-10-06", status="denied", paid_amount=0,
                   allowed_amount=0, billed_amount=100, denial_reason="duplicate claim"),
        make_valid("CLM-5", service_date="2026-10-07", paid_amount=0, allowed_amount=0,
                   billed_amount=100, status="denied", denial_reason="duplicate claim"),
        make_valid("CLM-6", service_date="2026-10-08", paid_amount=100, allowed_amount=100, billed_amount=200),
    ])
    first, second = pipe.monthly_trend()
    assert first["claims_change"] is None and first["denial_rate_pp"] is None
    assert second["claims_change"] == 1.0   # 2 -> 4 claims
    assert second["paid_change"] == 1.0     # 200 -> 400
    assert second["denial_rate_pp"] == 50.0  # 0% -> 50%


def test_report_renders_trend_table():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, trend=[
        {"month": "2026-09", "claims_change": None, "paid_change": None, "denial_rate_pp": None},
        {"month": "2026-10", "claims_change": 0.25, "paid_change": -0.1, "denial_rate_pp": 1.5}])
    assert "| 2026-10 | +25.0% | -10.0% | +1.50 pp |" in md and "| 2026-09 | - | - | - |" in md


def test_plan_cost_sharing_math_and_excludes_denied(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([
        make_valid("CLM-1", plan_type="PPO", billed_amount=100, allowed_amount=80, paid_amount=60),
        make_valid("CLM-2", plan_type="PPO", billed_amount=100, allowed_amount=80, paid_amount=40),
        make_valid("CLM-3", plan_type="HMO", billed_amount=100, allowed_amount=50, paid_amount=50),
        make_valid("CLM-4", plan_type="HMO", billed_amount=900, allowed_amount=0, paid_amount=0,
                   status="denied", denial_reason="duplicate claim"),
    ])
    out = {r["plan"]: r for r in pipe.plan_cost_sharing()}
    assert out["PPO"]["network_discount"] == 0.2          # 1 - 160/200
    assert out["PPO"]["member_cost_share"] == 0.375       # (160-100)/160
    assert out["HMO"] == {"plan": "HMO", "claims": 1, "network_discount": 0.5,
                          "member_cost_share": 0.0}       # denied claim ignored
    assert [r["plan"] for r in pipe.plan_cost_sharing()] == ["PPO", "HMO"]  # highest share first


def test_cost_sharing_section_renders_with_illustrative_label():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, cost_sharing=[
        {"plan": "PPO", "claims": 2, "network_discount": 0.2, "member_cost_share": 0.375}])
    assert "| PPO | 2 | 20.0% | 37.5% |" in md and "Illustrative" in md


def _cell(plan, month, n, denied, start=0):
    return [make_valid(f"CLM-{plan}-{month}-{start + i}", plan_type=plan, service_date=f"{month}-10",
                       status="denied" if i < denied else "paid",
                       denial_reason="duplicate claim" if i < denied else "",
                       paid_amount=0 if i < denied else 60) for i in range(n)]


def test_denial_rate_outliers_flags_high_cell_and_skips_small(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    claims = (_cell("PPO", "2026-09", 100, 5) + _cell("HMO", "2026-09", 100, 5)
              + _cell("PPO", "2026-10", 100, 5) + _cell("HMO", "2026-10", 100, 40)
              + _cell("HDHP", "2026-10", 10, 10))          # tiny cell: skipped
    pipe.ingest(claims)
    out = pipe.denial_rate_outliers()
    assert (out[0]["plan"], out[0]["month"]) == ("HMO", "2026-10")  # largest |z| first
    assert out[0]["z"] > 2 and out[0]["denial_rate"] == 0.4
    assert all(o["plan"] != "HDHP" for o in out)                    # 10-claim cell skipped
    assert any(o["z"] < 0 for o in out)                             # unusually low cells flagged too


def test_denial_rate_outliers_edge_cases(tmp_path):
    assert Pipeline(tmp_path / "e.csv").denial_rate_outliers() == []      # empty store
    pipe = Pipeline(tmp_path / "u.csv")
    pipe.ingest(_cell("PPO", "2026-10", 50, 0))                            # no denials at all
    assert pipe.denial_rate_outliers() == []


def test_outlier_section_renders_both_states():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, outliers=[
        {"plan": "HMO", "month": "2026-10", "claims": 100, "denial_rate": 0.4,
         "overall_rate": 0.1, "z": 5.2}])
    assert "| HMO | 2026-10 | 100 | 40.0% | 10.0% | +5.20 |" in md and "not a finding" in md
    assert "No plan/month cells" in report.render_markdown([], [], [], 0, outliers=[])


def test_paid_concentration_math(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    paid = [1000] + [10] * 99                               # 100 claims, total 1990
    pipe.ingest([make_valid(f"CLM-{i}", billed_amount=2000, allowed_amount=1500, paid_amount=p)
                 for i, p in enumerate(paid)])
    out = pipe.paid_concentration()
    assert out["claims"] == 100 and out["total_paid"] == 1990.0
    tiers = {t["top_pct"]: t for t in out["tiers"]}
    assert tiers[0.01]["claims"] == 1 and tiers[0.01]["share_of_paid"] == 0.5025   # 1000/1990
    assert tiers[0.05]["claims"] == 5 and tiers[0.05]["share_of_paid"] == 0.5226   # 1040/1990
    assert tiers[0.10]["claims"] == 10


def test_paid_concentration_tiny_and_empty_stores(tmp_path):
    assert Pipeline(tmp_path / "e.csv").paid_concentration()["tiers"] == []
    pipe = Pipeline(tmp_path / "one.csv")
    pipe.ingest([make_valid("CLM-1", paid_amount=60)])
    out = pipe.paid_concentration()
    assert [t["claims"] for t in out["tiers"]] == [1, 1, 1]       # at least one claim per tier
    assert all(t["share_of_paid"] == 1.0 for t in out["tiers"])
    pipe2 = Pipeline(tmp_path / "den.csv")
    pipe2.ingest([make_valid("CLM-D", paid_amount=0, allowed_amount=0, status="denied",
                             denial_reason="duplicate claim")])
    assert pipe2.paid_concentration()["tiers"] == []              # zero total: no division


def test_concentration_section_renders():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, concentration={
        "claims": 100, "total_paid": 1990.0,
        "tiers": [{"top_pct": 0.01, "claims": 1, "share_of_paid": 0.5025}]})
    assert "| top 1% | 1 | 50.2% |" in md or "| top 1% | 1 | 50.3% |" in md


def test_paid_curve_shape_and_values(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    pipe.ingest([make_valid(f"CLM-{i}", billed_amount=2000, allowed_amount=1500, paid_amount=p)
                 for i, p in enumerate([60, 20, 10, 10])])      # total 100
    curve = pipe.paid_curve(points=4)
    assert curve == [(0.0, 0.0), (0.25, 0.6), (0.5, 0.8), (0.75, 0.9), (1.0, 1.0)]
    shares = [c[1] for c in pipe.paid_curve(points=20)]
    assert shares == sorted(shares) and shares[-1] == 1.0       # monotonic, ends at 100%
    assert Pipeline(tmp_path / "e.csv").paid_curve() == []
    assert pipe.paid_curve(points=0) == []


def test_concentration_chart_renders(tmp_path):
    from healthdata import report
    assert report.plot_paid_concentration([(0.0, 0.0), (0.5, 0.8), (1.0, 1.0)], tmp_path / "c.png") is True
    assert (tmp_path / "c.png").stat().st_size > 1000
    assert report.plot_paid_concentration([], tmp_path / "x.png") is False


def test_procedures_by_denial_reason_ranking_and_ties(tmp_path):
    pipe = Pipeline(tmp_path / "c.csv")
    def den(i, proc, reason):
        return make_valid(f"CLM-D{i}", procedure_code=proc, status="denied", paid_amount=0,
                          allowed_amount=0, denial_reason=reason)
    claims = ([den(i, "27447", "missing prior authorization") for i in range(3)]
              + [den(10 + i, "99213", "missing prior authorization") for i in range(2)]
              + [den(20, "70553", "missing prior authorization")]
              + [den(30, "99213", "duplicate claim"), den(31, "93000", "duplicate claim")]
              + [make_valid("CLM-OK1"), make_valid("CLM-OK2")])        # paid claims are ignored
    pipe.ingest(claims)
    out = pipe.procedures_by_denial_reason(top_reasons=2, top_procs=2)
    assert [d["reason"] for d in out] == ["missing prior authorization", "duplicate claim"]
    top = out[0]
    assert top["denials"] == 6
    assert top["procedures"] == [{"code": "27447", "denials": 3, "share": 0.5},
                                 {"code": "99213", "denials": 2, "share": 0.3333}]
    assert [p["code"] for p in out[1]["procedures"]] == ["93000", "99213"]   # tie: code order
    assert Pipeline(tmp_path / "e.csv").procedures_by_denial_reason() == []


def test_denial_procs_section_renders():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, denial_procs=[
        {"reason": "duplicate claim", "denials": 4,
         "procedures": [{"code": "99213", "denials": 3, "share": 0.75}]}])
    assert "| duplicate claim | 4 | 99213 (75%) |" in md
