---
name: cleanup
description: Clean up Python codebase housekeeping tasks (add "run" to execute fixes)
argument-hint: run|check
---

Review the codebase and project context for cleanup tasks:

1. **Feature Tracker Order**: Verify that the history in `context/current-feature.md` is strictly in chronological order (oldest to newest).
2. **Debug Output**: Find leftover `print(...)`, `breakpoint()`, `pdb`, or `import pdb` in library code. Only `cli.py` may print. Use `logging` elsewhere.
3. **Unused Imports & Dead Code**: Detect unused imports, variables, and unreferenced functions or classes (`.\.venv\Scripts\python.exe -m ruff check . --select F`).
4. **Stale TODOs**: Identify unresolved `TODO`, `FIXME`, or `HACK` comments.
5. **Orphaned Modules & Files**: Find `.py` files that nothing imports or runs, missing `__init__.py` in packages, and stray scratch scripts.
6. **Context Alignment**: Verify that `context/` documents (`project-overview.md`, `project-structure.md`, `coding-standards.md`, `code-build.md`) match the real Python layout and tooling, and flag any that still describe another language or stack.
7. **Error Handling Audit**: Identify bare `except:`, `except Exception: pass`, raw `Exception` raised instead of `AssistantError` subclasses, and network calls without a timeout.
8. **Unsafe Code & Secrets Audit**: Find `eval`, `exec`, `os.system`, `shell=True`, `pickle.loads`, `yaml.load` without `# unsafe-ok`, hardcoded API keys, and a missing `.env` entry in `.gitignore` or missing `.env.example`.
9. **Typing & Docstrings**: List public functions without type hints or docstrings (`python -m mypy src` via `.venv` for hints).
10. **Dependencies**: Compare imports against `requirements.txt` and `requirements-dev.txt` for unused or unpinned packages.

**Mode: $ARGUMENTS**

If no argument or argument is "check":
- Only report findings with line numbers and file paths; do not modify any files.
- Categorize what WOULD be cleaned up.

If the argument is "run" or "fix":
- First, report all findings in a numbered list.
- Then ask: "Which items would you like me to fix? (enter numbers like 1,3,5 or 'all' or 'none')"
- Wait for user response before making any changes.
- Only modify the specific items requested by the user.
- Summarize all completed fixes clearly.
