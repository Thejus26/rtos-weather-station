"""
Feature Branch Reminder — UserPromptSubmit hook.

Reads context/current-feature.md and injects additional context when
a feature is "In Progress", so the agent never loses track of the active
/feature workflow lifecycle.

Stdin:  UserPromptSubmit JSON payload  (common fields)
Stdout: hookSpecificOutput with additionalContext, or nothing.
"""
import json
import os
import sys


def _resolve_project_root() -> str:
    """Resolve project root from script location: .claude/hooks/ -> root."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", ".."))


def main() -> None:
    try:
        # Consume stdin (required by contract even if unused)
        json.load(sys.stdin)

        feature_path = os.path.join(_resolve_project_root(), "context", "current-feature.md")

        if not os.path.isfile(feature_path):
            return

        with open(feature_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        # Extract title from first heading
        title = ""
        for line in lines:
            if line.startswith("# Current Feature:"):
                title = line.replace("# Current Feature:", "").strip()
                break
            if line.startswith("# Current Feature"):
                title = line.replace("# Current Feature", "").strip()
                break

        # Extract status (first non-empty line after "## Status")
        status = ""
        in_status = False
        for line in lines:
            if line.strip() == "## Status":
                in_status = True
                continue
            if in_status and line.strip():
                status = line.strip()
                break

        # Only inject when a feature is actively in progress
        if status == "In Progress" and title:
            json.dump({
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": (
                        f"Active feature: {title} | Status: {status}. "
                        f"Follow the /feature workflow and the Python (.venv-only) environment policy."
                    ),
                }
            }, sys.stdout)

    except Exception:
        pass


if __name__ == "__main__":
    main()
