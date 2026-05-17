"""Load and normalize domain scan data."""

from __future__ import annotations

import json
from pathlib import Path


def load_scan(path: Path) -> dict:
    """Load an offline domain scan fixture."""
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_scan(scan: dict) -> dict:
    """Ensure expected scan keys exist."""
    return {
        "domain": scan.get("domain", "unknown"),
        "subdomains": scan.get("subdomains", []),
        "ports": scan.get("ports", []),
        "ssl": scan.get("ssl", {}),
        "headers": scan.get("headers", {}),
        "paths": scan.get("paths", []),
    }
