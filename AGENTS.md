# LeadFlow AI — AI Development Instructions

## Project
LeadFlow AI is a Windows-first desktop application for discovering and managing potential customers from supported Facebook/Meta sources with AI-assisted analysis and human approval.

## Source of truth
Before making changes, read:
- README.md
- docs/architecture/architecture.md
- docs/product/requirements.md
- docs/ui/design-system.md
- docs/ai/scoring.md
- docs/integrations/meta.md

## Architecture rules
- Electron + React + TypeScript is the desktop shell.
- FastAPI + Python is the backend API.
- Keep external integrations behind provider adapters.
- Meta integration must use official Meta APIs and permissions.
- Do not implement cookie/session scraping, CAPTCHA bypass, stealth automation, or unsolicited bulk outreach.
- Outbound actions require an approval boundary.
- Actions must be auditable, rate-limited, deduplicated, and reversible/pausable where practical.
- Prefer small, testable services over large modules.

## UI rules
- Follow docs/ui/design-system.md.
- Keep the desktop UI consistent with the approved dashboard blueprint.
- Reuse existing components and patterns before introducing new ones.
- Do not redesign the product without updating the UI blueprint/spec.

## Documentation rules
- If an architectural decision changes, add/update an ADR in docs/architecture/decisions/.
- If a user-facing workflow changes, update product or UI documentation.
- If an integration contract changes, update docs/integrations/.

## Before finishing a task
- Run relevant tests.
- Run typecheck/build when applicable.
- Update documentation for behavior or architecture changes.
- Summarize files changed and validation performed in the PR.
