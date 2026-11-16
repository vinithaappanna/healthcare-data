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
