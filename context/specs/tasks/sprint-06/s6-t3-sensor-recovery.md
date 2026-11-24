# s6-t3: Sensor recovery

| Field | Value |
|-------|-------|
| Task ID | `s6-t3-sensor-recovery` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-12. Sensor recovery: after 3 consecutive failures (from `fault_policy`) `monitor_task` notifies `sensor_task`, which re-initialises the driver under `i2c_mutex` and keeps `SENSOR_OK_BIT` cleared until a read succeeds.

## Acceptance criteria

- [ ] Unplugging then replugging the sensor recovers without a reset.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |
| GOAL-4 | Handle sensor, network and resource faults without hanging |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-12** (settled in this task): How `monitor_task` asks `sensor_task` to re-init
  - Recommended default: Task notification to `sensor_task`, which does the re-init itself under `i2c_mutex`
  - Why it matters: The overview says monitor "restarts the sensor" but the sensor owns the bus access

## Dependencies

**Depends on:** 
- [`s6-t2-error-dispatch`](s6-t2-error-dispatch.md) (Error dispatch)
- [`s1-t11-fault-policy`](../sprint-01/s1-t11-fault-policy.md) (Fault policy)

**Blocks:** 
- [`s6-t4-restart-after-failed-recoveries`](s6-t4-restart-after-failed-recoveries.md) (Restart after failed recoveries)
- [`s6-t5-validation-faults-feed-policy`](s6-t5-validation-faults-feed-policy.md) (Validation faults feed policy)

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
