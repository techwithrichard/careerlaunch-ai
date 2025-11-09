# Phase 04 · Track 01 — Data Pipeline Foundation

Build trustworthy analytics infrastructure powering downstream intelligence.

## A. Source System Integration
- [ ] Enumerate source tables and CDC strategies for each service.
- [ ] Configure connectors (Fivetran, Airbyte, custom) with retries and monitoring.
- [ ] Apply row-level filtering to isolate school-specific data early in ingest.
- [ ] Document schema change detection workflow and alerting.

## B. Data Transformation
- [ ] Implement dbt project structure with staging, intermediate, and mart layers.
- [ ] Create shared macros for common transformations (date handling, currency).
- [ ] Write unit tests and data expectations (dbt tests, Great Expectations).
- [ ] Version-control transformation logic with code review policy.

## C. Privacy & Compliance
- [ ] Apply pseudonymization/anonymization transformations where required.
- [ ] Maintain mapping tables for re-identification under strict access controls.
- [ ] Track data processing agreements and ensure opt-out flags propagate.
- [ ] Conduct privacy impact assessment for analytics workflows.

## D. Scheduling & Orchestration
- [ ] Use Airflow/Prefect/dbt Cloud to schedule incremental loads.
- [ ] Configure SLAs and alerting for late runs or data freshness breaches.
- [ ] Implement recovery procedures for failed tasks with idempotency.
- [ ] Provide run history dashboards and operational documentation.

