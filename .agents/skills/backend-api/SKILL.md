---
name: backend-api
description: Build server-side logic with input validation, permissions, consistent errors, and integration tests.
whenToUse: When adding or changing API endpoints, background jobs, or server-side workflows.
---

1. Read the acceptance criteria and existing API conventions.
2. Design the endpoint or function contract: inputs, outputs, errors.
3. Implement server-side validation for all inputs.
4. Enforce authorization before business logic.
5. Return consistent error shapes and HTTP status codes.
6. Keep business rules on the server; do not trust the client.
7. Write integration tests for the success path and representative failure paths.
8. Run the tests and record results.
9. Update API documentation if the project maintains it.
