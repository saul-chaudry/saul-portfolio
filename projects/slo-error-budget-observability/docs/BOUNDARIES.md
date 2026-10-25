# Prototype boundaries

Current core: SLO arithmetic, burn-rate evaluation and a sample recording-rule template.

Pending: Instrumented sample service, Grafana dashboard, burn-alert validation, runbook drill.

Use synthetic inputs only. The prototype is not an authorization boundary. Cloud collectors must be read-only by default; deployments require explicit sandbox configuration and reviewed credentials. Do not commit tokens, Terraform state, real inventory, customer data or secrets. Supplied signature evidence is not cryptographic verification.

## Validation
Executable checks cover focused domain behavior. GitHub Actions results are the source of remote verification. No benchmark or production readiness is claimed.
