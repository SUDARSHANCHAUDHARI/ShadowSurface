# ShadowSurface

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Attack surface monitoring tool. Scans domains, subdomains, SSL certificates, open ports, exposed admin paths, and security headers to surface external-facing risk for a single domain or a fleet.

---

## Overview

ShadowSurface is a defensive reconnaissance tool that builds an external attack surface picture for a domain you own. It enumerates subdomains, checks SSL certificate validity and expiry, scans known ports, flags exposed admin paths and dev endpoints, and audits security headers. Outputs include a prioritized risk-scored inventory plus an analyst handoff report.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Subdomain enumeration from a seed domain
- SSL certificate inspection (validity, expiry, issuer)
- Common port scan
- Exposed admin and dev path detection
- Security header audit
- Risk scoring per finding and per asset
- Outputs JSON findings, risk summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container
- Network access for live scanning (fixture mode works offline)

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/ShadowSurface.git
cd ShadowSurface
pip install .
```

This registers the `shadow-surface` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Audit the included fixture domain:

```bash
python3 main.py --fixture data/samples/domain-fixture.json --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `findings.json` — all detected surface findings
- `subdomains.json` — enumerated subdomains
- `ssl.json` — SSL certificate inspection results
- `ports.json` — port scan results
- `headers.json` — security header audit
- `summary.json` — risk score and severity breakdown
- `report.md` — Markdown attack surface report
- `triage.md` — analyst triage checklist

## Project Structure

```
ShadowSurface/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js dashboard scaffold (planned)
├── data/
│   ├── samples/    Safe sample domain fixtures
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── scripts/        Setup, seed, run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only on domains, subdomains, and IP ranges you own or have explicit written permission to scan. Unauthorized scanning is illegal in many jurisdictions.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Live subdomain enumeration via passive DNS sources
- Configurable port list per scan profile
- Scheduled recurring scans with delta alerts
- Web dashboard for asset inventory and trending
- GitHub release `v0.1.0-mvp`

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/ShadowSurface/issues).
