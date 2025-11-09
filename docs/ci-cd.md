# CI/CD Overview

This repository uses GitHub Actions for continuous integration and lays the foundation for automated deployments across environments.

The plan aligns directly with the phase roadmap in `docs/phases/`. Phase 01 establishes CI baselines, Phase 02 introduces deployment automation for core services, and later phases enrich the pipeline with analytics, AI governance, and reliability controls.

## Continuous Integration (`.github/workflows/ci.yml`)

The CI workflow runs on every pull request and on pushes to `main`. It performs two stages:

- **Install & Verify**  
  - Checks out the repository.  
  - Sets up Node.js 18 with Yarn caching.  
  - Installs dependencies via `yarn install --non-interactive --prefer-offline`.  
  - Executes the workspace-level `yarn lint`, `yarn test`, and `yarn typecheck` scripts, which can delegate to service-specific checks as they are implemented.

- **Build Docker Images**  
  - Builds container images for each backend service and the web application using BuildKit.  
  - Ensures all Dockerfiles stay buildable even when service code changes.  
  - Currently configured to build the following images: `api-gateway`, `application-service`, `auth-service`, `job-intelligence-service`, `resume-service`, `transparency-service`, `analytics-service`, and `web-app`.

### Extending CI (Phase 01 → Phase 03)

- Add real lint/test commands in each workspace and have the root scripts invoke them.  
- Expand the matrix when new services or Docker images are added.  
- Publish build artifacts (coverage reports, static assets, etc.) as needed with additional steps.
- Parallelize workloads by splitting backend, frontend, and shared libraries into distinct jobs once scripts exist.  
- Introduce secret scanning, dependency audits, and license checks (see `docs/phases/phase-01/03-continuous-integration.md`).  
- Publish coverage badges and Action summaries for quick triage.

### Branching & Reviews

- All feature work occurs on short-lived branches merged via pull request.  
- `main` remains deployable; branch protection enforces status checks, linear history, and review requirements.  
- Optionally adopt a `release/x.y` branch when cutting coordinated releases for schools with change-freeze periods.

## Continuous Delivery

- Use environments (`dev`, `staging`, `production`) in GitHub with required approvals and secrets to enable safe deployments.  
- Author a `deploy` workflow that promotes build artifacts or Docker images to the target environment. A common pattern is to trigger deployment on `workflow_dispatch` with an environment input, run integration tests, and apply Kubernetes manifests (`infrastructure/kubernetes`) or Terraform changes (`infrastructure/terraform`).  
- Store required credentials (cloud providers, container registries, Kubernetes contexts) as encrypted GitHub Actions secrets referenced by the workflow.
- Leverage environment-level protection rules:  
  - `dev`: auto-deploy on merge to `main`, no approval required.  
  - `staging`: gated by release manager approval plus automated smoke tests.  
  - `production`: requires business approval, mentor/school communication checklist, and post-deploy verification.
- Capture deployment metadata (commit, operator, change request) and publish to the deployment timeline dashboard (see `docs/phases/phase-05/03-deployment-automation.md`).

### Deployment Workflow (`.github/workflows/deploy.yml`)

1. **Build & Prepare Artifacts**  
   - Triggered manually with an `environment` input (`dev`, `staging`, `production`).  
   - Checks out the repo, installs dependencies, and archives deployment context (scripts, infrastructure manifests, environment config).  
   - Calculates the image tag (`workflow_dispatch` input or defaults to commit SHA).
2. **Deploy**  
   - Downloads the artifact bundle, configures cloud credentials (placeholder), and executes `scripts/deployment/deploy.sh <environment>`.  
   - The shell script maps the environment to Kubernetes namespaces and echoes planned Terraform/Kubernetes operations until real commands are wired in.  
   - Environment-level URLs (e.g., deployment dashboards) can be surfaced via GitHub environment variables.
3. **Verify & Notify**  
   - Post-deploy step reserved for smoke tests, SLO checks, and stakeholder notifications.  
   - Replace placeholders with actual scripting as `tests/e2e` and monitoring hooks become available.

## Local Validation

Before pushing changes, run:

```
yarn install
yarn lint
yarn test
yarn typecheck
```

For container changes, validate the build locally:

```
docker build -f src/backend/api-gateway/Dockerfile src/backend/api-gateway
```

For multi-service validation use docker-compose:

```
docker-compose up --build api-gateway auth-service resume-service
```

## Observability & Follow-Up Work

- Integrate automated security scanning (Snyk, Trivy, or similar) into the CI pipeline.  
- Upload test coverage to the analytics service of choice.  
- Configure notifications (Slack, email) for failed CI/CD runs.  
- Add end-to-end and performance suites from `tests/` once implemented.
- Track workflow metrics (run duration, queue time) to optimize concurrency limits.
- Align with Phase 05 plans for reliability, security, and governance to keep the pipeline audit-ready.

