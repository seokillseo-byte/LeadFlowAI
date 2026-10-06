# Testing

## Backend
Run Python compilation/tests before opening a PR.

## Frontend
Run typecheck and production build.

## Required validation for feature work
- Happy path
- Empty state
- Loading state
- Error state
- Permission/provider failure where relevant
- Approval boundary for outbound actions
- Deduplication/idempotency where relevant
- Pause/kill switch where relevant

## High-value backend tests
- keyword include/exclude matching
- normalization
- deduplication
- lead scoring boundaries
- AI response schema validation
- approval enforcement
- action idempotency
- rate limiting
- retry bounds
- provider capability checks

## UI tests
Prioritize:
- Lead Inbox filtering and review
- approval/rejection flows
- campaign pause/resume
- keyword test preview
- provider permission errors
- global pause state
- loading/empty/error states

## CI
GitHub Actions is the baseline validation gate. Do not bypass failing CI without documenting why.

## Current gap

The repository currently has only a test README and compile/typecheck/build validation. Real automated unit/integration/UI tests are still implementation work and should be added as the corresponding services are built.
