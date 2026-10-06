ADR-0001: Monorepo structure
Date: 2026-10-06 Status: Accepted

Context
SupportIQ has three components: a Next.js frontend, a FastAPI API, and an MLservice. They share CI, tooling, and versioning.

Decision
Single repo with apps/ (deployable applications) and services/(infra-adjacent services). Python tooling managed by uv at the root.

Consequences
Positive: atomic changes across components, one CI pipeline.Negative: repo grows large; requires commit discipline.
