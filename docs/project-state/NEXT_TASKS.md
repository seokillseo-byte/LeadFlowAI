# LeadFlow AI — Next Tasks

This file is the execution queue for autonomous continuation.

## Selection rules

1. Select the highest-priority **unblocked** task whose dependencies are complete.
2. Do not skip a higher-priority task without recording a blocker.
3. Do not invent unrelated product work.
4. Do not start a task already owned by an open PR.
5. A task is complete only when its Definition of Done is satisfied.
6. After completing a task, update project-state and re-evaluate this queue.
7. If the next task requires a human gate, stop at that gate and report it.
8. Human gates include merge, architecture/contract changes, external authorization, and real outbound execution.
9. Emergency bug fixes required to make the current task/PR correct may be handled before queue advancement, but must remain within scope.

## P0 — Sprint 0 completion

### TASK-001 — Coder 01 persistence foundation
- Status: DONE
- Owner: Backend Foundation
- Dependency: none

### TASK-002 — Coder 07 frontend foundation
- Status: IN_PROGRESS
- Owner: Frontend Foundation
- PR: #4
- Dependency: TASK-001
- Next action: resolve review findings and validate typecheck/build/CI.
- Human gate: merge PR #4 after clean validation.

### TASK-003 — Sprint 0 QA / mocked E2E verification
- Status: TODO
- Owner: QA / Integration
- Dependency: TASK-002 merged
- Scope:
  - verify backend migration
  - verify API contract
  - verify frontend typecheck/build
  - verify mocked flow: post fixture → normalize → score → lead → review → approve → simulated action → audit
  - document remaining Sprint 0 blockers

## P1 — v0.2 Core Engine

### TASK-004 — Campaign & Keyword Engine
- Status: TODO
- Owner: Campaign / Keywords
- Dependency: TASK-003
- Scope: campaign CRUD/domain, keyword rules, matching interfaces, scheduler boundary, tests.

### TASK-005 — Discovery / Normalization / Deduplication
- Status: TODO
- Owner: Discovery / Lead Pipeline
- Dependency: TASK-004
- Scope: discovery interfaces, normalization, deduplication/idempotency, lead lifecycle progression, tests.

### TASK-006 — Structured AI Analysis
- Status: TODO
- Owner: AI
- Dependency: TASK-005
- Scope: structured intent/fit/need/confidence/score, schema validation, prompt/model versioning, reply suggestion boundary, tests.

### TASK-007 — Safety / Action Runtime
- Status: TODO
- Owner: Safety
- Dependency: TASK-006
- Scope: approval enforcement, action queue, capability checks, bounded retries, rate limits, kill switch, audit events.

## P2 — Meta integration and product hardening

### TASK-008 — Meta provider integration
- Status: TODO
- Owner: Meta
- Dependency: TASK-007
- Scope: official OAuth/permissions, capability checks, fetch/normalize translation, provider errors, no scraping.

### TASK-009 — Operations UI completion
- Status: TODO
- Owner: Operations UI
- Dependency: relevant backend contracts
- Scope: campaigns, keywords, groups/pages, settings and states.

### TASK-010 — Lead workflow UI completion
- Status: TODO
- Owner: Lead Workflow UI
- Dependency: TASK-005 and TASK-006
- Scope: lead detail, messages/comments, templates, AI assistant, approval states.

### TASK-011 — QA / release hardening
- Status: TODO
- Owner: QA / Release
- Dependency: P1 and P2 implementation
- Scope: integration/E2E, Windows validation, diagnostics, secure local secret storage, installer readiness.

## Queue discipline

When an agent finishes a task:
- mark it DONE only with evidence;
- update `CURRENT_STATE.md`, `ACTIVE_WORK.md`, and this file;
- create/update the PR;
- then select the next highest-priority unblocked task belonging to its assigned role;
- stop if the next task crosses a human gate or lacks a sufficiently defined scope.
