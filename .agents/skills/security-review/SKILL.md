---
name: security-review
description: Review changes against a concrete OWASP ASVS-derived checklist before release.
whenToUse: Before declaring a release ready or after significant auth, input, or data-flow changes.
---

1. Read the acceptance criteria and the changed code.
2. Check authentication and session handling:
   - passwords or tokens are not stored in code or logs;
   - sessions expire and can be revoked.
3. Check authorization:
   - every sensitive action verifies the user's right to perform it;
   - identifiers from the URL or body are not trusted for access control.
4. Check input validation:
   - all inputs are validated on the server;
   - injection risks are parameterized or escaped.
5. Check output encoding for XSS prevention.
6. Check secrets management:
   - no keys, tokens, or passwords in commits;
   - environment variables are documented by name only.
7. Check error handling:
   - errors do not leak internal paths, stack traces, or secrets.
8. Record findings and required fixes in `docs/progress.md`.
9. Do not treat a checklist pass as a penetration test.
