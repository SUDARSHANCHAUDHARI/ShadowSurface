# ShadowSurface Report

- Domain: example.test
- Findings: 9
- Risk score: 100/100

## Findings

### Sensitive environment subdomain is exposed.

- Severity: `medium`
- Type: `surface.sensitive_subdomain`
- Evidence: `{'subdomain': 'admin.example.test'}`

### Sensitive environment subdomain is exposed.

- Severity: `medium`
- Type: `surface.sensitive_subdomain`
- Evidence: `{'subdomain': 'dev.example.test'}`

### SSH port is exposed.

- Severity: `medium`
- Type: `surface.risky_open_port`
- Evidence: `{'open': True, 'port': 22}`

### Elasticsearch port is exposed.

- Severity: `high`
- Type: `surface.risky_open_port`
- Evidence: `{'open': True, 'port': 9200}`

### SSL certificate expires soon.

- Severity: `high`
- Type: `ssl.expiry`
- Evidence: `{'expires_on': '2026-05-20', 'days_remaining': 3}`

### Admin-style path appears exposed.

- Severity: `high`
- Type: `surface.exposed_admin_path`
- Evidence: `{'path': '/admin'}`

### Admin-style path appears exposed.

- Severity: `high`
- Type: `surface.exposed_admin_path`
- Evidence: `{'path': '/dashboard'}`

### CSP header is missing.

- Severity: `medium`
- Type: `headers.csp_missing`
- Evidence: `{}`

### HSTS header is missing.

- Severity: `medium`
- Type: `headers.hsts_missing`
- Evidence: `{}`
