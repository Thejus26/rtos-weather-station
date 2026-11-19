---
name: feature
description: Manage current feature workflow - load, start, test, review, explain, or complete
argument-hint: load|start|test|review|explain|complete
disable-model-invocation: true
---

# Feature Workflow

Manages the complete lifecycle of a feature (agent loop, LLM client, tool, tool registry, CLI) from specification to merge.

## Working File

[context/current-feature.md](../../../context/current-feature.md)

### File Structure

`current-feature.md` contains the following sections:

- `# Current Feature` - H1 heading with feature name when active
- `## Status` - `Not Started` | `In Progress` | `Complete`
- `## Goals` - Measurable criteria and deliverables for the feature
- `## Notes` - Design constraints, module boundaries, API behavior, or tool-schema requirements
- `## History` - Completed features list (append only)

## Task

Execute the requested action: `$ARGUMENTS`

| Action | Description |
|---|---|
| `load` | Load a feature spec from `context/specs/` or an inline description |
| `start` | Begin implementation, create git feature branch |
| `test` | Run pytest, ruff, and mypy through `.venv` |
| `review` | Verify all goals are met against `.claude/rules/python-standards.md` |
| `explain` | Document the change and the agent-loop data flow |
| `complete` | Stage, commit, merge to main/master, and reset `current-feature.md` |

## Token-Frugal & Graphify-First Operational Mandate

To preserve model context, prevent latency degradation, and avoid reading large files repeatedly:
1. **Graphify Before Reading**: Never open raw source files to discover signatures, callers, or dependencies. Always run `& .\.venv\Scripts\graphify.exe query "<concept>"`, `explain "<symbol>"`, or `path "<A>" "<B>"` first.
2. **Strict Slice Reading**: Never view full files exceeding 100 lines. Always use the Read tool's `offset` and `limit` to read only the targeted function or block.
3. **Tools-First Feedback**: Run `.\.venv\Scripts\python.exe -m mypy src` and `-m ruff check .` to catch type and import errors in a few lines of output, rather than cross-referencing multiple files.
4. **Subagent Offloading**: Delegate broad exploratory research (`research`) and deep code audits (`code-scanner`) to isolated subagents to keep context clean.

All Python runs through `.venv` (see `.claude/rules/build.md`).

See [actions/](actions/) for detailed instructions for each step.

If no action is provided, explain the available options.
