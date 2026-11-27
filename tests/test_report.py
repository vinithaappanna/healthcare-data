"""Report rendering: markdown content and chart files."""
import datetime as dt

from healthdata import report

MONTHLY = [
    {"month": "2026-09", "claims": 40, "billed": 5000.0, "allowed": 4000.0,
     "paid": 3000.0, "denial_rate": 0.1},
    {"month": "2026-10", "claims": 55, "billed": 7000.0, "allowed": 5600.0,
     "paid": 4200.0, "denial_rate": 0.12},
]
REASONS = [("duplicate claim", 8), ("timely filing exceeded", 4)]
MIX = [("PPO", 50), ("HMO", 45)]


def test_markdown_has_key_sections():
    md = report.render_markdown(MONTHLY, REASONS, MIX, 95,
                                generated_at=dt.datetime(2026, 11, 16, 12, 0))
    assert "95 claims" in md
    assert "2026-10" in md
    assert "duplicate claim (8)" in md
    assert "synthetic" in md.lower()


def test_charts_render(tmp_path):
    assert report.plot_monthly_financials(MONTHLY, tmp_path / "m.png") is True
    assert (tmp_path / "m.png").stat().st_size > 0
    assert report.plot_denial_reasons(REASONS, tmp_path / "d.png") is True
    assert (tmp_path / "d.png").stat().st_size > 0


def test_charts_empty_input(tmp_path):
    assert report.plot_monthly_financials([], tmp_path / "x.png") is False
    assert report.plot_denial_reasons([], tmp_path / "y.png") is False


def test_plan_denial_chart_renders_and_handles_empty(tmp_path):
    perf = [{"plan": "PPO", "claims": 100, "denial_rate": 0.1, "paid_to_billed": 0.5},
            {"plan": "HMO", "claims": 50, "denial_rate": 0.2, "paid_to_billed": 0.4}]
    assert report.plot_plan_denial_rates(perf, tmp_path / "p.png") is True
    assert (tmp_path / "p.png").stat().st_size > 1000
    assert report.plot_plan_denial_rates([], tmp_path / "e.png") is False
    assert report.plot_plan_denial_rates(perf, tmp_path / "m.png", min_claims=500) is False   # all filtered out
    # zero-denial plans must not break the axis limits
    zero = [{"plan": "PPO", "claims": 10, "denial_rate": 0.0, "paid_to_billed": 0.6}]
    assert report.plot_plan_denial_rates(zero, tmp_path / "z.png") is True


def test_plan_performance_section_embeds_chart():
    md = report.render_markdown([], [], [], 0, plan_perf=[
        {"plan": "PPO", "claims": 2, "denial_rate": 0.5, "paid_to_billed": 0.3}])
    assert "plan_denial_rates.png" in md


def test_size_band_chart_renders_and_handles_empty(tmp_path):
    bands = [{"band": "under $100", "claims": 10, "claim_share": 0.5, "paid": 100.0, "paid_share": 0.1,
              "denial_rate": 0.0},
             {"band": "$10,000+", "claims": 10, "claim_share": 0.5, "paid": 900.0, "paid_share": 0.9,
              "denial_rate": 0.0}]
    assert report.plot_size_bands(bands, tmp_path / "s.png") is True
    assert (tmp_path / "s.png").stat().st_size > 1000
    assert report.plot_size_bands([], tmp_path / "e.png") is False
    assert report.plot_size_bands([dict(bands[0], claims=0)], tmp_path / "z.png") is False


def test_size_band_section_embeds_chart():
    row = {"band": "under $100", "claims": 3, "claim_share": 0.6, "paid": 120.0, "paid_share": 0.1,
           "denial_rate": 0.0}
    assert "size_bands.png" in report.render_markdown([], [], [], 0, size_bands=[row])


def test_plot_denial_categories_writes_png_and_skips_empty(tmp_path):
    cats = [{"category": "administrative process", "claims": 5, "billed": 500.0, "share": 0.5},
            {"category": "clinical review", "claims": 5, "billed": 1500.0, "share": 0.5}]
    out = tmp_path / "c.png"
    assert report.plot_denial_categories(cats, out) is True
    assert out.stat().st_size > 1000
    assert report.plot_denial_categories([], tmp_path / "none.png") is False
    assert not (tmp_path / "none.png").exists()
    assert report.plot_denial_categories([{"category": "x", "claims": 0, "billed": 0.0, "share": 0.0}], tmp_path / "z.png") is True


def test_limitations_doc_covers_known_simplifications_and_is_linked():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    doc = (root / "docs" / "generator-limitations.md").read_text()
    for phrase in ("adjusted", "nominal allowed amount", "Plan type and age band", "generator-shaped", "enrollment"):
        assert phrase in doc
    assert "docs/generator-limitations.md" in (root / "README.md").read_text()
