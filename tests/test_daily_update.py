"""End-to-end smoke test of an update round in a temporary project root."""
import csv
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "daily_update.py"


def load_script():
    spec = importlib.util.spec_from_file_location("daily_update_under_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_two_rounds_add_batches_and_write_full_report(tmp_path, capsys):
    mod = load_script()
    assert mod.main(root=tmp_path) == 0
    assert mod.main(root=tmp_path) == 0
    out = capsys.readouterr().out
    assert "batch B01" in out and "batch B02" in out          # each round adds a new batch
    with (tmp_path / "data" / "claims.csv").open() as fh:
        assert len(list(csv.DictReader(fh))) == 2 * mod.BATCH_SIZE
    md = (tmp_path / "reports" / "claims_report.md").read_text()
    for section in ("## Monthly financials", "## Data quality gates", "## Cost sharing by plan",
                    "## Paid-amount concentration", "## Procedures behind the top denial reasons"):
        assert section in md
    assert "synthetic" in md.lower()
    assert (tmp_path / "reports" / "monthly_financials.png").exists()


def test_corrupted_store_fails_the_round(tmp_path, capsys):
    mod = load_script()
    assert mod.main(root=tmp_path) == 0
    store = tmp_path / "data" / "claims.csv"
    rows = list(csv.DictReader(store.open()))
    fields = list(rows[0])
    rows[0]["paid_amount"] = str(float(rows[0]["allowed_amount"]) + 500)   # paid over allowed
    with store.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    capsys.readouterr()
    assert mod.main(root=tmp_path) == 1
    assert "QUALITY ISSUE" in capsys.readouterr().out
    assert "FAIL" in (tmp_path / "reports" / "claims_report.md").read_text()


def test_report_only_is_repeat_safe_and_adds_no_batch(tmp_path):
    mod = load_script()
    assert mod.main(root=tmp_path) == 0
    store = (tmp_path / "data" / "claims.csv")
    before = store.read_bytes()
    assert mod.main(root=tmp_path, report_only=True) == 0
    assert mod.main(root=tmp_path, report_only=True) == 0
    assert store.read_bytes() == before                      # store untouched
    assert (tmp_path / "reports" / "claims_report.md").exists()


def test_report_only_without_store_fails_cleanly(tmp_path):
    assert load_script().main(root=tmp_path, report_only=True) == 1
