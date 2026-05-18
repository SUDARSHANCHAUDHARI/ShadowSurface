# Security Notes

ShadowSurface is defensive and monitoring-focused.

## Safe Use

- Scan only domains and infrastructure you own or have permission to assess.
- Do not commit private DNS inventories, customer domains, tokens, or internal scan results.
- Treat generated reports as sensitive because they identify exposed services and admin paths.

## Current Boundary

The MVP uses local JSON fixtures and does not perform live DNS, port, SSL, or HTTP scans.

## Before Production

- Add explicit target authorization.
- Add scan rate limits and timeouts.
- Add private IP and internal hostname redaction.
- Add audit logging and retention controls.
