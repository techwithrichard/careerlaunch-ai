# Phase 01 · Track 05 — Frontend & Mobile Shells

Provide cohesive client scaffolding ready for feature development.

## A. Web Application
- [ ] Initialize React app with Vite or Next.js (SSR decision recorded).
- [ ] Install design system primitives (component library, theming, typography).
- [ ] Configure routing (React Router/Next routing) with auth guards.
- [ ] Set up state management (Redux Toolkit, Zustand, Recoil) with persisted store.
- [ ] Add API client layer using `react-query`/`tanstack-query` or equivalent.

## B. Browser Extension
- [ ] Scaffold manifest v3 structure with background, content, and popup scripts.
- [ ] Implement secure messaging bridge to backend (via API gateway).
- [ ] Share UI components with web app via shared package.
- [ ] Establish hosting strategy (Chrome Web Store, Firefox Add-ons) documentation.

## C. Mobile Shells
- [ ] Decide on React Native vs Flutter; document trade-offs.
- [ ] Sync design tokens with web via shared package or REST endpoint.
- [ ] Implement authentication flows with secure storage (Keychain/Keystore).
- [ ] Integrate push notification service (Firebase/APNs).

## D. Developer Experience
- [ ] Configure Storybook (or equivalent) for UI component development.
- [ ] Add visual regression testing harness (Chromatic, Loki).
- [ ] Enable hot reload / fast refresh across web, extension, mobile projects.
- [ ] Document development workflows in `docs/frontend/`.

