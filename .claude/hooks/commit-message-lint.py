"""
Commit Message Lint — PreToolUse hook for Bash | PowerShell.

Validates that git commit messages follow Conventional Commits format:
  type(scope): description
  type: description

Allowed types: feat, fix, docs, test, chore, refactor, style, perf, ci, build, revert, merge

Only the subject (first line) of the message is checked.  Supported message forms:
  -m "msg" / -m 'msg' / --message=...
  -m "$(cat <<'EOF' ... EOF)"      (bash heredoc)
  -m @'...'@                       (PowerShell here-string)

Stdin:  PreToolUse JSON payload  (tool_input.command)
Stdout: hookSpecificOutput with permissionDecision "deny", or nothing to allow.
"""
import json
import re
import sys

TYPES = "feat|fix|docs|test|chore|refactor|style|perf|ci|build|revert|merge"

# type(optional-scope)optional-!: description
CONVENTIONAL_RE = re.compile(
    rf"^({TYPES})"
    r"(\([^)]+\))?"   # optional scope
    r"!?"              # optional breaking-change marker
    r":\s+.+"          # colon, space, description
)

HEREDOC_RE = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?[ \t]*\n(.*?)\n[ \t]*\1\b", re.DOTALL)
PS_HERESTRING_RE = re.compile(r"@(['\"])\s*\n(.*?)\n\1@", re.DOTALL)
MSG_RE = re.compile(r"""(?:-m|--message)(?:\s+|=)(?:"([^"]+)"|'([^']+)')""", re.DOTALL)


def _extract_message(cmd: str):
    """Return the commit message from a git commit command, or None if inline text is absent."""
    for pattern, group in ((HEREDOC_RE, 2), (PS_HERESTRING_RE, 2)):
        m = pattern.search(cmd)
        if m:
            return m.group(group)
    m = MSG_RE.search(cmd)
    if m:
        return m.group(1) or m.group(2)
    return None


def _deny(reason: str) -> None:
    json.dump({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, sys.stdout)


def main() -> None:
    try:
        data = json.load(sys.stdin)
        cmd = data.get("tool_input", {}).get("command", "")

        # Only inspect git commit commands
        if "git commit" not in cmd:
            return

        # Skip amend/fixup/squash — they reuse existing messages
        if any(flag in cmd for flag in ("--amend", "--fixup", "--squash")):
            return

        message = _extract_message(cmd)
        if message is None:
            # No inline message (editor-based commit) — allow
            return

        lines = message.strip().splitlines()
        subject = lines[0].strip() if lines else ""

        if not CONVENTIONAL_RE.match(subject):
            _deny(
                "Commit message doesn't follow Conventional Commits format.\n"
                "Expected: type(scope): description\n"
                f"Allowed types: {TYPES}\n"
                f"Got: '{subject}'"
            )

    except Exception:
        pass


if __name__ == "__main__":
    main()
