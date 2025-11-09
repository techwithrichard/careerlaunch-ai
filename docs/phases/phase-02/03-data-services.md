# Phase 02 · Track 03 — Data Services

Stand up resilient data stores and pipelines powering the platform.

## A. Relational Data
- [ ] Finalize PostgreSQL schema for auth, profiles, jobs, applications, analytics seeds.
- [ ] Configure schema migration tooling with versioning and rollback tests.
- [ ] Establish read replicas for reporting workloads.
- [ ] Implement row-level security enforcing `school_id` constraints.

## B. Caching & Messaging
- [ ] Provision Redis cluster with TLS and authentication.
- [ ] Define cache keys for session tokens, feature flags, and analytics aggregates.
- [ ] Implement cache invalidation strategies (time-based, event-based).
- [ ] Evaluate message broker (Kafka/SNS/SQS) for async processing requirements.

## C. Search Infrastructure
- [ ] Create Elasticsearch indices for job postings and candidate profiles.
- [ ] Design ingestion pipeline from job boards with deduplication logic.
- [ ] Map search analyzers for location, skills, and salary ranges.
- [ ] Add monitoring for indexing lag and query performance.

## D. Object Storage
- [ ] Configure S3/Blob storage buckets with lifecycle rules (archive, delete).
- [ ] Implement signed URL generation for secure downloads.
- [ ] Validate antivirus scanning and content-type enforcement.
- [ ] Track storage costs and optimize with compression/deduplication.

## E. Data Governance
- [ ] Define retention policies per data category (applications, resumes, logs).
- [ ] Implement data masking for PII when exposing to analytics environments.
- [ ] Automate backup/restore drills with documented RTO/RPO.
- [ ] Maintain data catalog documenting tables, fields, owners, and lineage.

