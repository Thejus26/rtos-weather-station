"""
C Code Guard — PreToolUse hook for Write | Edit | MultiEdit.

Inspects C source being written under main/ and components/ and enforces the
project rules that are cheap to check on text (context/coding-standards.md):

  * deny : ESP-IDF, FreeRTOS or driver includes in components/app_logic/ (must stay
           pure C so it builds in the host test container)
  * ask  : dynamic allocation in main/ or components/. Covers malloc, calloc, realloc,
           free, heap_caps_*, pvPortMalloc, vPortFree, strdup, strndup, asprintf and
           vasprintf. Other allocating APIs (cJSON_Print*, ...) are NOT detected.
  * ask  : hard-coded Wi-Fi credentials (.ssid/.password assigned a string literal, or
           strcpy/strncpy/memcpy of a literal into a field named ssid/password/pass) and
           hard-coded mqtt:// or mqtts:// broker URLs (use menuconfig/NVS)

This is a text heuristic, not a parser: it is a cheap reminder, not proof of compliance.
A line carrying a `rule-ok: <reason>` comment is skipped. Paths are judged relative to
the project root, so a checkout under a folder named "main" does not confuse it.

Stdin:  PreToolUse JSON payload  (tool_name, tool_input)
Stdout: hookSpecificOutput with permissionDecision "deny" or "ask", or nothing to allow.
"""
import json
import os
import re
import sys

C_EXTENSIONS = (".c", ".h", ".cpp", ".hpp")
ALLOW_MARKER = "rule-ok"

# Headers that components/app_logic/ must never include.
FORBIDDEN_INCLUDE_RE = re.compile(
    r'^\s*#\s*include\s*[<"]\s*(freertos/|esp_|driver/|nvs|soc/|hal/|lwip/|mqtt_client|sdkconfig)'
)
ALLOC_RE = re.compile(
    r"(?<![\w.>])(?:heap_caps_(?:malloc|calloc|realloc|free)|pvPortMalloc|vPortFree|"
    r"strn?dup|v?asprintf|malloc|calloc|realloc|free)\s*\("
)
SECRET_RES = [
    (re.compile(r'"mqtts?://'), "a hard-coded broker URL"),
    (re.compile(r'\.(?:ssid|password)\s*=\s*"[^"]+"'), "a hard-coded Wi-Fi credential"),
    (re.compile(r'\b(?:strn?cpy|memcpy)\s*\([^;]*\b(?:ssid|password|passwd|pass)\b[^;]*,\s*"[^"]+"'),
     "a hard-coded Wi-Fi credential"),
]

STRING_RE = re.compile(r'"(?:\x5c.|[^"\x5c])*"')  # \x5c is a backslash
BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/")

# <project>/.claude/hooks/this_file.py -> <project>
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _relative_path(path: str):
    """Project-relative path with forward slashes, or None if outside the project."""
    try:
        rel = os.path.relpath(os.path.abspath(path), PROJECT_ROOT)
    except ValueError:  # different drive on Windows
        return None
    rel = rel.replace("\\", "/")
    return None if rel.startswith("..") else rel.lower()


def _written_content(name: str, args: dict) -> str:
    """Return the text being introduced by the tool call."""
    if name == "Write":
        return args.get("content", "")
    if name == "Edit":
        return args.get("new_string", "")
    if name == "MultiEdit":
        return "\n".join(e.get("new_string", "") for e in args.get("edits", []))
    return ""


def _code_only(line: str) -> str:
    """Drop string literals and comments so identifiers inside them don't match."""
    line = STRING_RE.sub('""', line)
    line = BLOCK_COMMENT_RE.sub("", line)
    return re.sub(r"//.*$", "", line)


def _find_violation(content: str, path: str):
    """Return (decision, label) for the first violation found, or None."""
    rel = _relative_path(path)
    if rel is None:
        return None
    in_app_logic = rel.startswith("components/app_logic/")
    in_firmware = rel.startswith(("main/", "components/"))
    ask = None
    in_block = False  # inside a multi-line /* ... */ comment
    for line in content.splitlines():
        if in_block:
            if "*/" in line:
                in_block = line.rfind("/*") > line.rfind("*/")
            continue
        in_block = line.rfind("/*") > line.rfind("*/")
        if ALLOW_MARKER in line:
            continue
        if in_app_logic and FORBIDDEN_INCLUDE_RE.match(line):
            return ("deny", "an ESP-IDF/FreeRTOS include in components/app_logic/ "
                            "(it must stay pure C)")
        if not in_firmware or ask:
            continue
        stripped = line.lstrip()
        if stripped.startswith(("//", "/*", "*")):
            continue
        if ALLOC_RE.search(_code_only(line)):
            ask = ("ask", "dynamic allocation (no malloc/free in steady state)")
            continue
        for pattern, label in SECRET_RES:
            if pattern.search(line):
                ask = ("ask", label + " (use menuconfig/NVS)")
                break
    return ask


def main() -> None:
    try:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        data = json.load(sys.stdin)
        name = data.get("tool_name", "")
        args = data.get("tool_input", {})

        target_file = args.get("file_path", "")
        if not target_file.lower().endswith(C_EXTENSIONS):
            return

        found = _find_violation(_written_content(name, args), target_file)
        if found:
            decision, label = found
            json.dump({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": decision,
                    "permissionDecisionReason": (
                        f"{os.path.basename(target_file)}: {label}. See "
                        f"context/coding-standards.md sections 5 and 7. If this is deliberate "
                        f"(for example allocation in startup code), add a "
                        f"'/* rule-ok: <reason> */' comment to the line."
                    ),
                }
            }, sys.stdout)

    except Exception:
        pass


if __name__ == "__main__":
    main()
