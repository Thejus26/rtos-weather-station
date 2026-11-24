# s7-t7: Verify recovery counts

| Field | Value |
|-------|-------|
| Task ID | `s7-t7-verify-recovery-counts` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Fault recovery counts: 3 consecutive failures trigger re-init, and 10 failed recoveries trigger a restart.

## Acceptance criteria

- [ ] Both thresholds are observed in the log.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t11-fault-injection-hooks`](../sprint-06/s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
