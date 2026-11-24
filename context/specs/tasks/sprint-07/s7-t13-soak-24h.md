# s7-t13: Soak 24 h

| Field | Value |
|-------|-------|
| Task ID | `s7-t13-soak-24h` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

24-hour soak. Capture serial to a file with timestamps, free and minimum-free heap, uptime, reset reason and drop counters. Apply the D-17 criterion.

## Acceptance criteria

- [ ] No reset.
- [ ] No heap growth beyond the criterion.
- [ ] The log and a summary are saved.

## Requirements covered

| ID | Requirement |
|----|-------------|
| NFR-3 | 24-hour continuous run without reset or heap growth |
| DEL-3c | Test evidence: 24-hour soak log with stable heap and no resets |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-17** (referenced here): Soak pass criterion for "no heap growth"
  - Recommended default: Minimum free heap at hour 24 is no lower than at hour 1 minus a stated margin (for example 1 KB), and no reset
  - Why it matters: NFR-3 does not quantify growth

## Dependencies

**Depends on:** 
- [`s7-t1-measure-sampling-jitter`](s7-t1-measure-sampling-jitter.md) (Measure sampling jitter)
- [`s7-t10-fault-injection-matrix`](s7-t10-fault-injection-matrix.md) (Fault-injection matrix)
- [`s7-t11-stack-hwm-final`](s7-t11-stack-hwm-final.md) (Stack high-water marks, final)

**Blocks:** 
- [`s7-t14-no-alloc-audit`](s7-t14-no-alloc-audit.md) (No-allocation audit)

## Open questions

- the roadmap says the soak needs "a stable power supply and a machine that can capture serial for a full day", but does not say whether fault-injection hooks must be off during the soak. They are off by default in the build (s6-t11).

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
