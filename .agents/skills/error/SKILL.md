---
name: error
description: Manage error logging, debugging, and fix lifecycle - log, fix, or complete
argument-hint: log|fix|complete
---

# Error Management Workflow

Manages the complete lifecycle of bugs, Python tracebacks, agent-loop failures (infinite loops, bad tool calls, malformed message history), API errors, and test failures: from logging and root-cause investigation to branch creation, fixing, and merging.

## Working Directory & Files

- [context/errors/](../../../context/errors/) - Folder containing individual error report records (`ERR-XXX-YYYY-MM-DD-slug.md`)
- [context/errors/README.md](../../../context/errors/README.md) - Immutable chronological ledger and index table of all logged errors

### Error Report Structure

Each error file (`ERR-XXX-YYYY-MM-DD-slug.md`) contains the following sections:

- `# Error Report: ERR-XXX - <Title>` - H1 heading with error ID and title
- `## Metadata` - Table containing Error ID, Date & Time, Commit SHA, Task, Severity, and Impacted Files
- `## 1. Description & Symptoms` - Exact traceback, failing assertion, API error body (with secrets removed), or unexpected agent behavior
- `## 2. Root Cause Analysis` - Deep-dive technical explanation of the underlying failure mechanism
- `## 3. Resolution & Code Changes` - Fix strategy, resolution steps, and code diff
- `## 4. Verification & Prevention Guidelines` - Prevention checklist, the regression test that now covers it, and safeguards

## Task

Execute the requested action: `$ARGUMENTS`

| Action | Description |
|---|---|
| `log` | Log an error, traceback, or bug into `context/errors/` and update `README.md` index |
| `fix` | Create a dedicated `fix/` git branch, analyze the error report, and implement the fix |
| `complete` | Stage and commit the fix, update error report/ledger with commit SHA, merge to base branch, and push to origin |

See [actions/](actions/) for detailed instructions for each step.

If no action is provided, explain the available options: `log`, `fix`, `complete`.
