# Testing

## Backend
Run Python compilation/tests before opening a PR.

## Frontend
Run typecheck and production build.

## Required validation for feature work
- Happy path
- Empty state
- Error state
- Permission/provider failure where relevant
- Approval boundary for outbound actions
- Deduplication/idempotency where relevant

## CI
GitHub Actions is the baseline validation gate. Do not bypass failing CI without documenting why.
