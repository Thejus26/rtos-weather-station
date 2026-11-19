# Start Action

1. Read `context/current-feature.md` - verify Goals are populated.
2. If empty, error: "Run /feature load first"
3. Confirm the environment exists: `.venv\Scripts\python.exe` is present. If not, tell the user to create it (`python -m venv .venv`, then install `requirements-dev.txt`) before continuing.
4. Set Status to "In Progress" in `context/current-feature.md`.
5. Create and checkout the feature branch (derive the name from the H1 heading, e.g., `feature/calculator-tool`):
   ```bash
   git checkout -b feature/<feature-slug>
   ```
6. **Token-Frugal Implementation Rules**:
   - **Strict Slice Reading (Max 100 Lines)**: Never `Read` an entire file exceeding 100 lines. Query `& .\.venv\Scripts\graphify.exe explain "<symbol>"` to find the exact line number, then use the Read tool's `offset` and `limit` (e.g. 20–50 lines).
   - **Offload Exploratory Research to Subagents**: If researching an unfamiliar library or provider API that requires inspecting more than 3 files or pages, delegate to a subagent via the Agent tool (e.g. `Explore` or `general-purpose`). The subagent consumes tokens in its isolated sandbox and reports back a concise summary.
   - **Incremental Implementation**: List the goals, then implement them module by module according to `.claude/rules/python-standards.md`. Write the test for each piece alongside it.
