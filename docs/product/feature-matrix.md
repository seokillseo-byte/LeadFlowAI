# LeadFlow AI Feature Matrix

This matrix is the implementation contract for the MVP and the path to v1.0.

| Area | MVP | Required behavior | UI reference | Backend reference |
|---|---|---|---|---|
| Dashboard | Yes | KPIs, performance, conversion, activity, AI assistant, running campaigns, system status | dashboard blueprint | analytics/dashboard services |
| Campaigns | Yes | Create, edit, pause, resume, schedule, keyword-set binding | campaigns.md | campaign service |
| Keywords | Yes | Include/exclude terms, groups, matching mode, test preview | keywords.md | keyword engine |
| Groups & Pages | Yes | Connect supported Meta assets, permission/capability status | groups-pages.md | Meta provider |
| Discovery | Yes | Fetch supported content, normalize, deduplicate | architecture/data-flow | discovery service |
| Lead Inbox | Yes | Prioritize, inspect, review, approve/reject/snooze | lead-inbox.md | lead service |
| AI analysis | Yes | Intent, score, fit, need, spam, confidence | ai docs | AI engine |
| Reply suggestions | Yes | Generate editable contextual suggestion; never auto-send | templates + AI assistant | reply service |
| Comments/messages | Yes | Approval queue, permitted provider action, result tracking | messages-comments.md | action queue |
| Templates | Yes | Versioned response templates and variables | templates.md | template service |
| Analytics | Yes | Funnel, conversion, campaign performance, export-ready data | analytics.md | analytics service |
| Activity log | Yes | Immutable-ish audit trail for important events/actions | activity-log.md | audit service |
| Notifications | Yes | In-app notifications for leads, errors, permission changes | dashboard/settings | notification service |
| Safety controls | Yes | Pause/kill switch, rate limits, approval boundary | settings/states | safety service |
| Data/storage | Yes | SQLite MVP, migrations, backup/restore plan | settings | repository/data layer |
| Multi-account | Later | Multiple supported accounts/workspaces | settings | provider/account model |
| Auto-update | v1.0 | Signed Windows update flow | settings | desktop release pipeline |

## Definition of complete

A feature is not considered complete when only its happy-path UI exists. It must have:
1. UI state coverage.
2. Backend/API contract.
3. Persistence model where needed.
4. Error and permission handling.
5. Audit behavior for meaningful actions.
6. Tests appropriate to the risk.
7. Documentation and blueprint alignment.
