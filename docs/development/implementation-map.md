# Implementation Map

This document maps the approved blueprint to the current codebase.

## Frontend

### Application composition
- `src/App.tsx`
  - Thin route/view composition only.
- `src/main.tsx`
  - React entry point and global stylesheet import.
- `src/layouts/AppLayout.tsx`
  - Reusable Windows desktop shell and lightweight route registry.
- `src/styles.css`
  - Global design tokens, shell, states and Lead Inbox presentation.

### API boundary
- `src/api/client.ts`
  - Central Axios client using `VITE_API_BASE_URL`, with development fallback to `http://127.0.0.1:8000`.
- `src/api/leads.ts`
  - Typed wrappers for the existing Lead list/view/approve endpoints.
- `src/types/leads.ts`
  - Canonical frontend Lead and API error types.
- `src/vite-env.d.ts`
  - Vite environment typing.

### Feature and presentation
- `src/features/leads/useLeads.ts`
  - Lead loading, detail loading and approval state. Approval updates local UI state only after a successful API response.
- `src/components/navigation/Sidebar.tsx`
  - Canonical product navigation.
- `src/components/common/StatePanel.tsx`
  - Loading/empty/error/unavailable presentation primitive.
- `src/components/leads/LeadList.tsx`
  - Available Lead fields and approval action.
- `src/components/leads/LeadDetail.tsx`
  - Detail view using only the canonical Lead response.
- `src/pages/DashboardPage.tsx`
  - Dashboard foundation; unavailable metrics are explicitly marked unavailable.
- `src/pages/LeadInboxPage.tsx`
  - Real API Lead Inbox with loading, empty, error, detail and approval states.
- `src/pages/SettingsPage.tsx`
  - Settings foundation with no fake persistence.
- `src/pages/UnavailablePage.tsx`
  - Professional placeholders for navigation areas whose backend contracts are not implemented.

## Backend

Backend ownership is unchanged by Coder 07. Existing Lead API contract remains the source of truth:
- `backend/app/routers/leads.py`
- `backend/app/repositories/lead.py`
- `backend/app/services/leads.py`
- `backend/app/db/models.py`

## Dependency direction

`React UI → feature hook → API client → FastAPI`

No new state-management, routing, UI component or data-fetching framework is introduced.

## Contract note

Sprint 0 Lead responses expose:
`id`, `post_id`, `campaign_id`, `score`, `intent`, `fit`, `need`, `confidence`, `status`.

The response does not expose post content, source, author or suggested reply. The frontend therefore does not fabricate those values. A future backend contract can add them without changing the current API boundary.
