#!/usr/bin/env python3
"""Validate engineering-agent configuration files.

Checks:
- Agent files have required YAML frontmatter (name, description).
- Agent bodies contain ${base_prompt}.
- Skill files have required YAML frontmatter (name, description).
- Skill names match their containing directory names.
- No obvious secret-like strings appear in committed files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = REPO_ROOT / ".agents" / "agents"
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"

# Flag common secret-bearing keys with non-empty values.
SECRET_KEY_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|client_secret|app_secret|password|passwd|"
    r"private[_-]?key|token|access_token|auth_token|bearer)\s*[:=]\s*\S+",
    re.MULTILINE,
)

EXCLUDE_SECRET_FILES = {
    "LICENSE",
    ".gitignore",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("---", 3)
    if end == -1:
        raise ValueError("missing closing frontmatter delimiter")
    fm = text[3:end].strip()
    if not fm:
        raise ValueError("empty frontmatter")
    data: dict[str, str] = {}
    for line in fm.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_agent(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        fm = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{path}: {exc}"]
    for key in ("name", "description"):
        if not fm.get(key):
            errors.append(f"{path}: missing frontmatter key '{key}'")
    body = path.read_text(encoding="utf-8").split("---", 2)[-1]
    if "${base_prompt}" not in body:
        errors.append(f"{path}: agent body must contain '${base_prompt}'")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        fm = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{path}: {exc}"]
    for key in ("name", "description"):
        if not fm.get(key):
            errors.append(f"{path}: missing frontmatter key '{key}'")
    expected_name = path.parent.name
    if fm.get("name") != expected_name:
        errors.append(
            f"{path}: frontmatter name '{fm.get('name')}' does not match directory '{expected_name}'"
        )
    return errors


def validate_no_secrets() -> list[str]:
    errors: list[str] = []
    text_extensions = {".md", ".json", ".toml", ".yaml", ".yml", ".py", ".sh", ".txt"}
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name in EXCLUDE_SECRET_FILES:
            continue
        if ".git" in path.parts:
            continue
        if path.suffix not in text_extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SECRET_KEY_RE.search(text):
            errors.append(f"{path}: possible secret/key value found (review manually)")
    return errors


def main() -> int:
    all_errors: list[str] = []

    if AGENTS_DIR.exists():
        for agent_file in sorted(AGENTS_DIR.glob("*.md")):
            all_errors.extend(validate_agent(agent_file))

    if SKILLS_DIR.exists():
        for skill_file in sorted(SKILLS_DIR.rglob("SKILL.md")):
            all_errors.extend(validate_skill(skill_file))

    all_errors.extend(validate_no_secrets())

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for error in all_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Configuration validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
