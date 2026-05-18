# ShadowSurface Triage

- Domain: example.test
- Risk level: high
- Risk score: 100/100

## Remediation Checklist

- [ ] `high` Renew and deploy the certificate before expiry. (`ssl.expiry`)
- [ ] `high` Require authentication, IP allow-listing, or remove public admin routes. (`surface.exposed_admin_path`)
- [ ] `high` Require authentication, IP allow-listing, or remove public admin routes. (`surface.exposed_admin_path`)
- [ ] `high` Limit exposure with firewall rules, VPN access, or service hardening. (`surface.risky_open_port`)
- [ ] `medium` Add a Content-Security-Policy header appropriate for the application. (`headers.csp_missing`)
- [ ] `medium` Enable Strict-Transport-Security after confirming HTTPS is stable. (`headers.hsts_missing`)
- [ ] `medium` Limit exposure with firewall rules, VPN access, or service hardening. (`surface.risky_open_port`)
- [ ] `medium` Review whether this environment should be public and restrict access if it is internal. (`surface.sensitive_subdomain`)
- [ ] `medium` Review whether this environment should be public and restrict access if it is internal. (`surface.sensitive_subdomain`)
