# s6-t4: Restart after failed recoveries

| Field | Value |
|-------|-------|
| Task ID | `s6-t4-restart-after-failed-recoveries` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Count failed recoveries. After 10, log the cause and call `esp_restart()`.

## Acceptance criteria

- [ ] A permanently dead sensor ends in a restart with a logged reason.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |

## Dependencies

**Depends on:** 
- [`s6-t3-sensor-recovery`](s6-t3-sensor-recovery.md) (Sensor recovery)

**Blocks:** none in the roadmap

## Open questions

- "count failed recoveries" does not say when a recovery counts as failed (for example no successful read within one sample period after re-init). `fault_policy` from s1-t11 defines the counter, but the roadmap does not define the failure timing.

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
