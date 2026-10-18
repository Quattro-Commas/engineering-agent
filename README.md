# Engineering Agent Configuration

A reusable Kimi Code configuration that turns the CLI into a disciplined full-stack product-engineering agent.

## What this repo contains

- `AGENTS.md` — delivery contract and project rules.
- `.agents/agents/product-engineer.md` — custom main agent profile.
- `.agents/skills/*` — reusable skills for product discovery, architecture, UI, API, migrations, browser verification, security review, and release engineering.
- `.kimi-code/mcp.json` — Playwright MCP server for browser verification.
- `docs/` — product brief, architecture, acceptance criteria, progress log, and runbook.

## How to use it

1. Clone or copy this repo into your project root.
2. Start a new Kimi Code session with the product-engineer agent:
   ```bash
   cd /path/to/your-project
   kimi --agent product-engineer
   ```
3. Kimi discovers the project skills automatically from `.agents/skills/`.
4. Use `/skill:<name>` to invoke a specific skill, e.g.:
   ```text
   /skill:browser-verification
   ```

## Requirements

- Kimi Code CLI ≥ 2.2.0
- Node.js and npm (for Playwright MCP)
- A project that has real acceptance criteria and a runnable dev environment

## Status

Initial configuration committed on 2026-10-18. Ready for vertical-slice testing.
