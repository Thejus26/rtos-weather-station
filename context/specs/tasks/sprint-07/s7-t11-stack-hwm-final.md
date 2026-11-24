# s7-t11: Stack high-water marks, final

| Field | Value |
|-------|-------|
| Task ID | `s7-t11-stack-hwm-final` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Stack high-water marks under worst-case load (reconnect, publish, redraw). Resize any task over 75% used and re-measure.

## Acceptance criteria

- [ ] Every task has at least 25% headroom.
- [ ] The final table is recorded.

## Requirements covered

| ID | Requirement |
|----|-------------|
| NFR-2 | Every task has a measured stack high-water mark with at least 25% headroom |
| ACC-4 | No task stack above 75% usage |
| DEL-2 | `docs/`: wiring diagram, task and communication diagram, priorities/stacks/measured high-water marks table |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** 
- [`s7-t13-soak-24h`](s7-t13-soak-24h.md) (Soak 24 h)
- [`s8-t3-stack-table`](../sprint-08/s8-t3-stack-table.md) (Stack table)

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
