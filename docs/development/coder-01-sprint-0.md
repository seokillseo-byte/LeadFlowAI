# Coder 01 — Sprint 0 Foundation

## Scope completed

This workstream establishes the persistence foundation only:

- Alembic + SQLAlchemy + SQLite/aiosqlite
- canonical initial schema from docs/data/data-model.md
- async SQLAlchemy session factory
- repository interface + implementation for the existing Lead API path
- FastAPI router/service separation for existing lead endpoints
- preserved /api/scan endpoint
- backend migration/repository/API tests
- CI migration and test execution
- frontend typecheck dependency correction for the pre-existing CI failure

## Dependency direction

router → service → repository interface → repository implementation → SQLAlchemy/session → SQLite

No service contains raw SQL or direct SQLAlchemy persistence code.

## Canonical state semantics

Coder 01 does not introduce new lifecycle states. The existing Lead approval behavior uses the already-present approved value from the pre-foundation implementation. Other state semantics remain unspecified where the canonical documents do not define them and are left to owning workstreams.

## Minimal repository policy

Only Lead persistence is exposed as a repository in Sprint 0 because it proves the architecture against an existing API path. Additional repositories are added by their owning workstreams when their contracts are implemented.

## CI failure diagnosis

The pre-implementation CI run had a successful backend job and a failed frontend job. The frontend failed during npm run typecheck because React and JSX type declarations were absent (TS7016, TS7026, plus dependent implicit-any diagnostics). The fix adds @types/react and @types/react-dom; CI is not disabled or weakened.

## API compatibility note

The previous implementation stored demo Lead objects directly in memory and exposed fields such as source/author/content. The canonical data model now persists a Lead through Post/Campaign relationships. The Sprint 0 API separation therefore establishes the canonical persistence-backed Lead shape rather than retaining the obsolete in-memory demo representation. /api/scan is intentionally preserved unchanged because it exists in the current implementation but is not yet part of the canonical API blueprint.

## Out of scope

AI, Meta integration, discovery, keyword matching, action execution, frontend feature work and business state machines remain outside Coder 01 ownership.
