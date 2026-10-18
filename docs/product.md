# Product: Engineering Agent Configuration

## Problem

Kimi Code is a capable general-purpose agent, but turning an idea into a complete, tested, deployed product requires a repeatable engineering workflow. Without explicit constraints, agents can stop at code, mock data, or untested optimism.

## Users

- Solo builders who want Kimi to deliver working software, not just snippets.
- Small teams who want a shared, versioned agent configuration.
- Projects that need auditable acceptance criteria and real browser verification.

## Core value

A small, auditable configuration that makes Kimi Code behave like a disciplined full-stack product engineer: plan, build one vertical slice, verify in a browser, document, and hand off.

## Non-goals

- Replace human judgment in architecture or security.
- Provide a one-click autonomous build for any project.
- Cover every possible framework or infrastructure stack.

## Acceptance criteria

1. `kimi --agent product-engineer` starts a session that loads the custom agent.
2. Project skills are discovered from `.agents/skills/`.
3. Browser verification can be invoked via the Playwright MCP server.
4. The delivery contract in `AGENTS.md` is enforced in every session.
5. Setup is reproducible from this repo in a fresh project.
