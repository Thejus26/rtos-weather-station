## graphify (optional knowledge graph)

graphify is optional dev tooling (`context/code-build.md` section 9). The graph lives in `graphify-out/` (git-ignored). It is only useful once `main/` and `components/` contain C code.

- Run graphify only from the project `.venv`: `& .\.venv\Scripts\graphify.exe ...`. Never use global python, pipx, uv or a system-wide graphify. Do not run `graphify install`.
- If `graphify-out/graph.json` exists, use it for codebase questions before reading many files: `graphify.exe query "<question>"`, `path "<A>" "<B>"`, `explain "<concept>"`.
- If `graphify-out/wiki/index.md` exists, navigate it instead of raw files. Read `graphify-out/GRAPH_REPORT.md` only for a broad architecture review.
- Refresh after C source changes: `& .\.venv\Scripts\graphify.exe . --update --code-only` (tree-sitter only, no network). Set `GRAPHIFY_NO_AUTO_REFRESH=1` to stop it refreshing global skill folders.
- The graph does not replace the spec. `context/project-overview.md` stays the source of truth, and the graph can be stale or empty. If it disagrees with the code, trust the code.
