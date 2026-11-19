"""
Unsafe Code Sentry — PreToolUse hook for write_to_file | replace_file_content.

Inspects Python source being written and flags constructs that are dangerous in
an LLM agent, where tool arguments are controlled by the model (and, through
prompt injection, by whatever text the model has read): eval/exec, shell
execution, unsafe deserialization.  Uses "ask" (not "deny") so the user can
still approve a deliberate, reviewed use.

A line carrying a `# unsafe-ok: <reason>` comment is skipped.

Stdin:  PreToolUse JSON payload  (toolCall.name, toolCall.args)
Stdout: {"decision": "allow"|"ask", "reason": "..."}
"""
import json
import os
import re
import sys

# (regex, human-readable label).  The lookbehind keeps `model.eval()` / `obj.exec()` out.
UNSAFE_PATTERNS = [
    (r"(?<![\w.])eval\s*\(", "eval()"),
    (r"(?<![\w.])exec\s*\(", "exec()"),
    (r"\bos\.system\s*\(", "os.system()"),
    (r"\bos\.popen\s*\(", "os.popen()"),
    (r"\bshell\s*=\s*True\b", "subprocess with shell=True"),
    (r"\bpickle\.loads?\s*\(", "pickle.load(s)()"),
    (r"\bmarshal\.loads?\s*\(", "marshal.load(s)()"),
    (r"\byaml\.load\s*\(", "yaml.load() (use yaml.safe_load)"),
    (r"(?<![\w.])__import__\s*\(", "__import__()"),
]

ALLOW_MARKER = "unsafe-ok"


def _find_unsafe(content: str):
    """Return the label of the first unsafe construct found, or None."""
    for line in content.splitlines():
        if ALLOW_MARKER in line:
            continue
        code = re.sub(r"#.*$", "", line)  # drop comments to reduce false positives
        for pattern, label in UNSAFE_PATTERNS:
            if re.search(pattern, code):
                return label
    return None


def main() -> None:
    try:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        data = json.load(sys.stdin)
        tool = data.get("toolCall", {})
        name = tool.get("name", "")
        args = tool.get("args", {})

        target_file = args.get("TargetFile", "")

        # Only inspect .py files
        if not target_file.lower().endswith(".py"):
            json.dump({"decision": "allow"}, sys.stdout)
            return

        # Pick the right content field for the tool
        if name == "write_to_file":
            content = args.get("CodeContent", "")
        elif name == "replace_file_content":
            content = args.get("ReplacementContent", "")
        else:
            json.dump({"decision": "allow"}, sys.stdout)
            return

        label = _find_unsafe(content)
        if label:
            basename = os.path.basename(target_file)
            json.dump({
                "decision": "ask",
                "reason": (
                    f"⚠️ Unsafe construct {label} in '{basename}'. Tool arguments are "
                    f"model-controlled, so this can become code or command injection. "
                    f"Confirm it is intentional, or add '# unsafe-ok: <reason>' to the line."
                ),
            }, sys.stdout)
            return

        json.dump({"decision": "allow"}, sys.stdout)

    except Exception:
        json.dump({"decision": "allow"}, sys.stdout)


if __name__ == "__main__":
    main()
