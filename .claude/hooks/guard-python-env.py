"""
Python Environment Guard (graphify tooling only) — PreToolUse hook for Bash | PowerShell.

Denies Python tooling that would run from the global interpreter instead of the
project's .venv.  Only commands whose executable path contains ".venv" (or that
run through Docker) are allowed.  Creating the environment (`python -m venv`)
and version checks (`python --version`) are the only permitted global uses.

Stdin:  PreToolUse JSON payload  (tool_input.command)
Stdout: hookSpecificOutput with permissionDecision "deny", or nothing to allow.
"""
import json
import re
import sys

INTERPRETERS = frozenset({"python", "python3", "py", "pythonw"})

# Python tooling that must resolve to the project's .venv, never the global install.
# The C workflow runs through Docker and idf.py; Python remains only for graphify and
# the stdlib hook scripts.
VENV_ONLY = INTERPRETERS | frozenset({
    "pip", "pip3", "pipx", "conda", "poetry", "uv", "virtualenv", "graphify",
})

# First token of a segment: optional '&' call operator, then "quoted", 'quoted' or bare
FIRST_TOKEN_RE = re.compile(r"""^\s*&?\s*(?:"([^"]*)"|'([^']*)'|(\S+))(.*)$""", re.DOTALL)
ENV_ASSIGN_RE = re.compile(r"^\w+=")
PY_VERSION_SELECTOR_RE = re.compile(r"^-\d(\.\d+)?(-\d+)?$")  # py launcher: -3, -3.10, -3.10-64


HEREDOC_RE = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?[ \t]*\n.*?\n[ \t]*\1\b", re.DOTALL)
FALLBACK_SPLIT_RE = re.compile(r"\s*(?:;|&&|\|\||\||\n)\s*")


def _split_segments(cmd: str) -> list:
    """Split a command on ; && || | and newlines, but only outside quotes and heredocs.

    Text inside quotes (a commit message, a regex) and heredoc bodies is data, not
    commands. If a quote is left open the command is ambiguous, so fall back to a plain
    split (which errs towards checking more segments).
    """
    cmd = HEREDOC_RE.sub("<<HEREDOC", cmd)
    segments, current, quote, i = [], [], None, 0
    while i < len(cmd):
        ch = cmd[i]
        if quote:
            current.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            current.append(ch)
        elif ch in ";|\n" or cmd.startswith("&&", i):
            segments.append("".join(current))
            current = []
            if cmd.startswith("&&", i):
                i += 1
        else:
            current.append(ch)
        i += 1
    if quote:
        return FALLBACK_SPLIT_RE.split(cmd)
    segments.append("".join(current))
    return segments


def _basename(token: str) -> str:
    """Strip path prefixes and .exe suffix to get the bare executable name."""
    name = token.replace("\\", "/").rsplit("/", 1)[-1]
    return re.sub(r"(?i)\.exe$", "", name)


def _in_venv(token: str) -> bool:
    return ".venv" in token.replace("\\", "/").lower()


def _is_bootstrap(exe: str, args: list) -> bool:
    """Allow `python -m venv ...` and `python --version` from the global interpreter."""
    if exe not in INTERPRETERS:
        return False
    if exe == "py":
        args = [a for a in args if not PY_VERSION_SELECTOR_RE.match(a)]
    if args[:2] == ["-m", "venv"]:
        return True
    return bool(args) and args[0] in ("--version", "-V", "-VV")


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

        # Check each segment's first executable. A segment that starts with `docker` runs
        # in a container, so it is never in VENV_ONLY and passes.
        for segment in _split_segments(cmd):
            # Skip leading VAR=value assignments
            while True:
                stripped = segment.strip()
                first = stripped.split(None, 1)
                if first and ENV_ASSIGN_RE.match(first[0]):
                    segment = first[1] if len(first) > 1 else ""
                    continue
                break

            m = FIRST_TOKEN_RE.match(segment)
            if not m:
                continue
            token = m.group(1) or m.group(2) or m.group(3) or ""
            args = m.group(4).split()
            exe = _basename(token).lower()

            if exe not in VENV_ONLY or _in_venv(token) or _is_bootstrap(exe, args):
                continue

            _deny(
                f"Python environment policy violation: '{exe}' must not run from the "
                f"global interpreter. Use '.\\.venv\\Scripts\\{exe}.exe' (Python is only used for graphify here) "
                f"(create the environment once with 'python -m venv .venv'). "
                f"See .claude/rules/build.md."
            )
            return

    except Exception:
        # Never block the agent on hook failure
        pass


if __name__ == "__main__":
    main()
