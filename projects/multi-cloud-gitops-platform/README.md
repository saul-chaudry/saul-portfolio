# Multi-Cloud Kubernetes Platform with GitOps

Saul Chaudry · Personal engineering lab · **Domain prototype**

## Problem and scope
Explore multi-cloud kubernetes platform with gitops with clear invariants, failure boundaries and repeatable checks.

## Implemented
Local validated GitOps environment generator for AWS and Azure targets.

The core is a local reference implementation. Target technologies below are not all integrated. This is not a production deployment or evidence of employment experience. Cloud availability, cost savings, recovery time and throughput have not been measured.

## Target architecture
```mermaid
flowchart LR
  input[Validated input] --> core[Domain rules]
  core --> outcome[Decision and audit result]
  core -. planned .-> adapters[Infrastructure adapters]
```

Target stack: Terraform, EKS, AKS, ArgoCD, Helm, Kustomize.

## Run the executable checks
Requires Python 3.11+. No third-party runtime dependencies are needed for the prototype.
```sh
python -m unittest discover -s tests -v
```

## Next milestones
- [ ] Terraform modules
- [ ] EKS and AKS sandbox builds
- [ ] ArgoCD sync
- [ ] promotion measurements

## Trade-offs
The domain logic is independent of infrastructure for quick failure-path checks. In-memory prototypes do not coordinate multiple machines or survive restarts. Authentication, persistent state, telemetry and real provider adapters must be verified before production use.

## Evidence and discussion
See `docs/BOUNDARIES.md`. Explain the input contract, failure behavior, consistency model, security boundary and the next integration test. Quote performance results only after recording the commit, workload, runtime, hardware, duration, latency, error rate and limitations.
