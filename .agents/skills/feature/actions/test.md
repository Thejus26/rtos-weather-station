# Test Action

Per `.agents/rules/build.md`, all Python runs through the project's `.venv`. Never call the global `python`, `pip`, or `pytest`.

1. Read `context/current-feature.md` to understand what was implemented.
2. **Fast Static Feedback (Token-Frugal Checking)**:
   - Before manually tracing signatures across files, run:
     ```powershell
     .\.venv\Scripts\python.exe -m mypy src
     .\.venv\Scripts\python.exe -m ruff check .
     ```
   - These report exact line numbers for type mismatches, missing imports, and unused code in a few lines of output.
3. Identify the loop logic, tools, schemas, config, or error paths added or modified.
4. Ensure new or modified logic is covered, using the fake LLM client (never a real API):
   - Happy path: direct answer, one tool call, several tool calls in sequence.
   - Failure and edge cases: tool raises, unknown tool name, malformed or schema-invalid arguments, API error or timeout, empty model response, `MAX_ITERATIONS` reached.
   - Message-history assertions: every tool request has a matching result, in order.
5. **Run Verification**:
   ```powershell
   .\.venv\Scripts\python.exe -m pytest -q
   .\.venv\Scripts\python.exe -m pytest -q tests/<test_file>.py -k <name>
   .\.venv\Scripts\python.exe -m ruff format --check .
   ```
6. Report test results and quality-gate status (pytest, ruff check, ruff format, mypy).
