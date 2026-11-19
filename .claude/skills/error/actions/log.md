# Log Action

1. **Parse Arguments & Error Details**:
   - Check `$ARGUMENTS` (after "log"):
     - If inline text provided: Extract error title, impacted files, module, severity, and description.
     - If empty: Infer details from the latest pytest output, traceback, or failure log, or prompt the user for details.
   - **Blast Radius & Impact Analysis (Local Knowledge Graph)**:
     - If `graphify-out/graph.json` is available, query the failing function or class (`& .\.venv\Scripts\graphify.exe query "<failing_symbol>"`) to discover its callers and dependencies.
     - Include the dependent modules and callers in the impacted files list.
   - Remove API keys, tokens, and personal data from any pasted output before recording it.

2. **Determine Next Error ID**:
   - Read `context/errors/README.md` and inspect the `context/errors/` directory.
   - Find the highest existing error number (e.g., `ERR-005`) and increment by 1 to get `ERR-{NNN}` (e.g., `ERR-006`).

3. **Generate Error Report File**:
   - Create `context/errors/ERR-{NNN}-{YYYY-MM-DD}-{slug}.md` using today's date and a kebab-case slug of the title.
   - Populate standard sections:
     - `# Error Report: ERR-{NNN} - <Title>`
     - `## Metadata` (Error ID, Date & Time with timezone, current commit SHA, Task, Severity, Impacted Files)
     - `## 1. Description & Symptoms` (exact traceback, failing assertion, API error, or unexpected agent behavior)
     - `## 2. Root Cause Analysis` (explanation of why the issue occurred)
     - `## 3. Resolution & Code Changes` (proposed fix strategy or initial diff; marked *Pending Implementation* if unfixed)
     - `## 4. Verification & Prevention Guidelines` (prevention rules, the pytest command that reproduces and then guards the fix)

4. **Update Ledger Index**:
   - Open `context/errors/README.md`. Create it with the two sections below if it does not exist.
   - Append a new row to the `## Chronological Index of Errors` table:
     ```markdown
     | **`ERR-{NNN}`** | YYYY-MM-DD HH:MM:SS | `<short-sha>` | <Module> | **<Title>**: <Summary>. | [ERR-{NNN} Report](ERR-{NNN}-{YYYY-MM-DD}-{slug}.md) |
     ```
     If `git remote get-url origin` returns a URL, make the SHA a link: `[`<short-sha>`](<repo-url>/commit/<full-sha>)`.
   - Increment the relevant category count in the `## Error Classification by Category` Mermaid pie chart.

5. **Confirm and Guide**:
   - Output confirmation showing the generated Error ID, report file link, and prompt:
     `"Error logged as ERR-{NNN}. Run /error fix ERR-{NNN} to begin fixing."`
