---
name: browser-verification
description: Verify implemented user journeys in a real browser and add repeatable end-to-end tests.
whenToUse: After changing user-facing functionality or before declaring a feature complete.
---

1. Read the acceptance criteria for the changed feature.
2. Start the application using the repository's documented commands.
3. Confirm the required backend and database are available.
4. Use the configured browser tool to exercise the real user journey.
5. Check:
   - successful completion;
   - invalid input;
   - empty and loading states;
   - permission-denied behavior;
   - narrow and wide layouts;
   - keyboard interaction;
   - browser console and failed network requests.
6. Add or update automated end-to-end tests where appropriate.
7. Run the tests and record the actual results.
8. If browser tools are unavailable, report browser verification as blocked.
9. Never substitute a screenshot for functional testing.
10. Never claim the feature is complete while required checks are failing.
