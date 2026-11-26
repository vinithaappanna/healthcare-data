"""Quality checks catch dirty stores and pass clean ones."""
from healthdata.claims import ClaimGenerator
from healthdata.pipeline import Pipeline
from healthdata.quality import (check_amount_consistency,
                                check_denial_reasons,
                                check_duplicate_members_per_claim, run_all)


def test_clean_store_passes(tmp_path):
    pipe = Pipeline(tmp_path / "claims.csv")
    pipe.ingest(ClaimGenerator(seed=11).claims(50))
    assert run_all(tmp_path / "claims.csv") == []


def test_missing_store_is_an_issue(tmp_path):
    assert run_all(tmp_path / "nope.csv")


def test_paid_over_allowed_flagged():
    rows = [{"claim_id": "C1", "billed_amount": "100", "allowed_amount": "80",
             "paid_amount": "90"}]
    assert any("exceeds allowed" in i for i in check_amount_consistency(rows))


def test_denied_with_payment_flagged():
    rows = [{"claim_id": "C2", "status": "denied", "paid_amount": "10",
             "denial_reason": "duplicate claim"}]
    assert any("denied claim has a payment" in i for i in check_denial_reasons(rows))


def test_duplicate_claim_ids_flagged():
    rows = [{"claim_id": "C3"}, {"claim_id": "C3"}]
    assert check_duplicate_members_per_claim(rows)


def test_billed_outside_procedure_range_flagged():
    from healthdata.quality import check_billed_in_procedure_range
    rows = [
        {"claim_id": "A", "procedure_code": "99213", "billed_amount": "120"},
        {"claim_id": "B", "procedure_code": "99213", "billed_amount": "9000"},
        {"claim_id": "C", "procedure_code": "00000", "billed_amount": "10"},
    ]
    issues = check_billed_in_procedure_range(rows)
    assert len(issues) == 2
    assert any("B:" in i and "outside" in i for i in issues)
    assert any("C:" in i and "unknown procedure" in i for i in issues)


def test_unknown_diagnosis_flagged():
    from healthdata.quality import check_known_diagnosis
    rows = [{"claim_id": "A", "diagnosis_code": "I10"},
            {"claim_id": "B", "diagnosis_code": "ZZZ"}]
    assert len(check_known_diagnosis(rows)) == 1


def test_service_date_checks():
    import datetime as dt
    from healthdata.quality import check_service_dates
    today = dt.date(2026, 11, 19)
    rows = [{"claim_id": "OK", "service_date": "2026-11-19"},          # today is fine
            {"claim_id": "FUT", "service_date": "2026-11-20"},
            {"claim_id": "OLD", "service_date": "2024-11-01"},
            {"claim_id": "EDGE", "service_date": "2024-11-18"},         # 731 days: flagged
            {"claim_id": "BAD", "service_date": "11/19/2026"},
            {"claim_id": "EMPTY", "service_date": ""}]
    issues = check_service_dates(rows, today=today)
    flagged = {i.split(":")[0] for i in issues}
    assert flagged == {"FUT", "OLD", "EDGE", "BAD", "EMPTY"}
    assert any("in the future" in i for i in issues) and any("unparseable" in i for i in issues)
    assert check_service_dates([{"claim_id": "X", "service_date": "2024-11-20"}], today=today) == []  # 729 days ok; exactly 730 also ok


def test_run_all_catches_future_dates_in_store(tmp_path):
    import csv
    path = tmp_path / "claims.csv"
    Pipeline(path).ingest(ClaimGenerator(seed=3).claims(5))
    rows = list(csv.DictReader(path.open()))
    rows[0]["service_date"] = "2999-01-01"
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    assert any("in the future" in i for i in run_all(path))


def test_service_date_exactly_at_limit_passes():
    import datetime as dt
    from healthdata.quality import check_service_dates
    assert check_service_dates([{"claim_id": "L", "service_date": "2024-11-19"}],
                               today=dt.date(2026, 11, 19)) == []


def test_run_checks_lists_each_check_and_isolates_crashes(monkeypatch):
    from healthdata import quality
    rows = [{"claim_id": "C1", "billed_amount": "100", "allowed_amount": "80", "paid_amount": "90",
             "status": "paid", "denial_reason": "", "member_id": "M", "plan_type": "PPO",
             "procedure_code": "99213", "diagnosis_code": "I10", "service_date": "2026-11-01"}]
    results = dict(quality.run_checks(rows))
    assert list(results) == [n for n, _f in quality.CHECKS]
    assert results["amount consistency"]            # paid over allowed
    assert results["denial reasons"] == []

    def boom(_rows):
        raise ValueError("bad")
    monkeypatch.setattr(quality, "CHECKS", [("boom", boom), ("denial reasons", quality.check_denial_reasons)])
    out = quality.run_checks(rows)
    assert out[0][1] == ["check crashed: ValueError: bad"] and out[1] == ("denial reasons", [])


def test_run_all_matches_run_checks_total(tmp_path):
    from healthdata import quality
    path = tmp_path / "claims.csv"
    Pipeline(path).ingest(ClaimGenerator(seed=5).claims(40))
    rows = quality.load_rows(path)
    assert quality.run_all(path) == [i for _n, iss in quality.run_checks(rows) for i in iss] == []
    assert quality.load_rows(tmp_path / "nope.csv") is None


def test_gates_section_renders_pass_and_fail():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, gates=[("amount consistency", 0), ("service dates", 2)])
    assert "1 of 2 checks passed" in md
    assert "| amount consistency | 0 | pass |" in md and "| service dates | 2 | FAIL |" in md


def test_member_consistency_flags_conflicts_and_generator_is_consistent():
    from healthdata.quality import check_member_consistency
    rows = [{"claim_id": "C1", "member_id": "M1", "plan_type": "PPO", "age_band": "30-44"},
            {"claim_id": "C2", "member_id": "M1", "plan_type": "HMO", "age_band": "30-44"},
            {"claim_id": "C3", "member_id": "M2", "plan_type": "HMO", "age_band": "0-17"}]
    issues = check_member_consistency(rows)
    assert len(issues) == 1 and "C2" in issues[0]
    gen = ClaimGenerator(seed=5).claims(400)
    assert check_member_consistency(gen) == []


def test_harmonize_members_repairs_store_and_is_idempotent(tmp_path):
    from healthdata.claims import member_profile
    from healthdata.quality import load_rows
    pipe = Pipeline(tmp_path / "c.csv")
    claims = ClaimGenerator(seed=9).claims(30)
    for c in claims[:10]:
        c["plan_type"] = "HMO" if member_profile(c["member_id"])[0] != "HMO" else "PPO"   # force a conflict
    pipe.ingest(claims)
    first = pipe.harmonize_members()
    assert first >= 10
    assert check_member_consistency_rows(load_rows(tmp_path / "c.csv")) == []
    assert pipe.harmonize_members() == 0


def check_member_consistency_rows(rows):
    from healthdata.quality import check_member_consistency
    return check_member_consistency(rows)


def test_age_repair_keeps_amount_rules_and_denials_and_gate_catches_it(tmp_path):
    from healthdata.claims import ORIGIN_REGENERATED, age_plausible
    from healthdata.quality import check_age_plausibility, load_rows, run_all
    base = dict(member_id="MBR-0001", service_date="2026-10-01", diagnosis_code="Z00.00",
                age_band="0-17", plan_type="PPO")
    rows = [dict(base, claim_id="CLM-K1", procedure_code="27447", billed_amount=20000,
                 allowed_amount=15000, paid_amount=12000, status="paid", denial_reason=""),
            dict(base, claim_id="CLM-K2", procedure_code="27447", billed_amount=30000,
                 allowed_amount=0, paid_amount=0, status="denied", denial_reason="not covered")]
    assert len(check_age_plausibility(rows)) == 2
    # the same member profile must also hold for the gate to be isolated here
    pipe = Pipeline(tmp_path / "a.csv")
    pipe.ingest(rows)
    pipe.harmonize_members()
    fixed = {r["claim_id"]: r for r in load_rows(tmp_path / "a.csv")}
    for r in fixed.values():
        assert age_plausible(r["age_band"], r["procedure_code"], r["diagnosis_code"])
        assert r["data_origin"] == ORIGIN_REGENERATED
        assert float(r["paid_amount"]) <= float(r["allowed_amount"]) <= float(r["billed_amount"])
    assert fixed["CLM-K2"]["status"] == "denied" and float(fixed["CLM-K2"]["paid_amount"]) == 0.0
    assert run_all(tmp_path / "a.csv") == []
    assert pipe.harmonize_members() == 0
    assert pipe.origin_counts() == {ORIGIN_REGENERATED: 2}


def test_new_claims_default_to_generated_and_gate_clean(tmp_path):
    pipe = Pipeline(tmp_path / "g.csv")
    pipe.ingest(ClaimGenerator(seed=21).claims(300))
    assert pipe.origin_counts() == {"generated": 300}
    assert run_all(tmp_path / "g.csv") == []


def test_provenance_section_renders_only_with_regenerated_rows():
    from healthdata import report
    md = report.render_markdown([], [], [], 0, origins={"generated": 5, "regenerated-2026-11-21": 7})
    assert "| regenerated-2026-11-21 | 7 |" in md and "Data provenance" in md
    assert "Data provenance" not in report.render_markdown([], [], [], 0, origins={"generated": 5})


def test_generator_only_denies_duplicates_that_have_an_original(tmp_path):
    from healthdata.quality import check_duplicate_denials_supported
    claims = ClaimGenerator(seed=77).claims(1500)
    assert check_duplicate_denials_supported(claims) == []
    dups = [c for c in claims if c["denial_reason"] == "duplicate claim"]
    assert dups                                              # repeats are generated on purpose
    assert all(c["status"] == "denied" and c["paid_amount"] == 0 for c in dups)
    from healthdata.pipeline import Pipeline
    pipe = Pipeline(tmp_path / "g.csv")
    pipe.ingest(claims)
    out = pipe.duplicate_leakage()
    assert out["unsupported_duplicate_denials"] == 0 and out["caught"] > 0 and out["leaked_claims"] > 0


def test_gate_flags_unsupported_duplicate_denial_and_repair_fixes_it_keeping_provenance(tmp_path):
    from healthdata.pipeline import Pipeline
    from healthdata.quality import check_duplicate_denials_supported, load_rows, run_all
    base = dict(member_id="MBR-0001", plan_type=None, age_band=None, service_date="2026-10-01",
                procedure_code="99213", diagnosis_code="I10", billed_amount=100.0)
    from healthdata.claims import member_profile
    plan, band = member_profile("MBR-0001")
    base.update(plan_type=plan, age_band=band)
    orphan = dict(base, claim_id="CLM-X1", procedure_code="93000", status="denied", denial_reason="duplicate claim",
                  allowed_amount=0.0, paid_amount=0.0)
    original = dict(base, claim_id="CLM-Y1", status="paid", denial_reason="", allowed_amount=80.0, paid_amount=60.0)
    repeat = dict(base, claim_id="CLM-Y2", status="denied", denial_reason="duplicate claim",
                  allowed_amount=0.0, paid_amount=0.0)
    assert len(check_duplicate_denials_supported([orphan, original, repeat])) == 1
    pipe = Pipeline(tmp_path / "d.csv")
    pipe.ingest([orphan, original, repeat])
    assert pipe.harmonize_members() == 1
    rows = {r["claim_id"]: r for r in load_rows(tmp_path / "d.csv")}
    assert rows["CLM-X1"]["denial_reason"] != "duplicate claim" and rows["CLM-X1"]["status"] == "denied"
    assert rows["CLM-X1"]["data_origin"] == "regenerated-2026-11-22"
    assert rows["CLM-Y2"]["denial_reason"] == "duplicate claim" and rows["CLM-Y2"]["data_origin"] == "generated"
    assert run_all(tmp_path / "d.csv") == [] and pipe.harmonize_members() == 0


def test_status_vocabulary_flags_each_problem_and_passes_clean():
    from healthdata.quality import check_status_vocabulary
    base = {"billed_amount": "100", "allowed_amount": "80", "paid_amount": "60", "denial_reason": ""}
    rows = [dict(base, claim_id="A", status="paid"),
            dict(base, claim_id="A", status="paid"),                                   # duplicate id
            dict(base, claim_id="B", status="pending"),                                # unknown status
            dict(base, claim_id="C", status="adjusted", denial_reason="timely filing exceeded"),
            dict(base, claim_id="D", status="paid", paid_amount="-5"),
            dict(base, claim_id="E", status="denied", denial_reason="duplicate claim", paid_amount="0")]
    got = check_status_vocabulary(rows)
    assert got == ["A: duplicate claim id", "B: unknown status 'pending'",
                   "C: denial reason on a adjusted claim", "D: negative paid_amount"]
    assert check_status_vocabulary([rows[0], rows[5]]) == []
    assert check_status_vocabulary([dict(base, claim_id="F", status="paid", billed_amount="x")]) == []
