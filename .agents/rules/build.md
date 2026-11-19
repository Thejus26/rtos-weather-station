---
trigger: always_on
description: Mandatory Python virtual-environment (.venv-only) policy and standard verification commands.
---

## Python Environment & Verification Policy

This project runs all Python through its own virtual environment at `.venv/`. The global interpreter is only used once, to create that environment.

### Rules

1. **VENV ONLY**:
   - Never run `python`, `pip`, `pytest`, `ruff`, `mypy`, `pipx`, `conda`, `poetry` or `uv` from the global install.
   - The one exception is creating the environment: `python -m venv .venv`.
   - Everything else goes through `.\.venv\Scripts\python.exe -m <tool>`.

2. **STANDARD COMMANDS** (PowerShell, from the project root):

   | Purpose | Command |
   |---|---|
   | Create environment (once) | `python -m venv .venv` |
   | Install runtime deps | `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` |
   | Install dev deps | `.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt` |
   | Run the app | `.\.venv\Scripts\python.exe -m <package>` (or `.\.venv\Scripts\python.exe src\<file>.py`) |
   | Run tests | `.\.venv\Scripts\python.exe -m pytest -q` |
   | Lint | `.\.venv\Scripts\python.exe -m ruff check .` |
   | Format check | `.\.venv\Scripts\python.exe -m ruff format --check .` |
   | Type check | `.\.venv\Scripts\python.exe -m mypy src` |

3. **DEPENDENCIES**:
   - Runtime packages go in `requirements.txt`. Test, lint and type-check tools go in `requirements-dev.txt`. Pin versions.
   - Add a package only when the current feature needs it. Agent frameworks (LangGraph, CrewAI, etc.) are out of scope for this project.

4. **SECRETS**:
   - API keys live in `.env` (loaded with `python-dotenv`), never in source, logs, tests or commits.
   - Commit a `.env.example` with placeholder values. Keep `.env` in `.gitignore`.

5. **TESTS NEVER CALL A REAL LLM**:
   - Use a fake or mocked LLM client so the suite is offline, free and deterministic.
   - An optional live smoke test must be marked `@pytest.mark.live` and skipped by default.

6. **GIT SCOPE**:
   - The enclosing git repository may be rooted above this folder. Always `git add` explicit paths inside this project, never `git add .` or `-A` from a parent directory.
   - Never stage `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/` or `graphify-out/`.

7. **HOOKS**:
   - Hook scripts in `.agents/hooks/` use only the standard library, so they run on any Python 3.10+ interpreter and do not need `.venv`.
   - `guard-python-env.py` enforces rule 1 and denies the offending command with a message.
