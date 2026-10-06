# Pre-Code Readiness Audit

This document records what is defined before major production implementation begins.

## Defined

### Product
- Product goal and scope
- Core workflow
- MVP capabilities
- Non-goals/safety boundaries
- Feature matrix
- Roadmap

### Architecture
- Desktop/backend/provider boundaries
- Detailed service map
- Discovery and lead lifecycle
- Approval boundary
- Data model
- API contract
- Security/safety controls
- ADRs

### UI
- Information architecture
- Design system
- Master dashboard visual blueprint
- Lead Inbox contract
- Campaigns
- Keywords
- Groups & Fanpages
- Messages & Comments
- Templates
- AI Assistant
- Analytics
- Activity Log
- Settings
- Shared UI states

### Team/AI
- AGENTS.md
- Contributing rules
- Team workflow
- Issue/PR templates
- CI baseline

## Remaining implementation gaps

These are intentionally not hidden by the blueprint:

1. SQLite schema + migrations.
2. Repository/data-access layer.
3. Real campaign/keyword services.
4. Discovery/scanning scheduler.
5. Normalization and deduplication.
6. Production AI provider client and structured output validation.
7. Lead/approval/action state machine.
8. Rate limiter and bounded retry policy.
9. Real Meta OAuth/provider implementation using currently supported official APIs.
10. Notifications/tray/background worker behavior.
11. Analytics aggregation.
12. Secure local secret storage.
13. Windows installer/package pipeline.
14. Automated unit/integration/UI tests.
15. Production error reporting and diagnostics.

## Readiness rule

Do not start a large feature by editing only `src/App.tsx`. First create the domain/API/persistence boundary required by the feature, then implement the UI against that contract.

## Blueprint rule

The two master SVGs are now detailed implementation references. They should remain synchronized with the text specifications. If a requirement is missing from a visual, the text specification still wins; update the visual before the next feature cycle.

## Phase-0 acceptance

Phase 0 is considered complete when:
- all required docs are linked from README;
- architecture and dashboard SVGs render in GitHub;
- feature/UI/data/API contracts exist;
- safety and approval rules are explicit;
- team workflow is documented;
- CI baseline passes.

Phase 0 does not mean the production engine is complete.
