# s6-t5: Validation faults feed policy

| Field | Value |
|-------|-------|
| Task ID | `s6-t5-validation-faults-feed-policy` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Out-of-range and jump rejections count as sensor faults and feed the same policy.

## Acceptance criteria

- [ ] Repeated bad values trigger re-init like I2C errors.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |

## Dependencies

**Depends on:** 
- [`s6-t3-sensor-recovery`](s6-t3-sensor-recovery.md) (Sensor recovery)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
