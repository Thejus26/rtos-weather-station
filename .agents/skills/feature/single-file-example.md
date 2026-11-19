---
name: feature
description: Manage current feature workflow - load, start, review, explain, or complete
argument-hint: load|start|review|explain|complete
---

## Context

Read the current feature from:
[context/current-feature.md](../../../context/current-feature.md)

## File Structure

`current-feature.md` has these sections:

- `# Current Feature` - H1 heading with feature name when active
- `## Status` - `Not Started` | `In Progress` | `Complete`
- `## Goals` - Bullet points of what success looks like
- `## Notes` - Design constraints, module boundaries, API behavior, or tool-schema requirements
- `## History` - Completed features (append only)

## Task

Execute the requested action: `$ARGUMENTS`

---

### If action is "load":

1. Check `$ARGUMENTS` (after "load"):
   - If it looks like a filename (single word, no spaces): Look for `context/specs/{name}.md`
   - If it's multiple words: Use as inline feature description, generate goals
   - If empty: Error - "load" requires a spec filename or feature description
2. Update `context/current-feature.md`:
   - Update H1 heading to include the feature name (e.g., `# Current Feature: Calculator Tool`)
   - Write goals as bullet points under `## Goals`
   - Write any additional notes/context under `## Notes`
   - Set Status to `Not Started`
3. Confirm spec loaded and show the feature summary

---

### If action is "start":

1. Read `context/current-feature.md` - verify Goals are populated
2. If empty, error: "Run /feature load first"
3. Set Status to `In Progress`
4. Create and checkout the feature branch (derive name from H1 heading, e.g., `feature/calculator-tool`)
5. List the goals, then implement them module by module according to `.agents/rules/python-standards.md`

---

### If action is "review":

1. Read `context/current-feature.md` to understand the goals
2. Review all code changes made for this feature
3. Check for:
   - ✅ Goals met
   - ❌ Goals missing or incomplete
   - 🔁 Bounded loop, valid message history, clear stop condition
   - 🛡️ No `eval`/`exec`/shell on model-controlled input; validated tool arguments
   - ⚠️ `AssistantError` hierarchy, no bare `except`, tool failures returned to the model
   - 🔍 `logging` instead of `print` outside `cli.py`
   - 🚫 Scope creep (code beyond goals, agent frameworks)
4. Final verdict: Ready to complete or needs changes

---

### If action is "explain":

1. Read `context/current-feature.md` to understand what was implemented
2. Run `git diff main --name-only` to get the list of files changed
3. For each file created or modified:
   - Show the file path (`src/...`)
   - Give a 1-2 sentence explanation of what it does / what changed
   - Highlight any key functions, classes, or schemas
4. End with a brief summary of how the pieces fit into the agent loop

---

### If action is "complete":

1. Run verification through `.venv`: `.\.venv\Scripts\python.exe -m pytest -q` and `.\.venv\Scripts\python.exe -m ruff check .`
2. Stage the relevant files by explicit path (`git add <paths>`)
3. Commit with a conventional commit message based on the feature
4. Merge into `main`
5. Switch back to the `main` branch
6. Reset `context/current-feature.md`:
   - Change H1 back to `# Current Feature`
   - Clear Goals and Notes sections
   - Set Status to `Not Started`
7. Add the feature summary to the END of History

---

If no action provided, explain the available options: `load`, `start`, `review`, `explain`, `complete`
