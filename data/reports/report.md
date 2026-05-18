# ShadowSurface Report

- Domain: example.test
- Findings: 9
- Risk score: 100/100
- Risk level: high

## Priority Queue

1. `ssl.expiry` - high - SSL certificate expires soon.
2. `surface.exposed_admin_path` - high - Admin-style path appears exposed.
3. `surface.exposed_admin_path` - high - Admin-style path appears exposed.
4. `surface.risky_open_port` - high - Elasticsearch port is exposed.
5. `headers.csp_missing` - medium - CSP header is missing.
6. `headers.hsts_missing` - medium - HSTS header is missing.
7. `surface.risky_open_port` - medium - SSH port is exposed.
8. `surface.sensitive_subdomain` - medium - Sensitive environment subdomain is exposed.
9. `surface.sensitive_subdomain` - medium - Sensitive environment subdomain is exposed.

## Findings

### SSL certificate expires soon.

- Severity: `high`
- Type: `ssl.expiry`
- Evidence: `{"days_remaining": 1, "expires_on": "2026-05-20"}`
- Recommended action: Renew and deploy the certificate before expiry.

### Admin-style path appears exposed.

- Severity: `high`
- Type: `surface.exposed_admin_path`
- Evidence: `{"path": "/admin"}`
- Recommended action: Require authentication, IP allow-listing, or remove public admin routes.

### Admin-style path appears exposed.

- Severity: `high`
- Type: `surface.exposed_admin_path`
- Evidence: `{"path": "/dashboard"}`
- Recommended action: Require authentication, IP allow-listing, or remove public admin routes.

### Elasticsearch port is exposed.

- Severity: `high`
- Type: `surface.risky_open_port`
- Evidence: `{"open": true, "port": 9200}`
- Recommended action: Limit exposure with firewall rules, VPN access, or service hardening.

### CSP header is missing.

- Severity: `medium`
- Type: `headers.csp_missing`
- Evidence: `{}`
- Recommended action: Add a Content-Security-Policy header appropriate for the application.

### HSTS header is missing.

- Severity: `medium`
- Type: `headers.hsts_missing`
- Evidence: `{}`
- Recommended action: Enable Strict-Transport-Security after confirming HTTPS is stable.

### SSH port is exposed.

- Severity: `medium`
- Type: `surface.risky_open_port`
- Evidence: `{"open": true, "port": 22}`
- Recommended action: Limit exposure with firewall rules, VPN access, or service hardening.

### Sensitive environment subdomain is exposed.

- Severity: `medium`
- Type: `surface.sensitive_subdomain`
- Evidence: `{"subdomain": "admin.example.test"}`
- Recommended action: Review whether this environment should be public and restrict access if it is internal.

### Sensitive environment subdomain is exposed.

- Severity: `medium`
- Type: `surface.sensitive_subdomain`
- Evidence: `{"subdomain": "dev.example.test"}`
- Recommended action: Review whether this environment should be public and restrict access if it is internal.
