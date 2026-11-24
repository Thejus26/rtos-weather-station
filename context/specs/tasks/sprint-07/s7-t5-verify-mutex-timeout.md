# s7-t5: Verify mutex timeout

| Field | Value |
|-------|-------|
| Task ID | `s7-t5-verify-mutex-timeout` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

I2C mutex timeout: hold the mutex past 100 ms with the injection hook and confirm the error is reported.

## Acceptance criteria

- [ ] The timeout is logged within about 100 ms.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t11-fault-injection-hooks`](../sprint-06/s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
