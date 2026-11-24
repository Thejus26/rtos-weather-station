# s3-t3: Latest struct

| Field | Value |
|-------|-------|
| Task ID | `s3-t3-latest-struct` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

The shared `latest` struct with copy-in and copy-out accessors that take `data_mutex` with a timeout.

## Acceptance criteria

- [ ] Accessors hold the mutex only for the copy.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-5 | `data_mutex` protecting the shared `latest` struct |
| RUL-1 | Keep mutex hold times short (microseconds to a few milliseconds) |

## Dependencies

**Depends on:** 
- [`s3-t2-create-shared-objects`](s3-t2-create-shared-objects.md) (Create shared objects)

**Blocks:** 
- [`s4-t4-display-task-draw-locking`](../sprint-04/s4-t4-display-task-draw-locking.md) (Display task draw locking)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
