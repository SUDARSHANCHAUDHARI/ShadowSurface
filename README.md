# ShadowSurface

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Attack surface monitoring MVP for domains, SSL, ports, exposed admin paths, headers, and subdomain risks.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/ShadowSurface
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/ShadowSurface`

## MVP Snapshot

This repository includes a working MVP with safe domain scan fixtures, deterministic exposure checks, JSON outputs, Markdown risk report, triage checklist, tests, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- subdomain discovery
- SSL expiry check
- open port scan
- exposed admin panel check
- security header scan
- scheduled monitoring
- risk level and category breakdown
- remediation checklist

## Suggested Stack

FastAPI, React, scheduled workers, Docker.

## Status

Working CLI MVP.

## Quick Start

Analyze the included domain scan fixture:

```bash
python3 -m apps.api.app.cli --fixture data/samples/domain-scan.json --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Generated outputs:

- `data/reports/findings.json`
- `data/reports/summary.json`
- `data/reports/report.md`
- `data/reports/triage.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Analyzes offline domain scan fixtures.
- Flags sensitive subdomains.
- Flags risky open ports.
- Checks SSL expiry.
- Detects exposed admin paths.
- Checks missing CSP and HSTS headers.
- Writes JSON findings, JSON summary, and a Markdown report.
- Adds risk level, category breakdown, recommended actions, priority queue, and triage checklist.

## Roadmap

- Add authorized live scan adapter
- Add DNS and certificate history import
- Add scheduled drift monitoring
- Add dashboard for domain exposure over time
- Add alert routing and export bundles
