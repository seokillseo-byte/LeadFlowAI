# LeadFlow AI

Windows-first AI lead radar for service businesses.

## Project source of truth

This repository is the shared source of truth for product, architecture, UI, AI behavior and implementation. Team members may use separate ChatGPT conversations, but final decisions and artifacts belong in GitHub.

**Start here:** [AGENTS.md](./AGENTS.md) → [Product Requirements](./docs/product/requirements.md) → [Architecture Blueprint](./docs/architecture/architecture.md) → [UI Design System](./docs/ui/design-system.md)

## Blueprints

### Architecture

[Open the LeadFlow AI Architecture Blueprint](./docs/blueprints/leadflow-ai-architecture.svg)

The architecture blueprint covers:
- Electron + React + TypeScript desktop
- FastAPI backend
- AI engine
- SQLite data layer
- Official Meta provider adapter
- Background services
- Human approval boundary
- Auditability, deduplication and rate limiting

### Software UI

[Open the LeadFlow AI Dashboard UI Blueprint](./docs/blueprints/leadflow-ai-dashboard.svg)

The UI blueprint defines the visual direction for:
- Dashboard
- Metrics
- Performance charts
- Conversion overview
- Lead Inbox
- Recent activity
- AI Assistant
- Campaign operations
- Navigation and status patterns

See [UI Design System](./docs/ui/design-system.md) for implementation rules.

## MVP
- Keyword include/exclude
- Lead Inbox with scoring
- Human approval queue
- AI reply suggestion boundary
- FastAPI backend
- Electron + React + TypeScript desktop shell
- Provider adapter for official Meta integrations

## Team development

### Product
- [Product Overview](./docs/product/product-overview.md)
- [Requirements](./docs/product/requirements.md)
- [Roadmap](./docs/product/roadmap.md)

### Architecture
- [Architecture](./docs/architecture/architecture.md)
- [ADR-001 Desktop Stack](./docs/architecture/decisions/ADR-001-desktop-stack.md)
- [ADR-002 AI Engine](./docs/architecture/decisions/ADR-002-ai-engine.md)
- [ADR-003 Meta Integration](./docs/architecture/decisions/ADR-003-meta-integration.md)

### UI
- [UI Overview](./docs/ui/ui-overview.md)
- [Design System](./docs/ui/design-system.md)
- [Dashboard](./docs/ui/dashboard.md)
- [Lead Inbox](./docs/ui/lead-inbox.md)
- [Settings](./docs/ui/settings.md)

### AI & Integrations
- [AI Scoring](./docs/ai/scoring.md)
- [Prompt Strategy](./docs/ai/prompt-strategy.md)
- [Reply Generation](./docs/ai/reply-generation.md)
- [Meta Integration](./docs/integrations/meta.md)

### Development
- [Setup](./docs/development/setup.md)
- [Testing](./docs/development/testing.md)
- [Troubleshooting](./docs/development/troubleshooting.md)
- [Contributing Guide](./CONTRIBUTING.md)
- [AI Development Instructions](./AGENTS.md)
- [All Blueprints](./docs/blueprints/README.md)

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

The Meta adapter is intentionally limited to official APIs/permissions. It does not implement
cookie/session scraping, CAPTCHA bypass, stealth automation, or bulk unsolicited outreach.
Outbound actions are designed around approval, deduplication, rate limits and auditability.
