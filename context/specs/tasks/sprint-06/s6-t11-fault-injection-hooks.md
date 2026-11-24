# s6-t11: Fault-injection hooks

| Field | Value |
|-------|-------|
| Task ID | `s6-t11-fault-injection-hooks` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Fault-injection hooks behind a Kconfig flag that is off by default: force N consecutive sensor errors, inject out-of-range values, hold `i2c_mutex`, stall a task, leak heap, force Wi-Fi and MQTT disconnects, and fill `publish_queue`.

## Acceptance criteria

- [ ] Each injection can be switched on from `menuconfig`.
- [ ] The default build contains none of them.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| ERR-3 | Wi-Fi/MQTT loss: keep sampling and displaying, buffer, reconnect with backoff |
| ERR-4 | Queue full: drop oldest, count the drop, log it |
| ERR-5 | Task hang: task watchdog logs the cause and restarts |
| ERR-6 | Low heap (for example below 20 KB): log a warning, restart if it keeps falling |
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |

## Dependencies

**Depends on:** 
- [`s6-t7-task-watchdog`](s6-t7-task-watchdog.md) (Task watchdog)
- [`s6-t8-heap-monitor`](s6-t8-heap-monitor.md) (Heap monitor)

**Blocks:** 
- [`s6-t12-keep-gates-green`](s6-t12-keep-gates-green.md) (Keep gates green)
- [`s7-t5-verify-mutex-timeout`](../sprint-07/s7-t5-verify-mutex-timeout.md) (Verify mutex timeout)
- [`s7-t7-verify-recovery-counts`](../sprint-07/s7-t7-verify-recovery-counts.md) (Verify recovery counts)
- [`s7-t8-verify-watchdog`](../sprint-07/s7-t8-verify-watchdog.md) (Verify watchdog)
- [`s7-t10-fault-injection-matrix`](../sprint-07/s7-t10-fault-injection-matrix.md) (Fault-injection matrix)

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
