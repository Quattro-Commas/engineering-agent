---
name: database-migrations
description: Change database schemas safely with constraints, migration tests, and rollback review.
whenToUse: When adding, altering, or removing tables, columns, indexes, or constraints.
---

1. Read the current schema and migration history.
2. Write the migration to add the smallest change that satisfies the requirement.
3. Add constraints and indexes that protect data integrity and query performance.
4. Check for data-loss risk: can existing rows survive the change?
5. Write a rollback plan or reversible migration where the framework supports it.
6. Run migrations against a test database.
7. Verify the application still passes relevant tests.
8. Document the change in `docs/architecture.md` or `docs/runbook.md` if operators need to know.
