# Prototype boundaries

Current core: Validated deployment-stage planning and digest-only artifact references.

Pending: Azure DevOps adapter, Bicep infrastructure, Key Vault integration, AKS sandbox validation.

Use synthetic inputs only. The prototype is not an authorization boundary. Cloud collectors must be read-only by default; deployments require explicit sandbox configuration and reviewed credentials. Do not commit tokens, Terraform state, real inventory, customer data or secrets. Supplied signature evidence is not cryptographic verification.

## Validation
Executable checks cover focused domain behavior. GitHub Actions results are the source of remote verification. No benchmark or production readiness is claimed.
