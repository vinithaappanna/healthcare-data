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
