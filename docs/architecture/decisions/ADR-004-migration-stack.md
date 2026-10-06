# ADR-004 — Database Migration Stack

- Status: Accepted
- Date: 2026-10-06
- Scope: Coder 01 / Sprint 0

## Decision

LeadFlow AI uses **Alembic + SQLAlchemy 2.x + SQLite + aiosqlite** for the Windows-first MVP persistence and migration stack.

## Rationale

- SQLAlchemy is already the approved persistence abstraction in the backend dependencies.
- aiosqlite provides the async SQLite driver required by the FastAPI backend.
- Alembic provides versioned, reviewable schema changes and rollback/forward-compatibility notes.
- SQLite remains the canonical MVP store defined by the data-model and architecture specifications.
- Repository interfaces remain above SQLAlchemy so application services do not depend directly on persistence implementation details.

## Dependency direction

router → service → repository interface → repository implementation → SQLAlchemy/session → SQLite

Services must not contain raw SQL or direct SQLAlchemy query construction.

## Migration rules

1. Every schema change receives an Alembic revision.
2. Revisions must define both upgrade and downgrade behavior where SQLite permits safe reversal.
3. Canonical state semantics are not invented by migrations. State columns remain compatible with the approved specifications until their owning workstream defines lifecycle semantics.
4. Seed/demo data is separate from production migrations.
5. Migration failures must fail CI; CI must not be weakened to accommodate migration errors.

## Consequences

Coder 01 owns the persistence foundation and minimal repository contracts. Business rules and state machines remain with their owning workstreams (Coders 02–06).

## Migration compatibility note

The initial revision creates the tables and minimum indexes specified by docs/data/data-model.md. Future revisions must document any compatibility impact in the revision message and associated documentation.
