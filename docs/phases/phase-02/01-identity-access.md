# Phase 02 · Track 01 — Identity & Access

Deliver secure, school-aware authentication and authorization services.

## A. Authentication Flows
- [ ] Implement email/password signup with email verification workflow.
- [ ] Add multi-factor support (TOTP + backup codes) with enrollment UX.
- [ ] Expose passwordless login option (magic link or WebAuthn) for staff.
- [ ] Enforce rate-limiting and captcha for auth-sensitive endpoints.

## B. Authorization Model
- [ ] Design role hierarchy (learner, mentor, coach, admin, super-admin).
- [ ] Implement attribute-based policies to enforce `school_id` boundaries.
- [ ] Provide permission editor UI for admins to assign roles.
- [ ] Add policy evaluation caching layer with invalidation strategy.

## C. External Identity Providers
- [ ] Register OAuth apps (Google Workspace, Microsoft Entra) scoped per school.
- [ ] Support SSO handshake with JIT provisioning of learner accounts.
- [ ] Map IdP groups to internal roles and permissions.
- [ ] Document onboarding checklist for school IT integration.

## D. Session Lifecycle
- [ ] Issue short-lived access tokens and long-lived refresh tokens with rotation.
- [ ] Store session metadata (device, location) for user transparency.
- [ ] Provide forced logout endpoints for admins and user self-service.
- [ ] Monitor anomalous login activity with alerting hooks.

## E. Compliance & Auditing
- [ ] Log auth events with correlation IDs for incident response.
- [ ] Support GDPR/FERPA deletion requests through automation.
- [ ] Conduct security review (threat model, penetration test) before launch.
- [ ] Maintain runbook for identity incident handling.

