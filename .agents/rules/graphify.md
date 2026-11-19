---
trigger: always_on
description: Consult the graphify knowledge graph at graphify-out/ for codebase and architecture questions.
---

## graphify & build policy

This project has a graphify knowledge graph at graphify-out/.

Rules:
- **STRICT REQUIREMENT**: graphify must ONLY and EXCLUSIVELY be run using the local virtual environment `.venv` (`.\.venv\Scripts\graphify.exe` or `.\.venv\Scripts\python.exe -m graphify`). Never use global python, pipx, uv, or system-wide graphify commands.
- For codebase or architecture questions, when `graphify-out/graph.json` exists, first run `& .\.venv\Scripts\graphify.exe query "<question>"` (CLI) or `query_graph` (MCP). Use `& .\.venv\Scripts\graphify.exe path "<A>" "<B>"` / `shortest_path` for relationships and `& .\.venv\Scripts\graphify.exe explain "<concept>"` / `get_node` for focused concepts.
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- **Environment Policy**: All Python, including graphify, runs through the local `.venv`. Never use the global interpreter, `pip`, `pipx`, or `uv`. Follow `.agents/rules/build.md` exclusively.
