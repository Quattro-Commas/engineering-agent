---
name: frontend-ui
description: Implement responsive, accessible user interfaces with complete state handling and reusable components.
whenToUse: When building or changing user-facing pages, components, or design tokens.
---

1. Read the acceptance criteria for the feature.
2. Identify existing components, design tokens, and conventions.
3. Implement the UI for the success path first.
4. Add and verify:
   - loading states;
   - empty states;
   - validation errors;
   - permission-denied states;
   - general error states.
5. Ensure responsive layouts for mobile and desktop.
6. Ensure keyboard operability and focus management.
7. Add or update automated component tests where the project supports them.
8. Use browser verification for the actual user journey.
9. Do not ship mock data as real functionality.
