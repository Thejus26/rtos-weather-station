"""
Commit Message Lint — PreToolUse hook for run_command.

Validates that git commit messages follow Conventional Commits format:
  type(scope): description
  type: description

Allowed types: feat, fix, docs, test, chore, refactor, style, perf, ci, build, revert, merge

Only the subject (first line) of the message is checked.  Supported message forms:
  -m "msg" / -m 'msg' / --message=...
  -m "$(cat <<'EOF' ... EOF)"      (bash heredoc)
  -m @'...'@                       (PowerShell here-string)

A `git commit` mentioned inside a heredoc body or inside quotes is not a commit and is
ignored.

Stdin:  PreToolUse JSON payload  (toolCall.args.CommandLine)
Stdout: {"decision": "allow"|"deny", "reason": "..."}
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

# `git [options] commit` at the start of a command (after ; && || | ( or a newline)
GIT_COMMIT_RE = re.compile(r"(?m)(?:^|[;&|(])\s*git(?:\s+-\S+(?:\s+[^\s-]\S*)?)*\s+commit\b")


def _commit_tail(cmd: str):
    """Return the text from a real `git commit` invocation onwards, or None."""
    spans = [m.span() for m in HEREDOC_RE.finditer(cmd)]
    for m in GIT_COMMIT_RE.finditer(cmd):
        if not any(start <= m.start() < end for start, end in spans):
            return cmd[m.start():]
    return None


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


def _allow() -> None:
    json.dump({"decision": "allow"}, sys.stdout)


def main() -> None:
    try:
        data = json.load(sys.stdin)
        cmd = data.get("toolCall", {}).get("args", {}).get("CommandLine", "")

        # Only inspect real git commit commands
        cmd = _commit_tail(cmd)
        if cmd is None:
            _allow()
            return

        # Skip amend/fixup/squash — they reuse existing messages
        if any(flag in cmd for flag in ("--amend", "--fixup", "--squash")):
            _allow()
            return

        message = _extract_message(cmd)
        if message is None:
            # No inline message (editor-based commit) — allow
            _allow()
            return

        lines = message.strip().splitlines()
        subject = lines[0].strip() if lines else ""

        if CONVENTIONAL_RE.match(subject):
            _allow()
        else:
            json.dump({
                "decision": "deny",
                "reason": (
                    f"\U0001f4dd Commit message doesn't follow Conventional Commits format.\n"
                    f"Expected: type(scope): description\n"
                    f"Allowed types: {TYPES}\n"
                    f"Got: '{subject}'"
                ),
            }, sys.stdout)

    except Exception:
        _allow()


if __name__ == "__main__":
    main()
