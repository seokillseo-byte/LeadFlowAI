# Detailed Architecture

This is the implementation-level companion to the high-level architecture blueprint.

## Runtime topology

```
Electron Shell
  └─ React Renderer
       ├─ Dashboard
       ├─ Campaigns
       ├─ Keywords
       ├─ Lead Inbox
       ├─ Messages & Comments
       ├─ AI Assistant
       ├─ Analytics
       ├─ Activity Log
       └─ Settings
              │ HTTP/IPC boundary
              ▼
FastAPI Application
  ├─ API routers
  ├─ Authentication/session context
  ├─ Campaign service
  ├─ Discovery service
  ├─ Keyword matching
  ├─ Normalizer
  ├─ Deduplication
  ├─ Lead service
  ├─ AI engine
  ├─ Reply service
  ├─ Review/approval service
  ├─ Action queue
  ├─ Rate limiter
  ├─ Scheduler
  ├─ Notification service
  ├─ Analytics
  └─ Audit service
       │
       ├── SQLite / repository layer
       ├── AI provider adapter
       └── Meta provider adapter
```

## Discovery pipeline

1. Scheduler selects active campaigns.
2. Meta provider checks account capabilities and fetches supported content.
3. Discovery normalizes external posts into an internal Post model.
4. Keyword engine applies include/exclude rules.
5. Deduplication prevents repeated processing.
6. AI analyzes intent, fit, need, spam signals, confidence and score.
7. Lead service persists a prioritized lead.
8. Reply service creates a suggestion.
9. Review queue exposes the lead to a human.
10. Only an explicit approval creates an executable outbound action.
11. Action queue enforces provider capability, rate limits and retry rules.
12. Provider result is persisted and audited.
13. Analytics consumes normalized events.

## Boundaries

### Renderer
Never holds provider secrets. It requests backend capabilities through a narrow API.

### Backend
Owns business rules, persistence, AI orchestration, provider calls, approval checks and audit events.

### Providers
External systems are hidden behind adapters. No provider-specific logic should leak into UI components.

### AI
AI is advisory. A model response cannot authorize an outbound action.

## Failure handling

Every asynchronous operation should have:
- status
- started_at
- completed_at
- error code/message
- retry count where applicable
- correlation/request ID
- audit event when user-visible or externally consequential

## Implementation rule

Prefer small domain services over a single large FastAPI module. Keep provider adapters replaceable and testable with fakes.
