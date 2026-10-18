# Architecture

## Components

| Component | Path | Purpose |
|-----------|------|---------|
| Delivery contract | `AGENTS.md` | Persistent rules for what "complete" means. |
| Custom agent | `.agents/agents/product-engineer.md` | Specialist role that preserves the base prompt. |
| Reusable skills | `.agents/skills/<workflow>/SKILL.md` | Step-by-step procedures for repeated workflows. |
| Browser tool | `.kimi-code/mcp.json` | Playwright MCP server for real browser verification. |
| Living docs | `docs/` | Product brief, architecture, acceptance criteria, progress, runbook. |

## How Kimi discovers the configuration

- Kimi Code CLI scans `.agents/agents/` and `.agents/skills/` in the workspace.
- Custom agents are selected with `--agent <name>`.
- Skills are invoked with `/skill:<name>` or matched by their description.
- Project-level MCP servers are loaded from `.kimi-code/mcp.json`.

## Suggested default stack for target projects

- Next.js + TypeScript for the web application.
- PostgreSQL when persistent relational data is required.
- FastAPI only when a separate Python backend is justified.
- Docker Compose for required local services.
- Automated lint, type checks, tests, and production builds.
- Playwright for important user journeys.

Add other infrastructure only when requirements justify it.

## Constraints

- Do not add Kubernetes, microservices, queues, vector databases, or large monitoring stacks without a concrete requirement.
- For ordinary CRUD websites, start with Next.js and PostgreSQL; justify a separate FastAPI service before adding one.
