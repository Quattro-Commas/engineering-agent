---
name: bootstrap
description: Orient to a directory, classify its project state, and apply the engineering-agent configuration so future sessions start informed.
whenToUse: When starting work in a new or unfamiliar repo, or when applying the engineering-agent configuration to a fresh project.
---

1. Read the applicable `AGENTS.md` for the workspace before making changes.
2. Classify the directory using cheap checks:
   - Does `.kimi-code/PROJECT.md` already exist?
   - Is the folder inside a git work tree?
   - What manifests and code are present (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.)?
3. If the directory is a known project (`.kimi-code/PROJECT.md` exists):
   - Read `PROJECT.md` and report its one-liner, status, in-flight changes, and first next step.
   - Ask whether to continue with the recorded next step or tackle something else.
4. If the directory is an existing repo with no memory:
   - Summarise what the repo appears to be from its files and manifests.
   - Create `.kimi-code/PROJECT.md` from the project-brief template, filling in only facts from files, git history, or the user; mark guesses with `(unverified)`.
   - Create or update `AGENTS.md` with build/test commands and conventions discovered in the repo.
   - Ask before overwriting any existing project-specific rules.
5. If the directory is new or empty:
   - Ask the user for the project idea and scope.
   - Create `.kimi-code/PROJECT.md` and `AGENTS.md` as minimal living briefs.
6. Apply the engineering-agent configuration when requested:
   - Copy or symlink `AGENTS.md`, `.agents/agents/product-engineer.md`, `.agents/skills/`, and `.kimi-code/mcp.json` from the engineering-agent repo into the target project root.
   - Preserve any existing project-specific rules in the target `AGENTS.md` by merging rather than replacing.
   - Never copy secrets, tokens, or key values.
7. Record the outcome in `docs/progress.md` (or `PROJECT.md` if no `docs/` exists) and update the next steps list.
8. Report what was created, what remains unverified, and the exact command to start a session with the product-engineer agent.
