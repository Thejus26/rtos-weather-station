# s7-t6: Verify backoff

| Field | Value |
|-------|-------|
| Task ID | `s7-t6-verify-backoff` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Reconnect backoff: capture reconnect timing with the AP off.

## Acceptance criteria

- [ ] Delays follow 1 s doubling to 60 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-7 | Wi-Fi reconnect backoff 1 s doubling up to 60 s |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
