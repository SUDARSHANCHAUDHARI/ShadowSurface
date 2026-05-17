"""CLI for ShadowSurface MVP."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from apps.api.app.services.domain_scanner import load_scan, normalize_scan
from apps.api.app.services.exposure_checker import analyze_exposure
from apps.api.app.services.port_scanner import analyze_ports
from apps.api.app.services.scheduler import next_schedule
from apps.api.app.services.ssl_checker import analyze_ssl
from apps.api.app.services.subdomain_finder import analyze_subdomains

POINTS = {"critical": 50, "high": 30, "medium": 15, "low": 5}


def analyze(scan: dict) -> tuple[list[dict], dict]:
    scan = normalize_scan(scan)
    findings = [
        *analyze_subdomains(scan["subdomains"]),
        *analyze_ports(scan["ports"]),
        *analyze_ssl(scan["ssl"]),
        *analyze_exposure(scan["paths"], scan["headers"]),
    ]
    summary = {
        "domain": scan["domain"],
        "findings": len(findings),
        "risk_score": min(100, sum(POINTS.get(f["severity"], 0) for f in findings)),
        "by_severity": dict(Counter(f["severity"] for f in findings)),
        "schedule": next_schedule(),
    }
    return findings, summary


def report(summary: dict, findings: list[dict]) -> str:
    lines = ["# ShadowSurface Report", "", f"- Domain: {summary['domain']}", f"- Findings: {summary['findings']}", f"- Risk score: {summary['risk_score']}/100", "", "## Findings", ""]
    for finding in findings:
        lines.extend([f"### {finding['summary']}", "", f"- Severity: `{finding['severity']}`", f"- Type: `{finding['kind']}`", f"- Evidence: `{finding.get('evidence', {})}`", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="ShadowSurface offline exposure scanner")
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()
    scan = load_scan(args.fixture)
    findings, summary = analyze(scan)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "report.md").write_text(report(summary, findings), encoding="utf-8")
    print(f"Generated {summary['findings']} finding(s)")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
