"""Exposure checks."""

from __future__ import annotations


ADMIN_PATHS = ("/admin", "/dashboard", "/wp-admin", "/manage")


def analyze_exposure(paths: list[str], headers: dict) -> list[dict]:
    """Return exposed path and header findings."""
    findings = []
    for path in paths:
        if path.lower() in ADMIN_PATHS:
            findings.append(
                {
                    "kind": "surface.exposed_admin_path",
                    "severity": "high",
                    "summary": "Admin-style path appears exposed.",
                    "evidence": {"path": path},
                }
            )
    normalized = {str(k).lower(): str(v) for k, v in headers.items()}
    if "content-security-policy" not in normalized:
        findings.append({"kind": "headers.csp_missing", "severity": "medium", "summary": "CSP header is missing.", "evidence": {}})
    if "strict-transport-security" not in normalized:
        findings.append({"kind": "headers.hsts_missing", "severity": "medium", "summary": "HSTS header is missing.", "evidence": {}})
    return findings
