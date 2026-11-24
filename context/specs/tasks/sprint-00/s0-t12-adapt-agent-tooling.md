# s0-t12: Adapt agent tooling

| Field | Value |
|-------|-------|
| Task ID | `s0-t12-adapt-agent-tooling` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Adapt or remove the inherited Python-template tooling (`.claude/` and `.agents/` rules, hooks, `/feature` actions, graphify Stop hook, which now ignores docs-only commits) so the workflow gates match `code-build.md`. Decide whether to keep graphify. Remove the precedence note in `ai-interaction.md` when done.

## Acceptance criteria

- [ ] Hooks and rules no longer contradict the C workflow.
- [ ] The Stop hook no longer fires spuriously.

## Requirements covered

None listed in the roadmap for this task.

## Dependencies

**Depends on:** none

**Blocks:** none in the roadmap

## Open questions

- keep or remove graphify? The roadmap asks for a decision but gives no default.

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
