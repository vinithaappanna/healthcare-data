"""Synthetic claims generator.

Every record is invented by a seeded RNG - no real member, patient, provider
or plan data. The same seed always produces the same claims, which keeps
tests and demos reproducible.
"""
from __future__ import annotations

import datetime as dt
import hashlib
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
# "duplicate claim" is not drawn at random: it is only assigned to a claim that
# really repeats an earlier one (same member, procedure, service date).
RANDOM_DENIAL_REASONS = [r for r in DENIAL_REASONS if r != "duplicate claim"]
DUPLICATE_RATE = 0.03          # share of generated claims that repeat an earlier claim in the batch
DUPLICATE_CAUGHT = 0.7         # of those, share denied as "duplicate claim"; the rest still pay (leakage)

# Illustrative plausibility rules, not clinical guidance: age bands a code is
# not generated for.
AGE_RESTRICTED_PROCEDURES = {"27447": {"0-17"}}      # total knee replacement
AGE_RESTRICTED_DIAGNOSES = {"Z00.00": {"0-17"}}      # general ADULT medical exam
SERVICE_SPREAD_DAYS = 90      # daily batches spread service dates over this many trailing days
ORIGIN_REGENERATED = "regenerated-2026-11-21"        # data_origin of repaired history


def age_plausible(age_band: str, procedure_code: str, diagnosis_code: str) -> bool:
    return (age_band not in AGE_RESTRICTED_PROCEDURES.get(procedure_code, ())
            and age_band not in AGE_RESTRICTED_DIAGNOSES.get(diagnosis_code, ()))


def _frac(key: str) -> float:
    return int.from_bytes(hashlib.sha256(key.encode()).digest()[2:6], "big") / 2**32


def repair_age_plausibility(row: dict) -> bool:
    """Deterministically replace an age-implausible procedure or diagnosis on a
    stored row (in place). A new procedure is picked from the allowed list by
    hash of claim_id; billed is re-drawn inside its illustrative range and
    allowed/paid keep their original ratios, so amount rules and denial status
    still hold. Returns True when the row changed."""
    band, proc, dx = row["age_band"], row["procedure_code"], row["diagnosis_code"]
    changed = False
    if proc in AGE_RESTRICTED_PROCEDURES and band in AGE_RESTRICTED_PROCEDURES[proc]:
        ok = [p for p in PROCEDURES if band not in AGE_RESTRICTED_PROCEDURES.get(p[0], ())]
        code, _d, (lo, hi) = ok[int(_frac(row["claim_id"] + "p") * len(ok))]
        old_b = float(row["billed_amount"]) or 1.0
        allowed_ratio = float(row["allowed_amount"]) / old_b
        paid_ratio = (float(row["paid_amount"]) / float(row["allowed_amount"])
                      if float(row["allowed_amount"]) else 0.0)
        billed = round(lo + _frac(row["claim_id"] + "b") * (hi - lo), 2)
        allowed = round(billed * allowed_ratio, 2)
        row.update(procedure_code=code, billed_amount=billed, allowed_amount=allowed,
                   paid_amount=round(allowed * paid_ratio, 2))
        changed = True
    if dx in AGE_RESTRICTED_DIAGNOSES and band in AGE_RESTRICTED_DIAGNOSES[dx]:
        ok_dx = [d for d in DIAGNOSES if band not in AGE_RESTRICTED_DIAGNOSES.get(d[0], ())]
        row["diagnosis_code"] = ok_dx[int(_frac(row["claim_id"] + "d") * len(ok_dx))][0]
        changed = True
    return changed


def member_profile(member_id: str) -> tuple[str, str]:
    """Stable (plan_type, age_band) for a synthetic member id, derived from a
    hash so every claim for one member agrees (a member does not change plan
    or age band between claims in this toy dataset)."""
    h = hashlib.sha256(member_id.encode()).digest()
    return PLAN_TYPES[h[0] % len(PLAN_TYPES)], AGE_BANDS[h[1] % len(AGE_BANDS)]


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
        member_id = f"MBR-{rng.randrange(1, 2000):04d}"
        rng.choice(PLAN_TYPES), rng.choice(AGE_BANDS)   # keep the random stream unchanged
        plan, band = member_profile(member_id)
        return {"member_id": member_id, "plan_type": plan, "age_band": band}

    def claim(self, service_date: dt.date | None = None, spread_days: int | None = None) -> dict:
        rng = self._rng
        self._claim_seq += 1
        member = self._member()
        band = member["age_band"]
        code, _desc, (lo, hi) = rng.choice(
            [p for p in PROCEDURES if band not in AGE_RESTRICTED_PROCEDURES.get(p[0], ())])
        dx_code, _dx = rng.choice(
            [d for d in DIAGNOSES if band not in AGE_RESTRICTED_DIAGNOSES.get(d[0], ())])
        billed = round(rng.uniform(lo, hi), 2)
        status = rng.choices(STATUSES, weights=[78, 12, 10])[0]
        denial_reason = rng.choice(RANDOM_DENIAL_REASONS) if status == "denied" else ""
        allowed = round(billed * rng.uniform(0.6, 0.95), 2)
        paid = round(allowed * rng.uniform(0.7, 1.0), 2) if status != "denied" else 0.0
        if service_date and spread_days:
            # service_date is the latest day; each claim lands 0..spread_days-1 days earlier
            day = service_date - dt.timedelta(days=rng.randrange(spread_days))
        else:
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

    def _repeat_of(self, original: dict, service_date: dt.date | None,
                   spread_days: int | None = None) -> dict:
        """A claim that repeats `original` (same member, procedure, diagnosis,
        service date and billed amount) under a new claim id. Most are denied
        as "duplicate claim"; the rest are paid, which is what a leakage screen
        should find."""
        rng = self._rng
        dup = self.claim(service_date, spread_days)
        for key in ("member_id", "plan_type", "age_band", "service_date", "procedure_code",
                    "diagnosis_code", "billed_amount"):
            dup[key] = original[key]
        if rng.random() < DUPLICATE_CAUGHT:
            dup.update(status="denied", denial_reason="duplicate claim", allowed_amount=0.0, paid_amount=0.0)
        else:
            allowed = round(dup["billed_amount"] * rng.uniform(0.6, 0.95), 2)
            dup.update(status="paid", denial_reason="", allowed_amount=allowed,
                       paid_amount=round(allowed * rng.uniform(0.7, 1.0), 2))
        return dup

    def claims(self, n: int, service_date: dt.date | None = None,
               spread_days: int | None = None) -> list[dict]:
        """n claims. With service_date and spread_days, service dates spread
        over the spread_days ending at service_date (repeats keep their
        original's date); with service_date alone every claim gets that date."""
        out: list[dict] = []
        for _ in range(n):
            if out and self._rng.random() < DUPLICATE_RATE:
                original = self._rng.choice(out)
                out.append(self._repeat_of(original, service_date, spread_days))
            else:
                out.append(self.claim(service_date, spread_days))
        return out


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
