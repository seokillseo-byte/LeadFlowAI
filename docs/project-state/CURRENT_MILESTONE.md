# LeadFlow AI — Current Milestone

## Sprint 0 — Foundation

### Objective

Establish a compatible backend persistence foundation, frontend foundation, validation path, and stable contracts before Wave 1 core-engine implementation.

### Exit criteria

- Persistence foundation merged and verified.
- Frontend foundation reviewed and merged only after validation.
- Sprint 0 mocked E2E path is covered:
  post fixture → normalize → score → lead → review → approve → simulated action → audit.
- Typecheck/build/test validation is reproducible.
- Current project state and task queue are synchronized with GitHub.

### Transition

After Sprint 0 exit, execute Wave 1 in the order defined by `NEXT_TASKS.md`. Do not start lower-priority work while a higher-priority task is blocked only by avoidable implementation work.

### Human gates

- PR merge approval.
- Architecture/contract changes.
- Real external provider authorization.
- Real outbound Meta execution.
