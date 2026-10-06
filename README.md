# LeadFlow AI

Windows-first AI lead radar for service businesses.

## Project source of truth

This repository is the shared source of truth for product, architecture, UI, AI behavior and implementation. Team members may use separate ChatGPT conversations, but final decisions and artifacts belong in GitHub.

**Start here:** [AGENTS.md](./AGENTS.md) → [Product Requirements](./docs/product/requirements.md) → [Feature Matrix](./docs/product/feature-matrix.md) → [Architecture](./docs/architecture/architecture.md) → [UI Design System](./docs/ui/design-system.md)

## Blueprints

### Architecture

[Open the detailed LeadFlow AI Architecture Blueprint](./docs/blueprints/leadflow-ai-architecture.svg)

The architecture blueprint covers:
- Windows desktop shell
- FastAPI domain orchestration
- Discovery → normalization → keyword matching → deduplication
- AI analysis and reply suggestion
- Lead review and explicit approval
- Action queue, rate limits and provider capability checks
- SQLite/repository layer
- Scheduler, notifications, retries, analytics and audit
- Official Meta provider boundary

Supporting architecture docs:
- [Detailed Architecture](./docs/architecture/detailed-architecture.md)
- [Data Flow & State Transitions](./docs/architecture/data-flow.md)
- [Security & Safety](./docs/architecture/security-safety.md)
- [Data Model](./docs/data/data-model.md)
- [API Contract](./docs/api/api-contract.md)

### Software UI

[Open the master LeadFlow AI Dashboard UI Blueprint](./docs/blueprints/leadflow-ai-dashboard.svg)

The UI blueprint defines the product shell and information hierarchy for:
- Dashboard and KPIs
- Performance and conversion
- Lead Inbox and approval queue
- Recent activity
- AI Assistant
- Running campaigns
- Facebook/API/database status
- Global pause and campaign management
- Full navigation structure

Screen specifications:
- Dashboard
- Campaigns
- Keywords
- Groups & Fanpages
- Lead Inbox
- Messages & Comments
- Response Templates
- AI Assistant
- Analytics
- Activity Log
- Settings
- Shared UI states/interactions

## Product
- [Product Overview](./docs/product/product-overview.md)
- [Requirements](./docs/product/requirements.md)
- [Feature Matrix](./docs/product/feature-matrix.md)
- [Roadmap](./docs/product/roadmap.md)

## Architecture
- [Architecture](./docs/architecture/architecture.md)
- [Detailed Architecture](./docs/architecture/detailed-architecture.md)
- [Data Flow](./docs/architecture/data-flow.md)
- [Security & Safety](./docs/architecture/security-safety.md)
- [ADR-001 Desktop Stack](./docs/architecture/decisions/ADR-001-desktop-stack.md)
- [ADR-002 AI Engine](./docs/architecture/decisions/ADR-002-ai-engine.md)
- [ADR-003 Meta Integration](./docs/architecture/decisions/ADR-003-meta-integration.md)

## UI
- [UI Overview](./docs/ui/ui-overview.md)
- [Design System](./docs/ui/design-system.md)
- [Dashboard](./docs/ui/dashboard.md)
- [Campaigns](./docs/ui/campaigns.md)
- [Keywords](./docs/ui/keywords.md)
- [Groups & Fanpages](./docs/ui/groups-pages.md)
- [Lead Inbox](./docs/ui/lead-inbox.md)
- [Messages & Comments](./docs/ui/messages-comments.md)
- [Response Templates](./docs/ui/templates.md)
- [AI Assistant](./docs/ui/ai-assistant.md)
- [Analytics](./docs/ui/analytics.md)
- [Activity Log](./docs/ui/activity-log.md)
- [Settings](./docs/ui/settings.md)
- [UI States & Interactions](./docs/ui/states-and-interactions.md)

## AI & Integrations
- [AI Scoring](./docs/ai/scoring.md)
- [Prompt Strategy](./docs/ai/prompt-strategy.md)
- [Reply Generation](./docs/ai/reply-generation.md)
- [Meta Integration](./docs/integrations/meta.md)

## Development
- [Setup](./docs/development/setup.md)
- [Implementation Map](./docs/development/implementation-map.md)
- [Team Workflow](./docs/development/team-workflow.md)
- [Testing](./docs/development/testing.md)
- [Troubleshooting](./docs/development/troubleshooting.md)
- [Contributing Guide](./CONTRIBUTING.md)
- [AI Development Instructions](./AGENTS.md)
- [All Blueprints](./docs/blueprints/README.md)

## Current implementation status

The repository currently contains the desktop/backend foundation and blueprint/specification layer. The production discovery engine, persistence layer, real AI orchestration, Meta provider implementation and Windows packaging are still roadmap work.

Do not mistake demo endpoints or placeholder providers for production capability.

## Run backend

cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

## Run desktop

npm install
npm run dev

## Build Windows

npm run build

### Safety architecture

The Meta adapter is intentionally limited to official APIs/permissions. It does not implement cookie/session scraping, CAPTCHA bypass, stealth automation, or bulk unsolicited outreach. Outbound actions are designed around explicit approval, deduplication, rate limits and auditability.
