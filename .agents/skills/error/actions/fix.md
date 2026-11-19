# Fix Action

1. **Locate Target Error Report**:
   - Check `$ARGUMENTS` (after "fix"):
     - If an Error ID or report name is provided (e.g., `ERR-001` or `ERR-002`): Load `context/errors/ERR-{NNN}-*.md`.
     - If empty: Find the latest or highest-numbered error report in `context/errors/` that has pending resolution.
   - Read the error report to understand symptoms, root cause, and impacted files.

2. **Create Fix Branch**:
   - Verify the working tree is clean for this project's files.
   - Create and checkout a dedicated branch named `fix/ERR-{NNN}-{slug}` (e.g., `fix/ERR-001-tool-result-missing-id`):
     ```bash
     git checkout -b fix/ERR-{NNN}-{slug}
     ```

3. **Reproduce First**:
   - Write or run a failing pytest that demonstrates the bug, so the fix can be proven:
     ```powershell
     .\.venv\Scripts\python.exe -m pytest -q tests/<test_file>.py -k <name>
     ```

4. **Implement the Fix**:
   - Inspect callers:
     - If the local knowledge graph is available, query the callers of the function or class being modified (`& .\.venv\Scripts\graphify.exe query "<symbol>"`) to ensure the fix does not break assumptions elsewhere.
   - Apply minimal, targeted corrections.
   - Enforce `.agents/rules/python-standards.md`:
     - Type hints, no bare `except`, errors from the `AssistantError` hierarchy
     - No `eval`/`exec`/`shell=True` on model-controlled input
     - Loop stays bounded, history stays valid, tool failures return to the model
     - `logging`, not `print`, in library code
     - No secrets in code, logs, or tests

5. **Update Error Report Document**:
   - Update `## 3. Resolution & Code Changes` in `context/errors/ERR-{NNN}-*.md`:
     - Detail the concrete resolution steps taken.
     - Include the unified diff of changes made.
   - Update `## 4. Verification & Prevention Guidelines` if additional prevention checks were identified.

6. **Verify**:
   - Run the quality gates through `.venv` (see `.agents/rules/build.md`):
     ```powershell
     .\.venv\Scripts\python.exe -m pytest -q
     .\.venv\Scripts\python.exe -m ruff check .
     .\.venv\Scripts\python.exe -m mypy src
     ```

7. **Prompt Next Step**:
   - Present a concise diff summary of the fix.
   - Advise running `/error complete` to commit the fix, update the error ledger, and push.
