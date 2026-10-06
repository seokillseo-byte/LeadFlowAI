# Sprint 0 — Before Production Coding

Sprint 0 is the short contract-and-tooling phase that prevents 10 developers from writing incompatible implementations.

## Must complete

### Repository
- [ ] Split frontend out of src/App.tsx into pages/components/features.
- [ ] Split backend main.py into routers/services as implementation starts.
- [ ] Establish migrations and tests/unit, tests/integration, tests/e2e.

### Database
- [ ] Select and document migration tool.
- [ ] Create initial SQLite schema from docs/data/data-model.md.
- [ ] Create repository interfaces.
- [ ] Separate seed/demo fixtures from production data.

### API
- [ ] Modular API routers.
- [ ] Pydantic request/response schemas.
- [ ] Stable machine-readable error codes.
- [ ] Contract tests for critical endpoints.
- [ ] Keep API versioning under /api.

### Frontend
- [ ] Routing/page structure.
- [ ] Shared UI primitives.
- [ ] Typed API client and models.
- [ ] Loading/empty/error/permission/paused states.
- [ ] No production business logic hidden in page components.

### AI
- [ ] Strict structured output schema.
- [ ] Model/prompt version fields.
- [ ] Deterministic local fixtures.
- [ ] Validation for malformed/low-confidence results.
- [ ] AI remains advisory and cannot authorize actions.

### Provider
- [ ] Provider interface and capability model.
- [ ] Normalized external objects.
- [ ] Provider error taxonomy.
- [ ] Verify current official Meta API permissions/capabilities before implementation.

### Safety
- [ ] Server-side approval enforcement.
- [ ] Idempotency keys.
- [ ] Rate limiter.
- [ ] Bounded retries.
- [ ] Global pause/kill switch.
- [ ] Audit events.

### Testing/CI
- [ ] Backend unit test command.
- [ ] Frontend typecheck/build.
- [ ] API integration tests.
- [ ] One E2E happy path.
- [ ] CI blocks failures.

## Sprint 0 exit

The team can run one mocked end-to-end path:

post fixture → normalize → score → lead → review → approve → simulated action → audit

Meta may remain simulated during this exit check.
