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
