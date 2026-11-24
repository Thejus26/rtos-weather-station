# s1-t2: Moving average

| Field | Value |
|-------|-------|
| Task ID | `s1-t2-moving-average` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/moving_average.[ch]`: window of 5 in a fixed struct (no heap), init/push/value API, behaviour per D-1.

## Acceptance criteria

- [ ] Compiles with `-Wall -Wextra -Werror`.
- [ ] No ESP-IDF includes.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| NFR-1 | No dynamic allocation in steady state |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-1** (referenced here): Moving-average output before 5 samples exist
  - Recommended default: Average of the samples received so far
  - Why it matters: "5-sample moving average" does not say what the first four outputs are

## Dependencies

**Depends on:** 
- [`s1-t1-decide-average-and-dewpoint`](s1-t1-decide-average-and-dewpoint.md) (Decide average and dew point)

**Blocks:** 
- [`s1-t3-moving-average-test`](s1-t3-moving-average-test.md) (Moving average test)
- [`s3-t10-process-task-filter`](../sprint-03/s3-t10-process-task-filter.md) (Process task filter)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
