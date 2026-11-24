# s2-t13: Status LED driver

| Field | Value |
|-------|-------|
| Task ID | `s2-t13-status-led-driver` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

`main/drivers/status_led.[ch]`: on, off and toggle on GPIO2.

## Acceptance criteria

- [ ] The LED toggles from firmware.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |

## Dependencies

**Depends on:** 
- [`s2-t1-wire-circuit`](s2-t1-wire-circuit.md) (Wire circuit)

**Blocks:** 
- [`s2-t15-bringup-loop`](s2-t15-bringup-loop.md) (Bring-up loop)
- [`s6-t6-status-led-states`](../sprint-06/s6-t6-status-led-states.md) (Status LED states)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
