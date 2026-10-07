# LeadFlow AI — Current State

## Source of truth

GitHub repository: https://github.com/seokillseo-byte/LeadFlowAI

The repository and its project-state files are the durable project memory. Chat history is not a source of truth.

## Current baseline

- Main branch: `main`
- Main HEAD at state snapshot: `f1641b9a2e046ecbde5227558923fd91c0f36764`
- Milestone: Sprint 0 / Foundation
- Next phase: v0.2 Core Engine
- Coder 01 persistence foundation: merged and authoritative
- Coder 07 frontend foundation: PR #4, open and not authoritative until merged
- Current CI evidence: do not assume PASS unless GitHub reports a verified result

## Authoritative completed work

- Product, architecture, UI, AI and integration specifications
- ADR-001 desktop stack
- ADR-002 AI engine boundary
- ADR-003 Meta integration boundary
- ADR-004 migration stack
- SQLAlchemy + SQLite + aiosqlite
- Alembic initial migration
- Lead repository/service/router separation
- Lead API: list, detail, approve
- Backend integration/unit foundation
- CI foundation

## Current constraints

- Do not invent API fields/endpoints.
- Do not treat documentation as proof that an implementation exists.
- Official Meta APIs and permissions only.
- Human approval remains mandatory before outbound actions.
- Never merge main autonomously.
- Never commit secrets, cookies, tokens or passwords.
- No scraping, CAPTCHA bypass, stealth automation or unsolicited bulk outreach.

## Active work

See `ACTIVE_WORK.md`.

## Next work

See `NEXT_TASKS.md`.

## State update rule

Update this file when a milestone, authoritative branch state, blocker, or major architectural/contract status changes.
