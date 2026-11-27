# Known generator simplifications

All data in this repo is synthetic. These are the simplifications that matter when reading any report or metric. None of them is a defect to hide; each is a reason not to treat a number as real payer behavior.

| Area | What the generator does | Read it as |
| --- | --- | --- |
| Plan type and age band | A fixed label per member, drawn at random | A label only. No benefits, eligibility or clinical realism. Differences between plans are random draws. |
| Denial status and reason | Status drawn from fixed weights; reasons drawn at random, except "duplicate claim", which needs a real earlier claim | Plan, age and procedure do not drive denials, so the independence test is expected to show no association. |
| Allowed amount on denied claims | Most denied claims keep a nominal allowed amount; duplicate denials carry none | Denied allowed/billed is not a payer decision. Paid is always zero on denied claims. |
| "adjusted" status | A label with no separate adjustment logic | Expected to look like "paid". |
| Service dates | Each daily batch spreads dates over 90 days (see service-date-redistribution.md) | Monthly views are generator-shaped, not utilization trends. |
| Members | Assigned uniformly at random, no enrollment data | Zero-claim members are invisible; the dispersion ratio is indicative only. |
| Denial categories | A simplified teaching taxonomy over five reasons | Not an industry standard, not coding advice. |
| Procedure and diagnosis codes, amounts | Illustrative codes and ranges | Not authoritative coding or contract rates. |

Quality gates (`python scripts/query.py gates`) check internal consistency of the store, not realism.
