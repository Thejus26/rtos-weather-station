# s3-t10: Process task filter

| Field | Value |
|-------|-------|
| Task ID | `s3-t10-process-task-filter` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`process_task` applies the moving average and dew point to accepted samples and writes `latest` under `data_mutex`.

## Acceptance criteria

- [ ] `latest` holds filtered values and a dew point.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| FR-3 | Calculate dew point from the filtered values |
| OBJ-5 | `data_mutex` protecting the shared `latest` struct |

## Dependencies

**Depends on:** 
- [`s3-t9-process-task-validate`](s3-t9-process-task-validate.md) (Process task validate)
- [`s1-t2-moving-average`](../sprint-01/s1-t2-moving-average.md) (Moving average)
- [`s1-t6-dew-point`](../sprint-01/s1-t6-dew-point.md) (Dew point)

**Blocks:** 
- [`s3-t11-process-task-publish-queue`](s3-t11-process-task-publish-queue.md) (Process task publish queue)
- [`s3-t14-sample-logging`](s3-t14-sample-logging.md) (Sample logging)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
