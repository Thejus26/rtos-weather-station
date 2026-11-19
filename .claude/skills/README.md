# Skills

Custom skills and commands for the **01. Tool-calling assistant from scratch** workspace: a plain-Python LLM agent loop with no framework, run entirely from a project-local `.venv`.

Each skill resides in its own subfolder with a `SKILL.md` instruction file:

- `feature/` - Full lifecycle workflow: load a spec, start a feature branch, implement module by module, test (pytest, ruff, mypy), review against `rules/python-standards.md`, explain, and complete.
- `error/` - Bug and incident workflow: log an error or traceback, create a fix branch, implement the fix, and merge it.
- `research/` - Researches LLM API tool-use behavior, JSON-schema tool definitions, and Python library APIs, writing the findings into `docs/` or `context/`.
- `cleanup/` - Python housekeeping: leftover `print`/`breakpoint`, unused imports, stale TODOs, orphaned modules, bare `except`, hardcoded secrets.
- `list-components/` - Lists the agent loop, LLM client, tool registry, tools, config, CLI and tests with a one-line description each.
