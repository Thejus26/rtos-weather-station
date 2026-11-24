# s2-t14: Button bounce measure

| Field | Value |
|-------|-------|
| Task ID | `s2-t14-button-bounce-measure` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Configure GPIO4 as input with pull-up and falling-edge interrupt. Log edge timestamps and measure the contact bounce duration with the logic analyser.

## Acceptance criteria

- [ ] The bounce window is measured and recorded.
- [ ] The value is available to size the debounce in s4-t2-debounce.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |
| FR-5 | Push button toggles C/F, via ISR and semaphore |

## Dependencies

**Depends on:** 
- [`s2-t1-wire-circuit`](s2-t1-wire-circuit.md) (Wire circuit)

**Blocks:** 
- [`s2-t15-bringup-loop`](s2-t15-bringup-loop.md) (Bring-up loop)
- [`s4-t1-button-isr`](../sprint-04/s4-t1-button-isr.md) (Button ISR)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
