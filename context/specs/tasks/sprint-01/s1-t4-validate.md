# s1-t4: Validate

| Field | Value |
|-------|-------|
| Task ID | `s1-t4-validate` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/validate.[ch]`: result enum and a validate function. Reject temperature outside -40 to 85, humidity outside 0 to 100, a jump over 10 C from the previous accepted sample, and NaN. Accept the first sample and the exact limits.

## Acceptance criteria

- [ ] Every rejection reason has a distinct result code.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Dependencies

**Depends on:** 
- [`s1-t1-decide-average-and-dewpoint`](s1-t1-decide-average-and-dewpoint.md) (Decide average and dew point)

**Blocks:** 
- [`s1-t5-validate-test`](s1-t5-validate-test.md) (Validate test)
- [`s1-t17-app-types-header`](s1-t17-app-types-header.md) (App types header)
- [`s3-t9-process-task-validate`](../sprint-03/s3-t9-process-task-validate.md) (Process task validate)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
