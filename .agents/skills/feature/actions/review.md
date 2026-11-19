# Review Action

1. Read `context/current-feature.md` to understand the target deliverables and constraints.
2. Review the code diff summary on the feature branch (`git diff main --stat`, or `master` if that is the base).
3. **Subagent Delegation for Deep Code Audit (Token Preservation)**:
   - Offload line-by-line auditing to the specialized `code-scanner` subagent (`.agents/agents/code-scanner/agent.md`).
   - The subagent runs in an isolated context window, so the code analysis does not pollute the primary conversation.
   - The subagent audits against `.agents/rules/python-standards.md`:
     - 🔁 Agent-loop correctness (bounded loop, valid message history, stop condition)
     - 🛡️ Tool safety (no `eval`/`exec`/shell on model-controlled input, validated arguments)
     - ⚠️ Error handling (`AssistantError` hierarchy, no bare `except`, tool failures returned to the model)
     - 🔑 Secrets (none in code or logs, `.env` ignored, `.env.example` present)
     - 🔍 Logging (`logging` module, no `print` outside `cli.py`)
     - 🧪 Tests (fake LLM, failure paths covered, offline)
     - 🚫 Scope creep (agent frameworks, memory, planning, extra dependencies)
   - The primary agent receives only the synthesized, actionable findings report.
4. Verify the automated quality gates pass through `.venv`:
   - Tests: `.\.venv\Scripts\python.exe -m pytest -q`
   - Linter: `.\.venv\Scripts\python.exe -m ruff check .`
   - Formatter: `.\.venv\Scripts\python.exe -m ruff format --check .`
   - Types: `.\.venv\Scripts\python.exe -m mypy src`
5. Final verdict: **Ready to complete** or **Action items required**.