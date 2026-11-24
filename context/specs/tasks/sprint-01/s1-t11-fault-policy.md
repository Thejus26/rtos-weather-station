# s1-t11: Fault policy

| Field | Value |
|-------|-------|
| Task ID | `s1-t11-fault-policy` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/fault_policy.[ch]`: count consecutive sensor failures (re-init request at 3), count failed recoveries (restart request at 10), reset counters on success.

## Acceptance criteria

- [ ] The state machine is a plain struct with no timers or RTOS calls.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Dependencies

**Depends on:** 
- [`s0-t4-harness-smoke-test`](../sprint-00/s0-t4-harness-smoke-test.md) (Harness smoke test)

**Blocks:** 
- [`s1-t12-fault-policy-test`](s1-t12-fault-policy-test.md) (Fault policy test)
- [`s6-t3-sensor-recovery`](../sprint-06/s6-t3-sensor-recovery.md) (Sensor recovery)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
