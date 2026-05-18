# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic attack-surface fixture checks, risk summary, report output, triage output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add explicit authorization before live domain scanning.
- Add tests for malformed fixtures and missing SSL fields.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling customer domains.
- Run dependency and secret scans before release.
- Add scan rate limits, timeouts, and retention controls.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports include risk level, category breakdown, recommended actions, and triage checklist.
