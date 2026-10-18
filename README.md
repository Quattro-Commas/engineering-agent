# Engineering Agent Configuration

A reusable Kimi Code configuration that turns the CLI into a disciplined full-stack product-engineering agent.

## What this repo contains

- `AGENTS.md` — delivery contract and project rules.
- `.agents/agents/product-engineer.md` — custom main agent profile.
- `.agents/skills/*` — reusable skills for project bootstrap, prompt engineering, product discovery, architecture, UI, API, migrations, browser verification, security review, and release engineering.
- `.kimi-code/mcp.json` — Playwright MCP server for browser verification.
- `SYSTEM.md` — template for a user-level system prompt that applies prompt-engineering discipline to every session.
- `kimi.plugin.json` — plugin manifest so the whole configuration can be installed via `/plugins install`.
- `hooks/` — lifecycle hooks, including `UserPromptSubmit` prompt engineering.
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
   /skill:bootstrap
   /skill:browser-verification
   ```

## Bootstrapping a new project

Start Kimi in an empty or existing project folder and invoke the bootstrap skill:

```bash
cd /path/to/your-project
kimi --agent product-engineer
```

Then ask:

```text
/skill:bootstrap
```

The agent will orient to the directory, classify its state, and create or update `AGENTS.md` and `.kimi-code/PROJECT.md` so future sessions start informed.

## Automated prompt engineering

The `product-engineer` agent automatically reframes every request into a structured software-engineering prompt (goal, context, acceptance criteria, scope, constraints, verification plan, risks) before acting.

To rewrite a prompt explicitly without acting on it:

```text
/skill:prompt-engineer fix the login bug
```

For **global** automation across every Kimi session — not just sessions started with `--agent product-engineer` — copy `SYSTEM.md` to your user-level Kimi home:

```bash
cp SYSTEM.md ~/.kimi-code/SYSTEM.md
```

This replaces the default main-agent system prompt with the prompt-engineering discipline. Changes take effect in new sessions.

## Install as a Kimi Code plugin

For the most automatic setup, install the repo as a plugin. This enables the prompt-engineering `UserPromptSubmit` hook and injects the discipline into every session, regardless of which agent you select.

```bash
/plugins install https://github.com/Quattro-Commas/engineering-agent
```

Then reload or start a new session:

```bash
/reload
```

The plugin ships:

- All engineering-agent skills under `/skill:<name>`
- The `product-engineer` agent available as a sub-agent
- A `UserPromptSubmit` hook that scaffolds vague requests
- Playwright MCP for browser verification

## Validation

Run the local validation script before committing changes to agent or skill files:

```bash
python3 scripts/validate-config.py
```

CI runs the same script on every push and pull request.

## Requirements

- Kimi Code CLI ≥ 2.2.0
- Node.js and npm (for Playwright MCP)
- A project that has real acceptance criteria and a runnable dev environment

## Status

Initial configuration committed on 2026-10-18. Ready for vertical-slice testing.
