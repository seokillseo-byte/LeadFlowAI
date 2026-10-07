# Coder 07 — Sprint 0 Frontend Foundation

## Scope
Frontend architecture foundation, desktop shell, navigation, centralized API boundary, centralized Lead types, Lead Inbox foundation, explicit loading/empty/error/approval states, frontend validation foundation and implementation documentation.

Out of scope: AI, Meta integration, scraping, discovery, keyword matching, campaign backend logic, action execution, provider automation, credentials, autonomous outbound actions, stealth/CAPTCHA bypass, bulk outreach and backend/database changes.

## Architecture
The renderer follows:

`React UI → feature hooks → API client → FastAPI`

`App.tsx` is now composition only. Feature state lives in `src/features/leads/useLeads.ts`; API access lives in `src/api`; canonical Lead types live in `src/types`.

A lightweight view registry is used instead of introducing React Router. No state-management or UI framework was added.

## API boundary
`VITE_API_BASE_URL` is used when present. Development falls back to `http://127.0.0.1:8000`.

Only existing backend Lead endpoints are called:
- GET `/api/leads`
- GET `/api/leads/{id}`
- POST `/api/leads/{id}/approve`

No endpoint was invented.

## Lead contract
The backend response is:
- `id`
- `post_id`
- `campaign_id`
- `score`
- `intent`
- `fit`
- `need`
- `confidence`
- `status`

The UI intentionally does not fabricate `source`, `author`, `content` or `suggested_reply`.

## Approval behavior
Approval is not optimistic. The hook leaves the current Lead unchanged until the POST approval request returns a successful Lead response. A failed request exposes an error and leaves the original state available for retry.

The renderer does not authorize or execute outbound provider actions.

## Unavailable capabilities
Dashboard metrics without backend endpoints show `Unavailable`; Settings does not persist fake values; navigation areas without backend contracts render a professional `Not available yet` state.

The Lead Inbox supports list, open/view and approve because those endpoints exist. Reject, snooze and not-relevant are intentionally absent.

## Testing and validation
The repository's existing frontend setup has TypeScript and Vite build validation but no frontend unit-test framework. Coder 07 therefore does not add a large testing dependency. Required CI commands remain:
- `npm run typecheck`
- `npm run build:web`

The UI implementation explicitly covers loading, empty, API error, approval success and approval failure states in the Lead Inbox.

## Security constraints
- No secrets are stored in renderer code.
- Provider APIs are not called from React.
- Approval remains server-authoritative.
- No autonomous outbound action is implemented.
- Electron security settings remain untouched because no shell change required an Electron main-process modification.

## Files changed
- `src/App.tsx`
- `src/styles.css`
- `src/vite-env.d.ts`
- `src/api/client.ts`
- `src/api/leads.ts`
- `src/types/leads.ts`
- `src/features/leads/useLeads.ts`
- `src/layouts/AppLayout.tsx`
- `src/components/navigation/Sidebar.tsx`
- `src/components/common/StatePanel.tsx`
- `src/components/leads/LeadList.tsx`
- `src/components/leads/LeadDetail.tsx`
- `src/pages/DashboardPage.tsx`
- `src/pages/LeadInboxPage.tsx`
- `src/pages/SettingsPage.tsx`
- `src/pages/UnavailablePage.tsx`
- `docs/development/implementation-map.md`
- `docs/development/coder-07-sprint-0.md`

## Intentionally untouched
- `backend/**`
- `alembic/**`
- database schema
- AI logic
- Meta/provider adapters
- discovery and keyword engines
- action execution
- Electron main process
- CI workflow

## Contract conflict
No conflict requiring a backend change was discovered. One requested UI field set is not present in the backend Lead response; this gap is documented rather than silently filled.
