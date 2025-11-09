# CI/CD Overview

This repository uses GitHub Actions for continuous integration and lays the foundation for automated deployments across environments.

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

### Extending CI

- Add real lint/test commands in each workspace and have the root scripts invoke them.  
- Expand the matrix when new services or Docker images are added.  
- Publish build artifacts (coverage reports, static assets, etc.) as needed with additional steps.

## Continuous Delivery

- Use environments (`dev`, `staging`, `production`) in GitHub with required approvals and secrets to enable safe deployments.  
- Author a `deploy` workflow that promotes build artifacts or Docker images to the target environment. A common pattern is to trigger deployment on `workflow_dispatch` with an environment input, run integration tests, and apply Kubernetes manifests (`infrastructure/kubernetes`) or Terraform changes (`infrastructure/terraform`).  
- Store required credentials (cloud providers, container registries, Kubernetes contexts) as encrypted GitHub Actions secrets referenced by the workflow.

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

## Observability & Follow-Up Work

- Integrate automated security scanning (Snyk, Trivy, or similar) into the CI pipeline.  
- Upload test coverage to the analytics service of choice.  
- Configure notifications (Slack, email) for failed CI/CD runs.  
- Add end-to-end and performance suites from `tests/` once implemented.

