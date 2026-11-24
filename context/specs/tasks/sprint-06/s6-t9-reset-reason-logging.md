# s6-t9: Reset reason logging

| Field | Value |
|-------|-------|
| Task ID | `s6-t9-reset-reason-logging` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Log the reset reason and a boot counter at start-up, so watchdog and brown-out restarts are visible in logs.

## Acceptance criteria

- [ ] The reset reason is shown on every boot.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-5 | Task hang: task watchdog logs the cause and restarts |
| NFR-3 | 24-hour continuous run without reset or heap growth |

## Dependencies

**Depends on:** 
- [`s6-t7-task-watchdog`](s6-t7-task-watchdog.md) (Task watchdog)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
