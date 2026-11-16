"""Generator: deterministic, schema-complete, plausible values."""
from healthdata.claims import (ClaimGenerator, DIAGNOSES, PLAN_TYPES,
                               PROCEDURES, STATUSES)


def test_generator_is_deterministic():
    a = ClaimGenerator(seed=1).claims(10)
    b = ClaimGenerator(seed=1).claims(10)
    assert a == b


def test_different_seeds_differ():
    a = ClaimGenerator(seed=1).claims(10)
    b = ClaimGenerator(seed=2).claims(10)
    assert a != b


def test_claim_schema_and_domains():
    claims = ClaimGenerator(seed=3).claims(200)
    valid_proc = {c for c, _d, _r in PROCEDURES}
    valid_dx = {c for c, _d in DIAGNOSES}
    for c in claims:
        assert c["claim_id"].startswith("CLM-")
        assert c["plan_type"] in PLAN_TYPES
        assert c["procedure_code"] in valid_proc
        assert c["diagnosis_code"] in valid_dx
        assert c["status"] in STATUSES
        assert c["billed_amount"] > 0
        assert c["paid_amount"] <= c["allowed_amount"] <= c["billed_amount"]
        if c["status"] == "denied":
            assert c["denial_reason"]
            assert c["paid_amount"] == 0.0


def test_service_date_override():
    import datetime as dt
    day = dt.date(2026, 11, 16)
    claims = ClaimGenerator(seed=5).claims(5, service_date=day)
    assert all(c["service_date"] == "2026-11-16" for c in claims)


def test_claim_ids_scoped_to_seed():
    a = ClaimGenerator(seed=1).claims(5)
    b = ClaimGenerator(seed=2).claims(5)
    ids_a = {c["claim_id"] for c in a}
    ids_b = {c["claim_id"] for c in b}
    assert ids_a.isdisjoint(ids_b)
