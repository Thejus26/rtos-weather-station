"""
Python Environment Guard — PreToolUse hook for Bash | PowerShell.

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

# Executables that must resolve to the project's .venv, never the global install
VENV_ONLY = INTERPRETERS | frozenset({
    "pip", "pip3", "pipx", "conda", "poetry", "uv", "virtualenv",
    "pytest", "ruff", "mypy", "black", "isort", "flake8", "pylint",
})

# First token of a segment: optional '&' call operator, then "quoted", 'quoted' or bare
FIRST_TOKEN_RE = re.compile(r"""^\s*&?\s*(?:"([^"]*)"|'([^']*)'|(\S+))(.*)$""", re.DOTALL)
ENV_ASSIGN_RE = re.compile(r"^\w+=")
PY_VERSION_SELECTOR_RE = re.compile(r"^-\d(\.\d+)?(-\d+)?$")  # py launcher: -3, -3.10, -3.10-64


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

        # Commands that run through Docker are isolated from the host interpreter
        if re.search(r"\bdocker\b", cmd, re.IGNORECASE):
            return

        # Split on shell chaining operators (; && || |) and check each segment
        for segment in re.split(r"\s*(?:;|&&|\|\||\|)\s*", cmd):
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
                f"global interpreter. Use '.\\.venv\\Scripts\\python.exe -m <tool> ...' "
                f"(create the environment once with 'python -m venv .venv'). "
                f"See .claude/rules/build.md."
            )
            return

    except Exception:
        # Never block the agent on hook failure
        pass


if __name__ == "__main__":
    main()
