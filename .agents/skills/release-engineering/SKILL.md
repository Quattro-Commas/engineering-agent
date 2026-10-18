---
name: release-engineering
description: Prepare a production build, CI, deployment configuration, and rollback instructions.
whenToUse: Before the first production deployment or before each release.
---

1. Read `docs/runbook.md` and existing CI configuration.
2. Ensure the production build command succeeds locally.
3. Ensure lint, type checks, and tests pass.
4. Review database migrations for production safety.
5. Verify required secrets are documented by name only, never by value.
6. Check deployment configuration for health checks and restart behavior.
7. Write or update rollback instructions.
8. Write or update backup and restore procedures for persistent data.
9. Run the full CI pipeline if possible.
10. Report what was verified and what still requires owner approval.
