"""
Graphify Staleness Check — Stop hook (graphify is optional dev tooling).

Blocks the stop once, asking the agent to refresh the knowledge graph, but only when
the graph is genuinely out of date:

  * a commit newer than the graph touched C/C++ source (.c .h .cpp .hpp), or
  * the graph is missing, graphify is installed in .venv, and C source exists.

It stays silent for docs-only commits, hook/config/JSON edits, a project without C
source yet, and a machine where graphify is not installed. The graph's age is the
newest file in graphify-out/ (not just graph.json), so an update that rewrites nothing
else still counts as fresh.

Stdin:  Stop JSON payload  (stop_hook_active, etc.)
Stdout: {"decision": "block", "reason": "..."} or nothing to allow the stop.
"""
import json
import os
import subprocess
import sys

UPDATE_CMD = "& ./.venv/Scripts/graphify.exe . --update --code-only"
C_EXTENSIONS = {".c", ".h", ".cpp", ".hpp"}
SOURCE_DIRS = ("main", "components")


def _resolve_project_root() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", ".."))


def _block(reason: str) -> None:
    json.dump({"decision": "block", "reason": reason}, sys.stdout)


def _has_c_source(project_root: str) -> bool:
    for top in SOURCE_DIRS:
        for _dirpath, _dirs, files in os.walk(os.path.join(project_root, top)):
            if any(os.path.splitext(f)[1].lower() in C_EXTENSIONS for f in files):
                return True
    return False


def _graph_mtime(graph_dir: str) -> float:
    """Newest modification time among the files directly inside graphify-out/."""
    times = [os.path.getmtime(e.path) for e in os.scandir(graph_dir) if e.is_file()]
    return max(times) if times else 0.0


def _c_changed_since(project_root: str, graph_mtime: float) -> bool:
    """True if any commit newer than the graph touched a C/C++ source file."""
    result = subprocess.run(
        ["git", "-c", "core.quotepath=false", "log", "--no-merges",
         "--format=@@%ct", "--name-only", "-n", "500"],
        capture_output=True, text=True, cwd=project_root, timeout=5,
    )
    if result.returncode != 0:
        return False  # can't tell: don't block
    newer = False
    for line in result.stdout.splitlines():
        if line.startswith("@@"):
            newer = float(line[2:]) > graph_mtime
        elif newer and os.path.splitext(line)[1].lower() in C_EXTENSIONS:
            return True
    return False


def main() -> None:
    try:
        data = json.load(sys.stdin)

        # Already continuing because of this hook: never loop
        if data.get("stop_hook_active"):
            return

        project_root = _resolve_project_root()
        graph_dir = os.path.join(project_root, "graphify-out")
        graphify_exe = os.path.join(project_root, ".venv", "Scripts", "graphify.exe")

        # Optional tooling: nothing to do where it is not installed or nothing to graph
        if not os.path.isfile(graphify_exe) or not _has_c_source(project_root):
            return

        if not os.path.isfile(os.path.join(graph_dir, "graph.json")):
            _block(f"graphify-out/graph.json not found. Run: {UPDATE_CMD}")
            return

        if _c_changed_since(project_root, _graph_mtime(graph_dir)):
            _block(f"Knowledge graph is stale (newer commits changed C source). Run: {UPDATE_CMD}")

    except Exception:
        # On any failure, allow the agent to stop
        pass


if __name__ == "__main__":
    main()
