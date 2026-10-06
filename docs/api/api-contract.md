# API Contract Blueprint

The API is versioned under `/api`.

## Health

GET `/health`

Returns service status and version.

## Dashboard

GET `/api/dashboard/summary`
GET `/api/dashboard/performance?range=7d`
GET `/api/dashboard/activity`

## Campaigns

GET/POST `/api/campaigns`
GET/PATCH/DELETE `/api/campaigns/{id}`
POST `/api/campaigns/{id}/pause`
POST `/api/campaigns/{id}/resume`

## Keywords

GET/POST `/api/campaigns/{id}/keywords`
PATCH/DELETE `/api/keywords/{id}`
POST `/api/keywords/test`

## Leads

GET `/api/leads`
GET `/api/leads/{id}`
POST `/api/leads/{id}/approve`
POST `/api/leads/{id}/reject`
POST `/api/leads/{id}/snooze`
POST `/api/leads/{id}/not-relevant`

## Suggestions

POST `/api/leads/{id}/suggestion`
PATCH `/api/suggestions/{id}`

## Actions

GET `/api/actions`
POST `/api/actions/{id}/cancel`

## Provider

GET `/api/providers/meta/status`
POST `/api/providers/meta/connect`
POST `/api/providers/meta/disconnect`
GET `/api/providers/meta/capabilities`

## Safety

GET `/api/safety/status`
POST `/api/safety/pause`
POST `/api/safety/resume`

## Response rules

Use stable machine-readable error codes. Never return secrets. Outbound endpoints must enforce approval and provider capability checks server-side; UI checks are not sufficient.
