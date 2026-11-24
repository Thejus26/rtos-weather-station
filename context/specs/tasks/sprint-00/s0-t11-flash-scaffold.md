# s0-t11: Flash scaffold

| Field | Value |
|-------|-------|
| Task ID | `s0-t11-flash-scaffold` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Flash the scaffold and open the monitor from the host. Note the COM port.

## Acceptance criteria

- [ ] Boot banner appears on the serial monitor.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-4 | Flash and monitor from the host, not from Docker |
| HW-1 | ESP32-DevKitC (WROOM-32E, 4 MB flash), USB 5 V power |

## Dependencies

**Depends on:** 
- [`s0-t1-parts-and-hardware-check`](s0-t1-parts-and-hardware-check.md) (Parts and hardware check)
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** 
- [`s2-t1-wire-circuit`](../sprint-02/s2-t1-wire-circuit.md) (Wire circuit)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
