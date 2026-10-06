# LeadFlow AI Roadmap

## Phase 0 — Blueprint readiness
- Product requirements and feature matrix
- Detailed architecture/data flow
- Data model and API contract
- Complete UI information architecture
- Master dashboard and architecture SVG blueprints
- Team/AI workflow rules

## v0.1 — Foundation
- Desktop shell
- FastAPI backend
- Initial Lead Inbox
- Architecture and UI blueprint/spec layer

## v0.2 — Core engine
- SQLite persistence + migrations
- Campaigns
- Keyword management
- Source targets
- Post/lead normalization
- Deduplication/idempotency
- Scheduler
- Audit log
- Notifications
- Safety/kill switch

## v0.3 — AI
- Intent classification
- 0–100 lead scoring
- Fit/spam detection
- Need extraction
- Reply generation
- Confidence
- Prompt/model version tracking
- AI evaluation tests

## v0.4 — Meta integration
- OAuth/account connection
- Capability and permission checks
- Official API provider implementation
- Discovery normalization
- Action queue
- Rate limits and bounded retries
- Provider error mapping

## v0.5 — Windows product
- Background scanning
- Tray behavior
- Notifications
- First-run wizard
- Secure local secret storage
- Installer
- Crash/error diagnostics

## v1.0 — Commercial
- Multi-campaign workspace
- Response templates
- Analytics
- Conversion tracking
- CSV/Excel export
- Backup/restore
- Signed auto-update
- Release/rollback process
