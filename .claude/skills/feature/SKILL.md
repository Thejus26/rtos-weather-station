---
name: feature
description: Manage current feature workflow - load, start, test, review, explain, or complete
argument-hint: load|start|test|review|explain|complete
disable-model-invocation: true
---

# Feature Workflow

Manages the complete lifecycle of a feature (a roadmap task: app_logic module, firmware task, driver, build or tooling change) from specification to merge.

## Working File

[context/current-feature.md](../../../context/current-feature.md)

### File Structure

`current-feature.md` contains the following sections:

- `# Current Feature` - H1 heading with feature name when active
- `## Status` - `Not Started` | `In Progress` | `Complete`
- `## Goals` - Measurable criteria and deliverables for the feature
- `## Notes` - Design constraints, module boundaries, task and queue interfaces, config values, or hardware limits
- `## History` - Completed features list (append only)

## Task

Execute the requested action: `$ARGUMENTS`

| Action | Description |
|---|---|
| `load` | Load a feature spec from `context/specs/` or an inline description |
| `start` | Begin implementation, create git feature branch |
| `test` | Run the host unit tests and the firmware build, as the change requires |
| `review` | Verify all goals are met against `.claude/rules/c-standards.md` and the quality gates |
| `explain` | Document the change and the data flow between tasks, queues and app_logic |
| `complete` | Stage, commit, merge to main/master, and reset `current-feature.md` |

## Token-Frugal Operational Mandate

To preserve model context and avoid reading large files repeatedly:
1. **Slice Reading**: Never view full files exceeding 100 lines. Find the line with `Grep`, then use the Read tool's `offset` and `limit` to read only the targeted function or block.
2. **Graph First (optional)**: If `graphify-out/graph.json` exists, `& .\.venv\Scripts\graphify.exe query "<concept>"`, `explain "<symbol>"` or `path "<A>" "<B>"` can find callers and signatures faster than opening files (see `.claude/rules/graphify.md`). Skip it when there is no graph.
3. **Tools-First Feedback**: Run the host tests (`-Wall -Wextra -Werror`) and the firmware build to catch errors in a few lines of output, rather than cross-referencing files by eye.
4. **Subagent Offloading**: Delegate broad exploratory research (`research`) and deep code audits (`code-scanner`) to isolated subagents to keep context clean.

Build and verification policy: `.claude/rules/build.md`. Host tests and a container build never verify hardware behaviour, and `[HW]` tasks stay deferred while there is no board.

See [actions/](actions/) for detailed instructions for each step.

If no action is provided, explain the available options.
