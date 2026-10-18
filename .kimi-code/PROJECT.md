# Engineering Agent Configuration
> Reusable Kimi Code setup for disciplined full-stack product engineering.

## Status (updated 2026-10-18)
- Phase: prototype
- Working: custom agent loads, 8 skills discovered, repo pushed to Quattro-Commas/engineering-agent
- Broken / blocked: Playwright MCP not yet verified on this device (memory-constrained mobile environment)
- In-flight changes: none

## Stack and commands
- Runtime: Kimi Code CLI ≥ 2.2.0
- Install: clone into project root
- Run: `kimi --agent product-engineer`
- Skill invocation: `/skill:<name>`

## Architecture (5-10 lines)
- `AGENTS.md` holds the delivery contract and project rules.
- `.agents/agents/product-engineer.md` is the custom main agent.
- `.agents/skills/<workflow>/SKILL.md` are reusable procedures.
- `.kimi-code/mcp.json` configures the Playwright MCP server.
- `docs/` contains product brief, architecture, acceptance criteria, progress, and runbook.

## Conventions
- Skills must have `name` and `description` in YAML frontmatter.
- Agent bodies start with `${base_prompt}` to preserve default behavior.
- No secrets, tokens, or key values in committed files.
- Update `docs/progress.md` after each session.

## Decisions
- 2026-10-18: Use a dedicated repo instead of applying config to an existing project, so the setup is reusable across projects.
- 2026-10-18: Add Playwright MCP as the first external tool, because browser verification is the highest-value integration for UI work.

## Next steps
1. Verify Playwright MCP loads on a machine with sufficient memory.
2. Apply this configuration to a real project (e.g. TruthLedger) and build one vertical slice.
3. Add CI to validate agent/skill file syntax on pull requests.

## Open questions / risks
- Playwright MCP may be too heavy for the current mobile proot environment.
- Need to confirm `.kimi-code/mcp.json` format is exactly what Kimi 2.2.0 expects.
