# CareerLaunch AI – Build Plan

## Phase 0 – Foundations (Weeks 0-2)
- [ ] Establish local dev environment: Node.js 18, Yarn, Python 3.11, Docker Desktop.
- [ ] Configure Yarn workspaces and root tooling (ESLint, Prettier, TypeScript configs).
- [ ] Implement core shared libraries (logging, error handling, config loader).
- [ ] Stand up base microservices: `auth-service`, `api-gateway`, shared user profile service.
- [ ] Define PostgreSQL schema migrations for users, sessions, audit logs.
- [ ] Integrate Redis for session caching and rate limiting.
- [ ] Implement RBAC scaffolding and JWT-based access tokens.
- [ ] Set up CI pipeline (GitHub Actions) with linting, tests, Docker build.
- [ ] Configure infrastructure-as-code baselines (Terraform environment scaffolding).
- [ ] Instrument logging/metrics stack (Prometheus, Grafana dashboards skeleton).

## Phase 1 – Job Intelligence MVP (Weeks 3-8)
- [ ] Build job aggregation service with connectors for Indeed and LinkedIn APIs.
- [ ] Implement job deduplication logic across sources.
- [ ] Create enrichment pipelines: company intelligence lookup, salary estimation rules, skill extraction (spaCy).
- [ ] Index job postings into Elasticsearch; design search queries and filters.
- [ ] Develop `job-intelligence-service` REST/GraphQL endpoints.
- [ ] Build frontend job search experience (search UI, filters, job detail view).
- [ ] Create market heatmap visualizations with sample datasets.
- [ ] Implement ingestion scheduling (Temporal or BullMQ) and monitoring.
- [ ] Launch browser extension skeleton for manual application capture.
- [ ] Add unit/integration tests for aggregators and search API; run load test baseline.

## Phase 2 – Resume Transformation & Application Tracking (Weeks 9-16)
- [ ] Implement resume upload service with file storage (S3-compatible) and parsing (PDF, DOCX).
- [ ] Extract structured resume data (skills, experience, education) into normalized schema.
- [ ] Build ATS compliance checks and content scoring heuristics.
- [ ] Create resume optimization engine: template repository, keyword suggestion pipeline.
- [ ] Develop resume builder UI with real-time feedback.
- [ ] Implement application tracking service: statuses, events, manual entry, audit trail.
- [ ] Integrate email ingestion (IMAP/Gmail API) for auto status updates.
- [ ] Add calendar sync (Google/Outlook) for interview scheduling.
- [ ] Build dashboard for application pipeline, including notifications center.
- [ ] Expand browser extension for form capture and quick entry.
- [ ] Write automated tests for parsing, optimization, and tracking workflows.

## Phase 3 – Transparency Analytics (Weeks 17-24)
- [ ] Set up data warehouse ETL and anonymization pipelines.
- [ ] Compute applicant pool analytics (education, experience, skill distribution).
- [ ] Implement competitive positioning dashboards with comparison charts.
- [ ] Develop success probability scoring (v1 heuristic + feature explanations).
- [ ] Create application analytics widgets: timelines, response rates, ghosting alerts.
- [ ] Add WebSocket layer for live updates on dashboards.
- [ ] Enhance browser extension with cross-browser support and secure storage.
- [ ] Document data governance policies for privacy-compliant analytics.
- [ ] Expand automated testing to include analytics correctness and realtime flows.

## Phase 4 – Predictive Intelligence & Engagement (Weeks 25-32)
- [ ] Train ML models for success probability and skill ROI forecasting.
- [ ] Build ML service APIs with model versioning and monitoring.
- [ ] Implement personalized coaching service combining recommendations and learning paths.
- [ ] Introduce gamification: milestones, points, community leaderboards.
- [ ] Deliver salary negotiation intelligence and interview prep simulator MVPs.
- [ ] Create notification and messaging system (email, in-app, push).
- [ ] Build mobile (React Native/Flutter) prototype for dashboards and coaching.
- [ ] Instrument A/B testing framework and feature flag rollout rules.
- [ ] Extend testing suite with model evaluation pipelines and mobile smoke tests.

## Phase 5 – Hardening & Launch Prep (Weeks 33-40)
- [ ] Conduct scalability testing; optimize caching, database queries, event throughput.
- [ ] Complete security hardening: MFA, audit logs, penetration testing remediation.
- [ ] Finalize compliance artifacts (GDPR/CCPA, accessibility audits, SLA docs).
- [ ] Localize platform to Spanish/French; validate WCAG 2.1 AA compliance.
- [ ] Prepare pricing/paywall implementation (freemium, professional, success-based).
- [ ] Build user onboarding flows and in-product guidance.
- [ ] Establish observability dashboards, alerting rules, incident response procedures.
- [ ] Create launch runbook, support SOPs, and documentation handover.
- [ ] Plan post-launch roadmap (enterprise features, additional integrations).

