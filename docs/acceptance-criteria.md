# Acceptance Criteria

## AC-1: Agent loads

Given a fresh clone of this repo in a project root, when I run `kimi --agent product-engineer`, then the session starts with the `product-engineer` profile.

## AC-2: Skills are discoverable

Given the repo is in a project root, when I run `kimi` and type `/skill:browser-verification`, then the skill is found and its steps are available.

## AC-3: Browser MCP is configured

Given Node.js and npm are installed, when Kimi loads `.kimi-code/mcp.json`, then the Playwright MCP server is listed under available MCP servers.

## AC-4: Delivery contract is enforced

Given a `product-engineer` session, when asked to mark a feature complete, then the agent checks the `AGENTS.md` delivery contract before agreeing.

## AC-5: Reproducible setup

Given a new project directory, when I copy these files into it, then `kimi --agent product-engineer` behaves the same way as in the source repo.
