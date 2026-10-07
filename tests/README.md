# Tests

Cross-layer and integration tests live here.

## Current Sprint 0 coverage

- tests/unit/ — foundation-level deterministic checks.
- tests/integration/test_lead_repository.py — SQLAlchemy repository behavior against SQLite.
- tests/integration/test_api_contract.py — health endpoint and preserved /api/scan behavior.

CI also runs Alembic from an empty SQLite database before executing the test suite.

Future workstreams add their own focused tests without moving business logic into the Coder 01 foundation.
