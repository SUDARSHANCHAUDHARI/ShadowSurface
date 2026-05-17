"""SSL analysis."""

from __future__ import annotations

from datetime import date, datetime


def analyze_ssl(ssl: dict, today: date | None = None) -> list[dict]:
    """Return SSL expiry findings."""
    if not ssl:
        return [{"kind": "ssl.missing", "severity": "high", "summary": "SSL metadata is missing.", "evidence": {}}]
    today = today or date.today()
    expires = datetime.fromisoformat(str(ssl.get("expires_on"))).date()
    days = (expires - today).days
    if days < 0:
        severity = "critical"
        summary = "SSL certificate is expired."
    elif days <= 14:
        severity = "high"
        summary = "SSL certificate expires soon."
    else:
        return []
    return [{"kind": "ssl.expiry", "severity": severity, "summary": summary, "evidence": {"expires_on": str(expires), "days_remaining": days}}]
