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
