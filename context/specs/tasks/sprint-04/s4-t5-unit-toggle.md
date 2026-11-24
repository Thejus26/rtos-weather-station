# s4-t5: Unit toggle

| Field | Value |
|-------|-------|
| Task ID | `s4-t5-unit-toggle` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Keep the C/F state in `display_task` and convert only for display with `c_to_f`. Published data stays in Celsius.

## Acceptance criteria

- [ ] The toggle changes the shown unit and nothing else.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-5 | Push button toggles C/F, via ISR and semaphore |

## Dependencies

**Depends on:** 
- [`s4-t4-display-task-draw-locking`](s4-t4-display-task-draw-locking.md) (Display task draw locking)
- [`s1-t8-unit-convert`](../sprint-01/s1-t8-unit-convert.md) (Unit convert)

**Blocks:** 
- [`s4-t8-measure-button-response`](s4-t8-measure-button-response.md) (Measure button response)

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
