# LeadFlow AI Architecture Blueprint

This document is the canonical technical architecture reference for the project.

![LeadFlow AI Architecture](../blueprints/leadflow-ai-architecture.svg)

## System layers

### 1. Windows Desktop
- Electron
- React
- TypeScript
- Dashboard
- Lead Inbox
- Campaign Management
- Settings
- Notifications

### 2. Backend API
- FastAPI
- Campaign Service
- Keyword Engine
- Lead Service
- Action Queue
- Integration Provider Adapter

### 3. AI Engine
- Intent classification
- Lead score 0–100
- Spam / not-fit detection
- Need extraction
- Suggested reply generation
- Confidence

### 4. Data
- SQLite for the Windows-first MVP
- Users/settings
- Campaigns/keywords
- Posts/leads
- Actions/audit logs
- Templates
- Analytics

### 5. External integration
Meta integration is isolated behind a provider adapter and must use supported official Meta APIs, permissions, rate limits and account capabilities.

### 6. Background services
- Scheduler
- Deduplication
- Notifications
- Audit log
- Retry/error handling

## Approval boundary

The default workflow is:

1. Discover supported content
2. Normalize and deduplicate
3. Analyze with AI
4. Score lead
5. Generate suggested response
6. Human reviews
7. Human approves
8. Provider executes permitted action
9. Audit result

AI recommends; the user remains in control of outbound actions.

## Blueprint status

Status: Approved working blueprint for the current product direction.

Any structural change should be documented as an ADR.
