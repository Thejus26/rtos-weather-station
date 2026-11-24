# s1-t6: Dew point

| Field | Value |
|-------|-------|
| Task ID | `s1-t6-dew-point` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/dew_point.[ch]`: Magnus formula in `float`, behaviour at 0 %RH per D-2.

## Acceptance criteria

- [ ] Never returns NaN or infinity for valid input.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-3 | Calculate dew point from the filtered values |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-2** (referenced here): Dew point at 0 %RH
  - Recommended default: Clamp humidity to a small minimum (for example 1 %) inside `dew_point`, and document it
  - Why it matters: 0 %RH is valid per FR-2, but the Magnus formula takes `log(0)` and returns NaN (checked in a container run)

## Dependencies

**Depends on:** 
- [`s1-t1-decide-average-and-dewpoint`](s1-t1-decide-average-and-dewpoint.md) (Decide average and dew point)

**Blocks:** 
- [`s1-t7-dew-point-test`](s1-t7-dew-point-test.md) (Dew point test)
- [`s3-t10-process-task-filter`](../sprint-03/s3-t10-process-task-filter.md) (Process task filter)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
