# Phase 01 · Track 01 — Repository & Tooling Setup

Granular tasks to enable consistent collaboration and automation.

## A. GitHub Administration
- [ ] Enable branch protection on `main` (require PR, status checks, linear history).
- [ ] Configure CODEOWNERS for critical directories (`src/backend`, `src/frontend`, `infrastructure`).
- [ ] Turn on Dependabot alerts and security updates.
- [ ] Create default issue templates (`bug`, `feature`, `ops`, `doc`).
- [ ] Set up project board columns: `Backlog`, `Selected`, `In Progress`, `Review`, `Done`.

## B. Editor & Formatting Standards
- [ ] Add `.editorconfig` with whitespace, newline, charset rules.
- [ ] Adopt Prettier config shared across JS/TS workspaces.
- [ ] Align ESLint base rules with desired strictness (airbnb/base or custom).
- [ ] Define Stylelint config for CSS/SCSS modules if needed.
- [ ] Document formatting commands in `CONTRIBUTING.md`.

## C. Package & Workspace Management
- [ ] Audit workspaces to ensure Yarn Plug’n’Play (or classic) is consistent.
- [ ] Configure root `package.json` scripts to proxy service-level commands.
- [ ] Cache dependencies in CI using `.yarn/cache` or standard Yarn cache dir.
- [ ] Generate yarn.lock for deterministic builds.

## D. Documentation & Onboarding
- [ ] Draft `CONTRIBUTING.md` with PR process, testing expectations, commit conventions.
- [ ] Add `docs/development-setup.md` covering prerequisites and first-run steps.
- [ ] Record architecture overview short video or diagram for newcomers.
- [ ] Define communication channels (Slack, Teams) with decision logs.

## E. Automation Hooks
- [ ] Implement Git hooks via Husky (pre-commit lint, pre-push test).
- [ ] Configure semantic-release or conventional commits tooling if desired.
- [ ] Integrate pull request template referencing checklist items above.

