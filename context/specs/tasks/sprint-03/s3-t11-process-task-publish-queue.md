# s3-t11: Process task publish queue

| Field | Value |
|-------|-------|
| Task ID | `s3-t11-process-task-publish-queue` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`process_task` enqueues a `reading_t` to `publish_queue` every 30 s. When the queue is full it drops the oldest entry and counts the drop.

## Acceptance criteria

- [ ] A drop counter increments when the queue is deliberately filled.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| OBJ-2 | `publish_queue`: 10 x `reading_t`, `process_task` to `comms_task`, drop oldest when full |
| ERR-4 | Queue full: drop oldest, count the drop, log it |
| TIM-5 | MQTT publish every 30 s, tolerance +/-1 s when connected |

## Dependencies

**Depends on:** 
- [`s3-t10-process-task-filter`](s3-t10-process-task-filter.md) (Process task filter)

**Blocks:** 
- [`s6-t10-drop-counters`](../sprint-06/s6-t10-drop-counters.md) (Drop counters)

## Open questions

- the roadmap says to enqueue "every 30 s" but does not say whether the 30 s reading is the latest filtered value or an average over the period. The roadmap gives no rule.

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
