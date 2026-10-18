---
name: architecture
description: Compare minimal viable designs and document boundaries, tradeoffs, and default stack choices.
whenToUse: Before choosing a stack or before adding a new service.
---

1. Read the acceptance criteria and existing `docs/architecture.md`.
2. List the concrete capabilities the product needs now, not in five years.
3. Propose the smallest stack that satisfies those capabilities.
4. Compare at least two options with tradeoffs: complexity, hosting cost, operational burden, team familiarity.
5. State default choices:
   - Next.js + TypeScript for ordinary web apps.
   - PostgreSQL for relational persistence.
   - FastAPI only when a separate Python service is justified.
6. Document data flow, external services, and env vars needed (names only).
7. Save the decision to `docs/architecture.md` and `docs/decisions/` if non-trivial.
8. Do not add Kubernetes, microservices, queues, vector DBs, or large monitoring without a concrete requirement.
