# s5-t10: Outage buffering

| Field | Value |
|-------|-------|
| Task ID | `s5-t10-outage-buffering` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-16. During an outage `comms_task` stops consuming, `process_task` drops oldest when the queue is full, and on reconnect the backlog is sent oldest first at a bounded rate.

## Acceptance criteria

- [ ] After a long outage there is no crash and no unbounded burst.
- [ ] The drop count is logged.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-3 | Wi-Fi/MQTT loss: keep sampling and displaying, buffer, reconnect with backoff |
| ERR-4 | Queue full: drop oldest, count the drop, log it |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-16** (settled in this task): Behaviour on reconnect with buffered readings
  - Recommended default: Send oldest first, one per publish tick or rate-limited, never in an unbounded burst
  - Why it matters: Keeps the 30 s cadence meaningful and protects `comms_task` stack

## Dependencies

**Depends on:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

**Blocks:** 
- [`s5-t12-network-outage-test`](s5-t12-network-outage-test.md) (Network outage test)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
