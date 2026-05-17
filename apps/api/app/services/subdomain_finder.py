"""Subdomain analysis."""

from __future__ import annotations


SENSITIVE_NAMES = ("admin", "dev", "staging", "test", "internal")


def analyze_subdomains(subdomains: list[str]) -> list[dict]:
    """Flag sensitive subdomain names."""
    findings = []
    for subdomain in subdomains:
        first = subdomain.split(".", 1)[0].lower()
        if first in SENSITIVE_NAMES:
            findings.append(
                {
                    "kind": "surface.sensitive_subdomain",
                    "severity": "medium",
                    "summary": "Sensitive environment subdomain is exposed.",
                    "evidence": {"subdomain": subdomain},
                }
            )
    return findings
