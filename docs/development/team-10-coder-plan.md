# LeadFlow AI — 10-Coder Delivery Plan

## Goal
Run 10 developers in parallel without merge conflicts or drift between UI, backend, database and integrations.

## Team map

| Coder | Workstream | Primary ownership | Main dependencies |
|---|---|---|---|
| 01 | Backend Foundation | DB, migrations, repositories, domain primitives | None |
| 02 | Campaign & Keyword Engine | campaigns, keyword rules, matching, scheduler contract | 01 |
| 03 | Discovery & Lead Pipeline | discovery, normalization, dedup, lead lifecycle | 01, 02 |
| 04 | AI Engine | analysis schema, scoring, intent, need, spam/fit, reply generation | 03 contracts |
| 05 | Meta Provider | OAuth/capabilities, discovery/action adapter, provider errors | 01, 03 |
| 06 | Safety & Action Runtime | approval boundary, action queue, rate limits, retries, audit, kill switch | 01, 05 |
| 07 | Frontend Shell & Dashboard | app shell, navigation, dashboard, shared components | API contracts |
| 08 | Frontend Operations | campaigns, keywords, groups/pages, settings | 02, 05 |
| 09 | Frontend Lead Workflow | Lead Inbox, review, messages/comments, templates, AI Assistant | 03, 04, 06 |
| 10 | QA / Integration / Release | automated tests, integration tests, E2E, CI, Windows validation | all tracks |

## Ownership boundaries

Backend:
- Coder 01: models, repositories, database, migrations
- Coder 02: campaign/keyword services and scheduler interfaces
- Coder 03: discovery, normalization, dedup, leads
- Coder 04: AI services, scoring, replies
- Coder 05: provider adapters and Meta
- Coder 06: actions, safety, audit, rate limiting

Frontend:
- Coder 07: shell, shared components, dashboard
- Coder 08: campaigns, keywords, groups/pages, settings
- Coder 09: leads, messages, templates, AI
- Coder 10: tests, CI, integration harness, release validation

## Delivery waves

### Wave 0 — Contract freeze
All 10 read AGENTS.md and the relevant product, architecture, API, data and UI specifications. Confirm shared naming, fixtures, branch rules and acceptance criteria.

### Wave 1 — Foundations
01 starts database/repositories. 07 starts frontend shell/design system. 10 starts test harness/CI. 05 finalizes provider interfaces only.

### Wave 2 — Domain engine
02 campaigns/keywords. 03 discovery/normalization/dedup. 04 AI contracts/provider abstraction. 06 action/safety runtime. 08/09 build UI against typed APIs and mocks.

### Wave 3 — Integration
05 connects the official Meta provider. 04 connects the AI provider. 06 connects approved actions to provider capabilities. 10 runs integration/E2E validation.

### Wave 4 — Hardening
Performance, errors, permissions, pause/kill switch, retries, audit, backup/restore and Windows packaging.

## Important rule

Do not split by UI feature alone. A Lead Inbox feature spans lead domain, approval/action, UI and tests. Use one feature Issue with linked subtasks across the owning workstreams.

## Shared contracts

These are the cross-team contracts:
- docs/data/data-model.md
- docs/api/api-contract.md
- docs/architecture/data-flow.md
- docs/product/feature-matrix.md
- docs/ui/*
- docs/blueprints/*

Breaking changes require the contract and dependent tests to be updated before merge.

## Definition of Done

Code + tests + API/data alignment + UI state coverage + safety/audit behavior + docs/blueprint alignment + passing CI + review.

One coder should act as technical integrator, but should not become the only person who can merge or understand the system.
