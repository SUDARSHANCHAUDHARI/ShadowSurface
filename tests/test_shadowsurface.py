"""Tests for ShadowSurface MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from apps.api.app.cli import analyze, triage_report
from apps.api.app.services.domain_scanner import load_scan
from apps.api.app.services.ssl_checker import analyze_ssl


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "data/samples/domain-scan.json"


class ShadowSurfaceTests(unittest.TestCase):
    def test_detects_surface_findings(self) -> None:
        findings, summary = analyze(load_scan(FIXTURE))
        kinds = {finding["kind"] for finding in findings}
        self.assertIn("surface.sensitive_subdomain", kinds)
        self.assertIn("surface.risky_open_port", kinds)
        self.assertIn("surface.exposed_admin_path", kinds)
        self.assertIn("headers.csp_missing", kinds)
        self.assertGreater(summary["risk_score"], 80)
        self.assertEqual("high", summary["risk_level"])
        self.assertIn("surface", summary["by_category"])
        self.assertIn("recommended_action", findings[0])

    def test_ssl_expiry(self) -> None:
        findings = analyze_ssl({"expires_on": "2026-05-20"}, today=date(2026, 5, 17))
        self.assertEqual(findings[0]["kind"], "ssl.expiry")

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, "-m", "apps.api.app.cli", "--fixture", str(FIXTURE), "--out-dir", tmp], cwd=ROOT, check=True, capture_output=True, text=True)
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            triage = Path(tmp, "triage.md").read_text(encoding="utf-8")
            self.assertIn("Risk score", result.stdout)
            self.assertGreaterEqual(summary["findings"], 7)
            self.assertIn("Remediation Checklist", triage)

    def test_builds_triage_report(self) -> None:
        findings, summary = analyze(load_scan(FIXTURE))
        triage = triage_report(summary, findings)

        self.assertIn("ShadowSurface Triage", triage)
        self.assertIn("Renew and deploy", triage)


if __name__ == "__main__":
    unittest.main()
