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
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
RECOMMENDED_ACTIONS = {
    "surface.sensitive_subdomain": "Review whether this environment should be public and restrict access if it is internal.",
    "surface.risky_open_port": "Limit exposure with firewall rules, VPN access, or service hardening.",
    "ssl.expiry": "Renew and deploy the certificate before expiry.",
    "surface.exposed_admin_path": "Require authentication, IP allow-listing, or remove public admin routes.",
    "headers.csp_missing": "Add a Content-Security-Policy header appropriate for the application.",
    "headers.hsts_missing": "Enable Strict-Transport-Security after confirming HTTPS is stable.",
}


def risk_level(score: int) -> str:
    if score >= 80:
        return "high"
    if score >= 45:
        return "medium"
    return "low"


def enrich_findings(findings: list[dict]) -> list[dict]:
    enriched = []
    for finding in findings:
        item = dict(finding)
        item["recommended_action"] = RECOMMENDED_ACTIONS.get(item["kind"], "Review and remediate this exposure.")
        enriched.append(item)
    return sorted(enriched, key=lambda item: (SEVERITY_ORDER.get(item["severity"], 9), item["kind"]))


def analyze(scan: dict) -> tuple[list[dict], dict]:
    scan = normalize_scan(scan)
    findings = enrich_findings([
        *analyze_subdomains(scan["subdomains"]),
        *analyze_ports(scan["ports"]),
        *analyze_ssl(scan["ssl"]),
        *analyze_exposure(scan["paths"], scan["headers"]),
    ])
    score = min(100, sum(POINTS.get(f["severity"], 0) for f in findings))
    summary = {
        "domain": scan["domain"],
        "findings": len(findings),
        "risk_score": score,
        "risk_level": risk_level(score),
        "by_severity": dict(Counter(f["severity"] for f in findings)),
        "by_category": dict(Counter(f["kind"].split(".", 1)[0] for f in findings)),
        "top_priority": findings[0] if findings else None,
        "schedule": next_schedule(),
    }
    return findings, summary


def report(summary: dict, findings: list[dict]) -> str:
    lines = [
        "# ShadowSurface Report",
        "",
        f"- Domain: {summary['domain']}",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        f"- Risk level: {summary['risk_level']}",
        "",
        "## Priority Queue",
        "",
    ]
    for index, finding in enumerate(findings, start=1):
        lines.append(f"{index}. `{finding['kind']}` - {finding['severity']} - {finding['summary']}")
    lines.extend(["", "## Findings", ""])
    for finding in findings:
        lines.extend([
            f"### {finding['summary']}",
            "",
            f"- Severity: `{finding['severity']}`",
            f"- Type: `{finding['kind']}`",
            f"- Evidence: `{json.dumps(finding.get('evidence', {}), sort_keys=True)}`",
            f"- Recommended action: {finding['recommended_action']}",
            "",
        ])
    return "\n".join(lines)


def triage_report(summary: dict, findings: list[dict]) -> str:
    lines = [
        "# ShadowSurface Triage",
        "",
        f"- Domain: {summary['domain']}",
        f"- Risk level: {summary['risk_level']}",
        f"- Risk score: {summary['risk_score']}/100",
        "",
        "## Remediation Checklist",
        "",
    ]
    if not findings:
        lines.append("No remediation items were generated.")
    for finding in findings:
        lines.append(f"- [ ] `{finding['severity']}` {finding['recommended_action']} (`{finding['kind']}`)")
    return "\n".join(lines).rstrip() + "\n"


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
    (args.out_dir / "triage.md").write_text(triage_report(summary, findings), encoding="utf-8")
    print(f"Generated {summary['findings']} finding(s)")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
