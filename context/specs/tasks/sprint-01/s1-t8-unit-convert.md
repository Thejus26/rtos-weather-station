# s1-t8: Unit convert

| Field | Value |
|-------|-------|
| Task ID | `s1-t8-unit-convert` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/unit_convert.[ch]` with Celsius to Fahrenheit, and `test_unit_convert.c` (freezing, boiling, negative values).

## Acceptance criteria

- [ ] Assertions pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-5 | Push button toggles C/F, via ISR and semaphore |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s0-t4-harness-smoke-test`](../sprint-00/s0-t4-harness-smoke-test.md) (Harness smoke test)

**Blocks:** 
- [`s4-t5-unit-toggle`](../sprint-04/s4-t5-unit-toggle.md) (Unit toggle)

## Open questions

- the task combines the module and its test in one row, but there is no separate "unit-convert-test" task ID. Treat both as one deliverable.

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
