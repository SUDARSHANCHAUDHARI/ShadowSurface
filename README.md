# ShadowSurface

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Attack surface monitoring MVP for domains, SSL, ports, exposed admin paths, headers, and subdomain risks.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/ShadowSurface
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/ShadowSurface`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- subdomain discovery
- SSL expiry check
- open port scan
- exposed admin panel check
- security header scan
- scheduled monitoring

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

## MVP Capabilities

- Analyzes offline domain scan fixtures.
- Flags sensitive subdomains.
- Flags risky open ports.
- Checks SSL expiry.
- Detects exposed admin paths.
- Checks missing CSP and HSTS headers.
- Writes JSON findings, JSON summary, and a Markdown report.

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
