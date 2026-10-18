---
name: prompt-engineer
description: Rewrite a vague or informal request into a structured, high-quality software-engineering prompt with goal, context, acceptance criteria, scope, constraints, verification, and risks.
whenToUse: When the user's request is vague, underspecified, or needs to be turned into a disciplined engineering task before work begins.
---

Rewrite the user's request into a high-quality software-engineering prompt. Preserve the original intent, but structure it so an agent can act on it directly.

Output format (use exactly these sections):

```
## Goal
One-sentence objective: what must become true.

## Context
- Current repository / project
- Relevant files, branches, or prior decisions
- Stack, runtime, or tooling constraints already known

## Acceptance criteria
- Measurable, checkable outcomes that prove done
- Include at least one verification command or observable result

## Scope
- In scope:
- Out of scope:

## Constraints and conventions
- Build/test/lint commands to use
- Approval boundaries (deployments, credentials, destructive ops)
- Existing patterns or anti-patterns from AGENTS.md / PROJECT.md

## Verification plan
1. Step the agent should take to prove correctness
2. Expected result

## Risks / open questions
- What could make this harder than it looks
- What is still unknown
```

Rules:
- Do not invent facts. Use only what the user supplied, the repo files, or the conversation context. Mark guesses with `(unverified)`.
- If the request is already well-specified, return it largely unchanged but confirm the acceptance criteria and verification plan.
- Keep the reframed prompt actionable; avoid analysis paralysis.
- Do not start implementing the task unless the user explicitly asks you to after seeing the reframed prompt.
