# Deployment Scripts

This directory stores helper scripts used by the GitHub Actions deployment workflow and local operators.

## `deploy.sh`

Usage:

```
./scripts/deployment/deploy.sh <environment>
```

Supported environments:

- `dev`
- `staging`
- `production`

The script expects the following environment variables (usually injected by CI/CD):

- `REGISTRY_URL` – Container registry host (default `ghcr.io`).
- `IMAGE_TAG` – Image tag to deploy (commit SHA or release tag).
- `CLOUD_PROVIDER` – Friendly identifier (`azure`, `aws`, `gcp`) used for logging.
- `DEPLOYMENT_STRATEGY` – `rolling`, `blue-green`, or `canary` (informational).
- Any provider-specific credentials exported before invocation (e.g., `AZURE_*`, `AWS_*`).

Current behaviour echoes the planned operations so the workflow can be wired in safely before live credentials exist. Replace the placeholders with `kubectl`, `helm`, or Terraform commands as infrastructure becomes available.

## Extending the Scripts

- Add environment-specific configuration files under `config/environment/`.
- Introduce smoke test scripts (e.g., `scripts/deployment/smoke-tests.sh`) and call them from `deploy.sh`.
- Log deployment metadata (git SHA, user, timestamp) to centralized storage once persistence is available.

