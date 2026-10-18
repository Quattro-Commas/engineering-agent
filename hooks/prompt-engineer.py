#!/usr/bin/env python3
"""UserPromptSubmit hook: scaffold vague software requests into structured engineering prompts.

The hook receives the Kimi Code event payload on stdin and writes the scaffold to stdout.
Anything printed to stdout is appended to the conversation context.
"""

import json
import re
import sys

SKIP_PATTERNS = [
    re.compile(r"^\s*/"),  # slash commands
    re.compile(r"^(hi|hello|hey|ok|thanks|thank you|bye)\s*$", re.I),
]

REQUIRED_SECTIONS = ["goal:", "acceptance criteria:", "verification plan:"]


def extract_text(value) -> str:
    """Handle string prompt or ContentPart[] array."""
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, list):
        parts = []
        for part in value:
            if isinstance(part, dict) and part.get("type") == "text":
                text = part.get("text", "")
                if isinstance(text, str):
                    parts.append(text)
        return " ".join(parts).strip()
    return ""


def extract_prompt(payload: dict) -> str:
    for key in ("prompt", "text", "message", "content"):
        value = payload.get(key)
        text = extract_text(value)
        if text:
            return text
    return ""


def should_skip(prompt: str) -> bool:
    if len(prompt) < 10:
        return True
    for pattern in SKIP_PATTERNS:
        if pattern.match(prompt):
            return True
    lower = prompt.lower()
    if all(section in lower for section in REQUIRED_SECTIONS):
        return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    prompt = extract_prompt(payload)
    if not prompt or should_skip(prompt):
        return 0

    print(
        f"""Reframe this request as a disciplined engineering task before acting:

- Goal: {prompt}
- Context: inspect repo state, relevant files, and prior decisions
- Acceptance criteria: define measurable, checkable outcomes
- Scope: state what is in scope and what is explicitly out of scope
- Constraints: honor AGENTS.md / PROJECT.md, existing conventions, and approval boundaries
- Verification plan: list commands or observations that prove correctness
- Risks / open questions: flag unknowns that could change the approach

If a critical requirement is missing, ask a targeted question. Otherwise proceed with the reframed task.""",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
