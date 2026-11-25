---
name: graphify
description: Refresh the optional knowledge graph of the C source (graphify, run from the project .venv)
---

# Workflow: graphify

Run graphify using the project's local virtual environment only (never global python, pipx, or uv; see `.agents/rules/graphify.md`):

```powershell
& .\.venv\Scripts\graphify.exe <path> --update --code-only
```

If no path argument is given, use `.` (current directory).
