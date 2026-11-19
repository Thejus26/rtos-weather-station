"""
Graphify Staleness Check — Stop hook.

Compares graphify-out/graph.json modification time against the latest git
commit timestamp.  If the graph is stale, blocks the stop once and asks the
agent to run a graphify update before finishing.

Stdin:  Stop JSON payload  (stop_hook_active, etc.)
Stdout: {"decision": "block", "reason": "..."} or nothing to allow the stop.
"""
import json
import os
import subprocess
import sys

UPDATE_CMD = "& .\\.venv\\Scripts\\graphify.exe . --update --code-only"


def _resolve_project_root() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", ".."))


def _block(reason: str) -> None:
    json.dump({"decision": "block", "reason": reason}, sys.stdout)


def main() -> None:
    try:
        data = json.load(sys.stdin)

        # Already continuing because of this hook — never loop
        if data.get("stop_hook_active"):
            return

        project_root = _resolve_project_root()
        graph_path = os.path.join(project_root, "graphify-out", "graph.json")

        if not os.path.isfile(graph_path):
            _block(f"graphify-out/graph.json not found. Run: {UPDATE_CMD}")
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
            return

        latest_commit_epoch = float(result.stdout.strip())

        if latest_commit_epoch > graph_mtime:
            _block(f"Knowledge graph is stale (newer commits exist). Run: {UPDATE_CMD}")

    except Exception:
        # On any failure, allow the agent to stop
        pass


if __name__ == "__main__":
    main()
