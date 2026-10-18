# Runbook

## Start a product-engineer session

```bash
cd /path/to/project
kimi --agent product-engineer
```

## Invoke a skill

Inside the session:

```text
/skill:browser-verification
```

## Verify MCP servers are available

Inside the session:

```text
/mcp
```

## Update this configuration

1. Edit the relevant file in `.agents/` or `docs/`.
2. Run tests or a trial session to confirm behavior.
3. Commit with a descriptive message.
4. Push to `Quattro-Commas/engineering-agent`.

## Troubleshooting

- If the agent does not load, confirm the file is at `.agents/agents/product-engineer.md` and has valid YAML frontmatter.
- If a skill is missing, check that its directory contains `SKILL.md` with `name` and `description` in the frontmatter.
- If Playwright MCP fails, confirm `npx @playwright/mcp@latest` runs in the project directory and that Node.js and npm are installed.
