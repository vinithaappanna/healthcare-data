import json

from healthdata import cli
from healthdata.pipeline import Pipeline


def make_valid(claim_id, **overrides):
    claim = {
        "claim_id": claim_id, "member_id": "MBR-0001", "plan_type": "PPO",
        "age_band": "30-44", "service_date": "2026-11-01",
        "procedure_code": "99213", "diagnosis_code": "I10",
        "billed_amount": 100.0, "allowed_amount": 80.0,
        "paid_amount": 60.0, "status": "paid", "denial_reason": "",
    }
    claim.update(overrides)
    return claim


def store(tmp_path):
    path = tmp_path / "c.csv"
    Pipeline(path).ingest([
        make_valid("CLM-A", member_id="MBR-0001", plan_type="PPO", billed_amount=100,
                   allowed_amount=80, paid_amount=60),
        make_valid("CLM-B", member_id="MBR-0001", plan_type="PPO", billed_amount=200,
                   allowed_amount=0, paid_amount=0, status="denied",
                   denial_reason="duplicate claim"),
        make_valid("CLM-C", member_id="MBR-0002", plan_type="HMO"),
    ])
    return path


def test_member_summary_totals(tmp_path):
    out = cli.member_summary(Pipeline(store(tmp_path)), "MBR-0001")
    assert out["claims"] == 2 and out["denied"] == 1
    assert out["billed"] == 300.0 and out["paid"] == 60.0
    assert out["claim_ids"] == ["CLM-A", "CLM-B"]
    assert cli.member_summary(Pipeline(store(tmp_path)), "NOPE") is None


def test_claim_and_plan_lookup_case_insensitive(tmp_path):
    pipe = Pipeline(store(tmp_path))
    assert cli.lookup_claim(pipe, "CLM-C")["plan_type"] == "HMO"
    assert cli.lookup_claim(pipe, "missing") is None
    assert cli.plan_summary(pipe, "ppo")["claims"] == 2


def test_main_prints_json_and_exit_codes(tmp_path, capsys):
    path = store(tmp_path)
    assert cli.main(["member", "MBR-0001"], store=path) == 0
    assert json.loads(capsys.readouterr().out)["claims"] == 2
    assert cli.main(["claim", "nope"], store=path) == 1
    assert "no claim found" in capsys.readouterr().out


def test_procedure_summary_math_and_reasons(tmp_path):
    out = cli.procedure_summary(Pipeline(store(tmp_path)), "99213")
    assert out["claims"] == 3 and out["denial_rate"] == 0.3333
    assert out["avg_billed"] == 133.33 and out["avg_paid_non_denied"] == 60.0
    assert out["denial_reasons"] == {"duplicate claim": 1}
    assert cli.procedure_summary(Pipeline(store(tmp_path)), "00000") is None


def test_diagnosis_summary_case_insensitive_and_all_denied(tmp_path):
    path = tmp_path / "d.csv"
    Pipeline(path).ingest([make_valid("CLM-X", diagnosis_code="E11.9", status="denied",
                                      paid_amount=0, allowed_amount=0, denial_reason="timely filing exceeded")])
    out = cli.diagnosis_summary(Pipeline(path), "e11.9")
    assert out["denial_rate"] == 1.0 and out["avg_paid_non_denied"] == 0.0  # no divide-by-zero
    assert out["denial_reasons"] == {"timely filing exceeded": 1}


def test_main_procedure_and_diagnosis_commands(tmp_path, capsys):
    path = store(tmp_path)
    assert cli.main(["procedure", "99213"], store=path) == 0
    assert json.loads(capsys.readouterr().out)["claims"] == 3
    assert cli.main(["diagnosis", "ZZZ"], store=path) == 1
    assert "no diagnosis found" in capsys.readouterr().out


def test_whole_store_commands_and_reconcile_exit_code(tmp_path, capsys):
    path = store(tmp_path)
    assert cli.main(["reconcile"], store=path) == 0
    rows = json.loads(capsys.readouterr().out)
    assert len(rows) == 8 and all(r["ok"] for r in rows)
    assert cli.main(["origins"], store=path) == 0
    n = len(Pipeline(path).load_store())
    assert json.loads(capsys.readouterr().out) == {"generated": n}
    assert cli.main(["bands"], store=path) == 0
    assert sum(b["claims"] for b in json.loads(capsys.readouterr().out)) == n
    # break the store: a blank plan makes the plan views drop that row, so exit code is 2
    import csv
    from healthdata.pipeline import FIELDNAMES
    rows_in = list(Pipeline(path).load_store().values())
    rows_in[0]["plan_type"] = ""
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDNAMES); w.writeheader(); w.writerows(rows_in)
    assert cli.main(["reconcile"], store=path) == 2


def test_summary_command(tmp_path, capsys):
    assert cli.main(["summary"], store=store(tmp_path)) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["claims"] == len(Pipeline(store_path := None or (tmp_path / "c.csv")).load_store())
    assert out["denial_rate"] > 0 and "generated" in out["origins"]


def test_months_command_prints_distribution(tmp_path, capsys):
    import json
    from healthdata.cli import main
    from healthdata.pipeline import Pipeline
    store = tmp_path / "c.csv"
    Pipeline(store).ingest([make_valid("A-1", service_date="2026-10-01")])
    assert main(["months"], store=store) == 0
    assert json.loads(capsys.readouterr().out)[0]["month"] == "2026-10"


def test_gates_command_reports_each_check_and_exit_code(tmp_path, capsys):
    import json
    from healthdata.cli import main
    from healthdata.pipeline import Pipeline
    store = tmp_path / "g.csv"
    Pipeline(store).ingest([make_valid("A-1", service_date="2026-10-01")])
    assert main(["gates"], store=store) == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 12 and all(g["ok"] for g in out) and out[0]["check"] == "amount consistency"
    # corrupt a row: paid above allowed
    import csv
    rows = list(csv.DictReader(store.open()))
    rows[0]["paid_amount"] = str(float(rows[0]["allowed_amount"]) + 50)
    with store.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    assert main(["gates"], store=store) == 2
    bad = [g for g in json.loads(capsys.readouterr().out) if not g["ok"]]
    assert bad[0]["check"] == "amount consistency" and bad[0]["issues"] == 1
    assert main(["gates"], store=tmp_path / "missing.csv") == 2


def test_denials_command_combines_category_and_plan_views(tmp_path, capsys):
    path = store(tmp_path)
    assert cli.main(["denials"], store=path) == 0
    out = json.loads(capsys.readouterr().out)
    assert [r["category"] for r in out["by_category"]] == ["billing error"]
    assert out["by_category"][0]["claims"] == 1 and out["by_category"][0]["share"] == 1.0
    plans = {r["plan"]: r for r in out["by_plan"]}
    assert plans["PPO"]["denied_billed"] == 200.0 and plans["HMO"]["denied_billed"] == 0.0
    assert "synthetic" in out["note"]
    assert cli.main(["denials"], store=tmp_path / "missing.csv") == 0     # empty store: empty views, not a crash
    assert json.loads(capsys.readouterr().out)["by_category"] == []
