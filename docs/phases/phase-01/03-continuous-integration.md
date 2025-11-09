# Phase 01 · Track 03 — Continuous Integration Baseline

Convert the skeleton CI into a comprehensive quality gate.

## A. Yarn Script Implementation
- [ ] Implement real `lint` scripts per workspace (ESLint/Prettier checks).
- [ ] Wire `test` scripts to actual test runners (Jest/Vitest) with watch disabled in CI.
- [ ] Add `typecheck` (TypeScript `tsc --noEmit`, `pyright`, etc.).
- [ ] Update root scripts to run all workspace targets sequentially.

## B. Workflow Enhancements
- [ ] Cache Yarn dependencies with fallback (if cache miss, install fresh).
- [ ] Upload test results and coverage via `actions/upload-artifact`.
- [ ] Fail build on uncovered or skipped tests above threshold.
- [ ] Introduce separate `jobs` for backend, frontend, and shared libs in parallel.

## C. Security & Compliance
- [ ] Add `yarn audit` / `npm audit` or use `oss-index` for dependency scanning.
- [ ] Integrate container scanning (Trivy, Grype) on Docker build outputs.
- [ ] Run secret scanning (gitleaks) as part of PR checks.
- [ ] Enforce license policy using `license-checker`.

## D. Developer Feedback
- [ ] Enable GitHub Action summary with key metrics and links.
- [ ] Configure Slack/Teams webhook for failed run notifications.
- [ ] Add badges to `README.md` for CI status and coverage.
- [ ] Document re-run procedures and known flaky test handling.

