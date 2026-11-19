---
description: Turn any folder of files into a navigable knowledge graph
argument-hint: [path]
---

# Workflow: graphify

Run the full graphify pipeline using the project's local virtual environment only (never global python, pipx, or uv; see `.claude/rules/graphify.md`):

```powershell
& .\.venv\Scripts\graphify.exe <path> --update --code-only
```

Substitute `<path>` with `$ARGUMENTS`; if no path argument is given, use `.` (current directory).
