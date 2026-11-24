# s8-t4: Collect test evidence

| Field | Value |
|-------|-------|
| Task ID | `s8-t4-collect-test-evidence` |
| Sprint | [Sprint 8: Documentation, Demo and Acceptance](../../sprint-08-documentation-acceptance.md) |
| Branch | `docs/deliverables` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Collect test evidence under `docs/test-results/`: host unit-test output, the fault-injection matrix, the soak log and summary, and the timing measurements.

## Acceptance criteria

- [ ] One folder holds all four evidence sets.
- [ ] Each is linked from the README.

## Requirements covered

| ID | Requirement |
|----|-------------|
| DEL-3a | Test evidence: unit tests for moving average, validation and dew point |
| DEL-3b | Test evidence: fault-injection results (sensor unplugged, Wi-Fi off, broker down, queue overflow) |
| DEL-3c | Test evidence: 24-hour soak log with stable heap and no resets |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s7-t15-final-gates-run`](../sprint-07/s7-t15-final-gates-run.md) (Final gates run)

**Blocks:** 
- [`s8-t8-acceptance-walkthrough`](s8-t8-acceptance-walkthrough.md) (Acceptance walkthrough)

## Source

Derived from [`sprint-08-documentation-acceptance.md`](../../sprint-08-documentation-acceptance.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
