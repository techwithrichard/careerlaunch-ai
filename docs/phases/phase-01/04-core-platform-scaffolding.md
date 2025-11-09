# Phase 01 · Track 04 — Core Platform Scaffolding

Stand up service foundations aligned with the target architecture.

## A. Service Skeletons
- [ ] Generate NestJS service templates for each backend component.
- [ ] Implement health check endpoints (`/health`, `/readiness`) with status.
- [ ] Add shared configuration module consuming validated environment vars.
- [ ] Set up basic authentication middleware (JWT verification stub).

## B. Data Layer Baseline
- [ ] Define ORM configuration (Prisma/TypeORM) with connection pooling.
- [ ] Create initial migrations for user, school, cohort tables with `school_id`.
- [ ] Seed reference data (roles, feature toggles) for local usage.
- [ ] Document migration run order and rollback process.

## C. Communication Contracts
- [ ] Establish API gateway routing table with rate limiting defaults.
- [ ] Create shared DTO/Schema library for request/response validation.
- [ ] Draft interface definitions for service-to-service calls.
- [ ] Prototype async messaging (Kafka/SQS/EventBridge) if required later.

## D. Observability Foundations
- [ ] Instrument logging with structured output (pino/winston).
- [ ] Add distributed tracing hooks (OpenTelemetry) ready for exporters.
- [ ] Capture basic metrics (request duration, error rates) via Prometheus.
- [ ] Produce service diagrams in `docs/architecture/system-architecture-diagrams`.

