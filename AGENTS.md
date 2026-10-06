# LeadFlow AI — AI Development Instructions

## Project
LeadFlow AI is a Windows-first desktop application for discovering and managing potential customers from supported Facebook/Meta sources with AI-assisted analysis and human approval.

## Source of truth hierarchy
Before making changes, read the smallest relevant set, but use this precedence when artifacts disagree:

1. Product requirements and feature matrix
2. Architecture specifications / ADRs
3. Feature and UI specifications
4. Visual blueprints
5. Existing code

Visuals are a contract for appearance and information hierarchy, not the only source of functionality.

Start with:
- README.md
- docs/product/requirements.md
- docs/product/feature-matrix.md
- docs/architecture/architecture.md
- docs/architecture/detailed-architecture.md
- docs/ui/design-system.md
- docs/ai/scoring.md
- docs/integrations/meta.md

## Architecture rules
- Electron + React + TypeScript is the desktop shell.
- FastAPI + Python is the backend API.
- Keep external integrations behind provider adapters.
- Meta integration must use official Meta APIs and permissions.
- Do not implement cookie/session scraping, CAPTCHA bypass, stealth automation, or unsolicited bulk outreach.
- Outbound actions require a server-side approval boundary.
- Actions must be auditable, rate-limited, deduplicated and pausable.
- Prefer small, testable services over large modules.
- Do not put business logic directly into React components or provider adapters.
- External IDs and action idempotency keys must prevent duplicate processing.

## UI rules
- Follow docs/ui/design-system.md.
- Use docs/blueprints/leadflow-ai-dashboard.svg as the master visual reference.
- Use the screen-specific specs under docs/ui/ before implementing a screen.
- Preserve the information architecture and interaction states from the blueprint.
- Empty, loading, error, permission, paused and approval states are part of the product.
- Do not redesign the product without updating the UI blueprint/spec in the same change.

## Documentation rules
- If an architectural decision changes, add/update an ADR in docs/architecture/decisions/.
- If a user-facing workflow changes, update product or UI documentation.
- If an integration contract changes, update docs/integrations/.
- If data entities or API behavior changes, update docs/data/ or docs/api/.
- If implementation intentionally deviates from a blueprint, update the blueprint and spec before merging.

## Safety rules
- Never commit secrets, tokens, cookies, passwords or session data.
- Never allow an AI response to authorize outbound execution.
- Enforce approval and provider capability checks on the server, not only in the UI.
- Global pause/kill switch must stop new outbound execution.
- Rate limits and retries must have bounded behavior.

## Before finishing a task
- Run relevant tests.
- Run typecheck/build when applicable.
- Validate loading/empty/error/permission states for UI work.
- Validate approval/idempotency for outbound work.
- Update documentation and blueprints for behavior/architecture changes.
- Summarize files changed and validation performed in the PR.
