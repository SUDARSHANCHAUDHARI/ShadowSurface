# ShadowSurface

**Goal:** Attack surface monitoring platform.

**MVP:** Add domain, scan common exposure risks.

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

## Repository Status

This repository contains the production-ready foundation for the ShadowSurface MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
