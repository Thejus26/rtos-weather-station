# s7-t8: Verify watchdog

| Field | Value |
|-------|-------|
| Task ID | `s7-t8-verify-watchdog` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Watchdog: stall each monitored task for more than 10 s.

## Acceptance criteria

- [ ] The cause is logged.
- [ ] The device restarts.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-9 | Task watchdog 10 s on `sensor_task`, `process_task` and `monitor_task` |
| ERR-5 | Task hang: task watchdog logs the cause and restarts |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t11-fault-injection-hooks`](../sprint-06/s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

**Blocks:** none in the roadmap

## Open questions

- the roadmap says "stall each monitored task", which relies on the fault-injection hooks from s6-t11 but does not list a separate hook per task.

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
