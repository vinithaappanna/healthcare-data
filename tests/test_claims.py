"""Generator: deterministic, schema-complete, plausible values."""
from healthdata.claims import (ClaimGenerator, DIAGNOSES, PLAN_TYPES,
                               PROCEDURES, STATUSES, next_batch_index)


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


def test_batches_share_prefix_but_differ():
    """Same day, two batches: distinct ids AND distinct claim content."""
    prefix = "CLM-61116"
    a = ClaimGenerator(20261116 * 1000 + 1, batch=1, id_prefix=prefix).claims(30)
    b = ClaimGenerator(20261116 * 1000 + 2, batch=2, id_prefix=prefix).claims(30)
    ids_a = {c["claim_id"] for c in a}
    ids_b = {c["claim_id"] for c in b}
    assert not ids_a & ids_b  # disjoint: no dedupe collisions between rounds
    assert all(i.startswith("CLM-61116-B01-") for i in ids_a)
    assert all(i.startswith("CLM-61116-B02-") for i in ids_b)
    # content differs too - not the same claims with new ids
    assert [c["billed_amount"] for c in a] != [c["billed_amount"] for c in b]


def test_batch_zero_keeps_original_id_format():
    claims = ClaimGenerator(seed=7).claims(3)
    assert all("-B" not in c["claim_id"] for c in claims)


def test_same_batch_reproduces_identically():
    a = ClaimGenerator(99, batch=1, id_prefix="CLM-X").claims(10)
    b = ClaimGenerator(99, batch=1, id_prefix="CLM-X").claims(10)
    assert a == b


def test_next_batch_index_sequences_rounds():
    assert next_batch_index([], "CLM-61116") == 1
    # today's unbatched batch exists -> first sequenced batch is B01
    assert next_batch_index(["CLM-61116-000001"], "CLM-61116") == 1
    assert next_batch_index(["CLM-61116-B01-000001"], "CLM-61116") == 2
    assert next_batch_index(
        ["CLM-61116-B01-000001", "CLM-61116-B03-000002"], "CLM-61116") == 4
    # other days' ids do not count
    assert next_batch_index(["CLM-50115-B09-000001"], "CLM-61116") == 1
