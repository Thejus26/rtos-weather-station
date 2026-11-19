---
name: error
description: Manage error logging, debugging, and fix lifecycle - log, fix, or complete
argument-hint: log|fix|complete
---

## Context

Error records and incident logs are managed in:
- [context/errors/](../../../context/errors/)
- [context/errors/README.md](../../../context/errors/README.md)

## File Structure

Individual error reports follow `ERR-XXX-YYYY-MM-DD-slug.md` with sections:
- `# Error Report: ERR-XXX - <Title>`
- `## Metadata` (Error ID, Date & Time, Commit SHA, Task, Severity, Impacted Files)
- `## 1. Description & Symptoms`
- `## 2. Root Cause Analysis`
- `## 3. Resolution & Code Changes`
- `## 4. Verification & Prevention Guidelines`

The index ledger (`context/errors/README.md`) maintains:
- `## Chronological Index of Errors` - Append-only Markdown table tracking ID, Date/Time, Commit, Module, Title/Summary, and Report Link
- `## Error Classification by Category` - Mermaid pie chart tracking distribution

## Task

Execute the requested action: `$ARGUMENTS`

---

### If action is "log":

1. Check `$ARGUMENTS` (after "log") or infer from the latest pytest output, traceback, or user input. Remove secrets first.
2. Read `context/errors/README.md` to find the latest error ID and increment it (e.g. `ERR-005` -> `ERR-006`).
3. Create `context/errors/ERR-{NNN}-{YYYY-MM-DD}-{slug}.md` using the current timestamp and standard report layout.
4. Append an entry row to the `## Chronological Index of Errors` table in `context/errors/README.md`.
5. Update the category count in the `## Error Classification by Category` pie chart if applicable.
6. Display confirmation and suggest running `/error fix ERR-{NNN}`.

---

### If action is "fix":

1. Locate the target error report in `context/errors/` from `$ARGUMENTS` or select the latest unresolved error.
2. Review symptoms, root cause, and impacted files.
3. Create and checkout a dedicated fix branch: `fix/ERR-{NNN}-{slug}`.
4. Reproduce with a failing pytest, then implement minimal, targeted changes following `.claude/rules/python-standards.md`.
5. Update `## 3. Resolution & Code Changes` in the error report with explanation and unified diff.
6. Verify through `.venv`: `.\.venv\Scripts\python.exe -m pytest -q`, `-m ruff check .`, `-m mypy src`.
7. Present a diff summary and suggest running `/error complete`.

---

### If action is "complete":

1. Stage the code changes and the error report by explicit path (`git add <paths>`).
2. Commit with a conventional format: `fix(<module>): resolve ERR-{NNN} <summary>`.
3. Retrieve the commit SHA and update `context/errors/ERR-{NNN}-*.md` and `context/errors/README.md`.
4. Amend the commit to include ledger updates: `git commit --amend --no-edit`.
5. Checkout the base branch (`main`), merge the fix branch, and push to origin if a remote exists.
6. Delete the local fix branch (`git branch -d fix/ERR-{NNN}-{slug}`).
7. Output a completion summary.

---

If no action provided, explain the available options: `log`, `fix`, `complete`.
