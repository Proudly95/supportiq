ADR-0002: Synchronous SQLAlchemy (sync-first)
Date: 2026-10-06 Status: Accepted

Context
FastAPI supports async endpoints and async SQLAlchemy. Our workload is regularCRUD plus calls to ML services — not tens of thousands of concurrentconnections. The codebase must stay easy to read and debug.

Decision
Use synchronous SQLAlchemy 2.0 with the psycopg (v3) driver and plain defendpoints. FastAPI automatically runs sync endpoints in a threadpool, so theydon't block the server.

Consequences
Positive: simpler code, readable stack traces, smaller dependency surface.Negative: lower theoretical concurrency ceiling; migrating to async laterwould touch the data layer and every endpoint.

This is a decision interviewers actually ask about — and you'll have a documented answer.

(Also note: we're putting all Python deps in the root pyproject.toml for now. When the ML service arrives in Phase 3 with heavyweight deps like PyTorch, we'll split into uv workspaces. Deliberate YAGNI.)
