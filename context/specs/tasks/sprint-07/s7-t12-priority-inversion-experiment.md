# s7-t12: Priority-inversion experiment

| Field | Value |
|-------|-------|
| Task ID | `s7-t12-priority-inversion-experiment` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Show the effect with a plain binary semaphore in place of `i2c_mutex`, then with the mutex, and record the difference.

## Acceptance criteria

- [ ] The observed difference is written up for the README Notes.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-4 | `i2c_mutex` with priority inheritance, shared by `sensor_task` and `display_task` |
| GOAL-2 | Queues, mutexes, binary semaphores and event groups, each for the problem it suits |
| DEL-5 | Reflection notes in README: priority inversion, stack sizing, what to change for STM32 |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** 
- [`s8-t6-reflection-notes`](../sprint-08/s8-t6-reflection-notes.md) (Reflection notes)

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
