"""
Commit Message Lint — PreToolUse hook for run_command.

Validates that git commit messages follow Conventional Commits format:
  type(scope): description
  type: description

Allowed types: feat, fix, docs, test, chore, refactor, style, perf, ci, build, revert

Stdin:  PreToolUse JSON payload  (toolCall.args.CommandLine)
Stdout: {"decision": "allow"|"deny", "reason": "..."}
"""
import json
import re
import sys

# Conventional Commits pattern
# type(optional-scope)optional-!: description
CONVENTIONAL_RE = re.compile(
    r"^(feat|fix|docs|test|chore|refactor|style|perf|ci|build|revert)"
    r"(\([^)]+\))?"   # optional scope
    r"!?"              # optional breaking-change marker
    r":\s+.+"          # colon, space, description
)

# Patterns to extract -m message from a command line
# Handles: -m "msg", -m 'msg', -m "msg with 'quotes'"
MSG_RE = re.compile(r"""-m\s+(?:"([^"]+)"|'([^']+)')""")


def main() -> None:
    try:
        data = json.load(sys.stdin)
        cmd = data.get("toolCall", {}).get("args", {}).get("CommandLine", "")

        # Only inspect git commit commands
        if "git commit" not in cmd:
            json.dump({"decision": "allow"}, sys.stdout)
            return

        # Skip amend/fixup/squash — they reuse existing messages
        if any(flag in cmd for flag in ("--amend", "--fixup", "--squash")):
            json.dump({"decision": "allow"}, sys.stdout)
            return

        # Extract the -m message
        match = MSG_RE.search(cmd)
        if not match:
            # No inline -m message (editor-based commit) — allow
            json.dump({"decision": "allow"}, sys.stdout)
            return

        message = match.group(1) or match.group(2)

        if CONVENTIONAL_RE.match(message):
            json.dump({"decision": "allow"}, sys.stdout)
        else:
            allowed = "feat|fix|docs|test|chore|refactor|style|perf|ci|build|revert"
            json.dump({
                "decision": "deny",
                "reason": (
                    f"\U0001f4dd Commit message doesn't follow Conventional Commits format.\n"
                    f"Expected: type(scope): description\n"
                    f"Allowed types: {allowed}\n"
                    f"Got: '{message}'"
                ),
            }, sys.stdout)

    except Exception:
        json.dump({"decision": "allow"}, sys.stdout)


if __name__ == "__main__":
    main()
