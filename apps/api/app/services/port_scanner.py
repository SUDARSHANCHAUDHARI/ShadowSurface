"""Open port analysis."""

from __future__ import annotations


RISKY_PORTS = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 9200: "Elasticsearch"}


def analyze_ports(ports: list[dict]) -> list[dict]:
    """Return open port findings."""
    findings = []
    for item in ports:
        port = int(item.get("port", 0))
        if port in RISKY_PORTS and item.get("open", False):
            findings.append(
                {
                    "kind": "surface.risky_open_port",
                    "severity": "high" if port in {23, 3389, 9200} else "medium",
                    "summary": f"{RISKY_PORTS[port]} port is exposed.",
                    "evidence": item,
                }
            )
    return findings
