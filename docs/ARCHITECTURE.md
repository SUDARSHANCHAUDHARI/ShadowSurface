# Architecture

ShadowSurface is a defensive attack-surface monitoring MVP for domain exposure.

## Flow

1. `domain_scanner.py` loads and normalizes local scan fixtures.
2. `subdomain_finder.py` flags sensitive subdomain names.
3. `port_scanner.py` flags risky open ports.
4. `ssl_checker.py` checks certificate expiry.
5. `exposure_checker.py` checks exposed admin paths and missing headers.
6. `cli.py` writes findings, summary, Markdown report, and triage output.

## Outputs

- findings JSON
- summary JSON
- Markdown risk report
- Markdown remediation checklist

The MVP is offline and fixture-based. It does not scan live domains.
