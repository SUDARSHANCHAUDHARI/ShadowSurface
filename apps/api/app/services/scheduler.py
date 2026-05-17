"""Monitoring schedule helper."""

from __future__ import annotations


def next_schedule(interval_hours: int = 24) -> dict:
    """Return simple schedule metadata."""
    return {"interval_hours": interval_hours, "mode": "recurring"}
