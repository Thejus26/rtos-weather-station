# s6-t6: Status LED states

| Field | Value |
|-------|-------|
| Task ID | `s6-t6-status-led-states` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-6. Status LED state machine driven by `monitor_task`: OK, no network, sensor fault, critical.

## Acceptance criteria

- [ ] Each state shows its own pattern on the LED.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-6** (settled in this task): Status LED patterns
  - Recommended default: Solid = OK, slow blink = no network, fast blink = sensor fault, double blink = critical
  - Why it matters: FR-9 says "shows system state" without defining states

## Dependencies

**Depends on:** 
- [`s6-t2-error-dispatch`](s6-t2-error-dispatch.md) (Error dispatch)
- [`s2-t13-status-led-driver`](../sprint-02/s2-t13-status-led-driver.md) (Status LED driver)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
