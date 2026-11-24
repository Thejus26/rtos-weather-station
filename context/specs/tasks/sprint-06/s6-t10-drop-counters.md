# s6-t10: Drop counters

| Field | Value |
|-------|-------|
| Task ID | `s6-t10-drop-counters` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Surface queue-full and drop counters (for `raw_queue` and `publish_queue`) in the housekeeping log.

## Acceptance criteria

- [ ] Counts appear.
- [ ] Counts increase when a queue is overfilled.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-4 | Queue full: drop oldest, count the drop, log it |

## Dependencies

**Depends on:** 
- [`s6-t2-error-dispatch`](s6-t2-error-dispatch.md) (Error dispatch)
- [`s3-t11-process-task-publish-queue`](../sprint-03/s3-t11-process-task-publish-queue.md) (Process task publish queue)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
