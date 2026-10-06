# Coding Contracts

## Python
- Pydantic models define API contracts.
- Services contain business rules.
- Repositories contain persistence concerns.
- Providers contain external-system translation only.
- Do not put FastAPI request concerns into domain services.

## TypeScript
- Pages compose features; they do not contain domain rules.
- API calls live in an API client layer.
- Shared types represent backend contracts.
- Reusable UI components live outside page modules.
- Never place provider secrets in renderer code.

## IDs and idempotency
Every external object preserves provider name + external ID + internal ID. Outbound actions require an idempotency key.

## State changes
Use explicit state transitions. Do not mutate status strings from arbitrary UI handlers.

## Error handling
Use stable machine-readable codes and user-readable messages. Distinguish validation, permission, provider unavailable, rate limited, temporary failure and safety-paused states.

## Mock-first development
When a dependency is not ready, use typed fixtures with the real API shape. Do not duplicate business logic in the frontend.

## Outbound safety
The only outbound path is:
review → explicit approval → server validation → action queue → provider capability check → execute → audit

## Breaking changes
Update the contract, identify dependent workstreams, add migration/compatibility handling, update tests and explain the change in the PR.
