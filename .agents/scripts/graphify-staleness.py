"""
Graphify Staleness Check — Stop hook.

Compares graphify-out/graph.json modification time against the latest git
commit timestamp.  If the graph is stale, blocks the stop and asks the
agent to run a graphify update before finishing.

Stdin:  Stop JSON payload  (terminationReason, fullyIdle, etc.)
Stdout: {"decision": "continue"|"stop", "reason": "..."}
"""
import json
import os
import subprocess
import sys


def _resolve_project_root() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", ".."))


def main() -> None:
    try:
        data = json.load(sys.stdin)

        # Only intercept natural model stops, not errors or max-step limits
        reason = data.get("terminationReason", "")
        if reason not in ("model_stop", ""):
            json.dump({"decision": "stop"}, sys.stdout)
            return

        project_root = _resolve_project_root()
        graph_path = os.path.join(project_root, "graphify-out", "graph.json")

        if not os.path.isfile(graph_path):
            json.dump({
                "decision": "continue",
                "reason": (
                    "\U0001f4ca graphify-out/graph.json not found. "
                    "Run: & .\\.venv\\Scripts\\graphify.exe . --update --code-only"
                ),
            }, sys.stdout)
            return

        graph_mtime = os.path.getmtime(graph_path)

        # Get latest git commit epoch timestamp
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct"],
            capture_output=True, text=True,
            cwd=project_root, timeout=5,
        )
        if result.returncode != 0:
            # Can't determine git state — don't block
            json.dump({"decision": "stop"}, sys.stdout)
            return

        latest_commit_epoch = float(result.stdout.strip())

        if latest_commit_epoch > graph_mtime:
            json.dump({
                "decision": "continue",
                "reason": (
                    "\U0001f4ca Knowledge graph is stale (newer commits exist). "
                    "Run: & .\\.venv\\Scripts\\graphify.exe . --update --code-only"
                ),
            }, sys.stdout)
        else:
            json.dump({"decision": "stop"}, sys.stdout)

    except Exception:
        # On any failure, allow the agent to stop
        json.dump({"decision": "stop"}, sys.stdout)


if __name__ == "__main__":
    main()
