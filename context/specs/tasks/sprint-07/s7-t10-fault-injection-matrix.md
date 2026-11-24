# s7-t10: Fault-injection matrix

| Field | Value |
|-------|-------|
| Task ID | `s7-t10-fault-injection-matrix` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Fault-injection matrix: sensor unplugged, out-of-range value, Wi-Fi off, broker down, queue overflow, task hang, low heap. One row per fault with the steps, the expected response, the observed response, and the log excerpt.

## Acceptance criteria

- [ ] Every row recovers without manual intervention.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| ERR-3 | Wi-Fi/MQTT loss: keep sampling and displaying, buffer, reconnect with backoff |
| ERR-4 | Queue full: drop oldest, count the drop, log it |
| ERR-5 | Task hang: task watchdog logs the cause and restarts |
| ERR-6 | Low heap (for example below 20 KB): log a warning, restart if it keeps falling |
| ACC-3 | Recovers from every fault in the error-handling table without manual intervention |
| DEL-3b | Test evidence: fault-injection results (sensor unplugged, Wi-Fi off, broker down, queue overflow) |
| GOAL-4 | Handle sensor, network and resource faults without hanging |

## Dependencies

**Depends on:** 
- [`s6-t11-fault-injection-hooks`](../sprint-06/s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

**Blocks:** 
- [`s7-t13-soak-24h`](s7-t13-soak-24h.md) (Soak 24 h)

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
