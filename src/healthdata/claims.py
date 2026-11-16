"""Synthetic claims generator.

Every record is invented by a seeded RNG - no real member, patient, provider
or plan data. The same seed always produces the same claims, which keeps
tests and demos reproducible.
"""
from __future__ import annotations

import datetime as dt
import random

PLAN_TYPES = ["HMO", "PPO", "EPO", "HDHP"]
AGE_BANDS = ["0-17", "18-29", "30-44", "45-59", "60-74", "75+"]
# (code, description, typical billed range)
PROCEDURES = [
    ("99213", "Office visit, established patient", (80, 160)),
    ("99214", "Office visit, moderate complexity", (120, 220)),
    ("99285", "Emergency department visit, high severity", (600, 1500)),
    ("70450", "CT head/brain without contrast", (400, 900)),
    ("80053", "Comprehensive metabolic panel", (40, 120)),
    ("85025", "Complete blood count", (25, 80)),
    ("93000", "Electrocardiogram", (50, 150)),
    ("97110", "Therapeutic exercises", (60, 180)),
    ("27447", "Total knee replacement", (15000, 35000)),
    ("43239", "Upper GI endoscopy with biopsy", (1200, 3000)),
]
DIAGNOSES = [
    ("I10", "Essential hypertension"),
    ("E11.9", "Type 2 diabetes without complications"),
    ("J06.9", "Acute upper respiratory infection"),
    ("M54.5", "Low back pain"),
    ("R51", "Headache"),
    ("Z00.00", "General adult medical exam"),
]
DENIAL_REASONS = [
    "not medically necessary",
    "missing prior authorization",
    "duplicate claim",
    "out-of-network provider",
    "timely filing exceeded",
]
STATUSES = ["paid", "denied", "adjusted"]


class ClaimGenerator:
    """Deterministic synthetic claims. `ClaimGenerator(seed).claims(n)`.

    `batch` numbers a batch within a day so several runs a day produce
    distinct, non-overlapping claims (ids carry a -Bnn- segment). Leave it
    at 0 for a standalone generator and the id format is unchanged.
    `id_prefix` overrides the seed-derived prefix so a day's batches share
    one prefix even though each batch gets its own RNG seed.
    """

    def __init__(self, seed: int = 42, batch: int = 0, id_prefix: str | None = None):
        self._rng = random.Random(seed)
        # Scope claim ids to the seed so batches from different generators
        # never collide on claim_id (the dedupe grain).
        self._id_prefix = id_prefix or f"CLM-{seed % 100000:05d}"
        self._batch = batch
        self._claim_seq = 0

    def _member(self) -> dict:
        rng = self._rng
        return {
            "member_id": f"MBR-{rng.randrange(1, 2000):04d}",
            "plan_type": rng.choice(PLAN_TYPES),
            "age_band": rng.choice(AGE_BANDS),
        }

    def claim(self, service_date: dt.date | None = None) -> dict:
        rng = self._rng
        self._claim_seq += 1
        member = self._member()
        code, _desc, (lo, hi) = rng.choice(PROCEDURES)
        dx_code, _dx = rng.choice(DIAGNOSES)
        billed = round(rng.uniform(lo, hi), 2)
        status = rng.choices(STATUSES, weights=[78, 12, 10])[0]
        denial_reason = rng.choice(DENIAL_REASONS) if status == "denied" else ""
        allowed = round(billed * rng.uniform(0.6, 0.95), 2)
        paid = round(allowed * rng.uniform(0.7, 1.0), 2) if status != "denied" else 0.0
        day = service_date or dt.date.today() - dt.timedelta(days=rng.randrange(0, 365))
        if self._batch:
            claim_id = f"{self._id_prefix}-B{self._batch:02d}-{self._claim_seq:06d}"
        else:
            claim_id = f"{self._id_prefix}-{self._claim_seq:06d}"
        return {
            "claim_id": claim_id,
            **member,
            "service_date": day.isoformat(),
            "procedure_code": code,
            "diagnosis_code": dx_code,
            "billed_amount": billed,
            "allowed_amount": allowed,
            "paid_amount": paid,
            "status": status,
            "denial_reason": denial_reason,
        }

    def claims(self, n: int, service_date: dt.date | None = None) -> list[dict]:
        return [self.claim(service_date) for _ in range(n)]


def next_batch_index(claim_ids, day_prefix: str) -> int:
    """Next batch number for a day, from existing claim ids.

    Scans ids like CLM-61116-B03-000042 for the day's prefix and returns one
    more than the highest batch seen. A day with only unbatched ids (or no
    ids yet) starts at 1.
    """
    highest = 0
    marker = f"{day_prefix}-B"
    for cid in claim_ids:
        if not cid.startswith(marker):
            continue
        try:
            number = int(cid[len(marker):len(marker) + 2])
        except ValueError:
            continue
        highest = max(highest, number)
    return highest + 1
