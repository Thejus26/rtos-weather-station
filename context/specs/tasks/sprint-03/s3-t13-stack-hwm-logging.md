# s3-t13: Stack high-water-mark logging

| Field | Value |
|-------|-------|
| Task ID | `s3-t13-stack-hwm-logging` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Log each task's stack high-water mark every 10 s so measurement starts early.

## Acceptance criteria

- [ ] The log shows a number for each of the five tasks.

## Requirements covered

| ID | Requirement |
|----|-------------|
| NFR-2 | Every task has a measured stack high-water mark with at least 25% headroom |

## Dependencies

**Depends on:** 
- [`s3-t12-monitor-task-stub`](s3-t12-monitor-task-stub.md) (Monitor task stub)

**Blocks:** none in the roadmap

## Open questions

- the 10 s stack logging period matches the `monitor_task` housekeeping period, but the stub in s3-t12 has no housekeeping yet. The roadmap does not say which task does the logging.

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
