# s8-t7: Source review

| Field | Value |
|-------|-------|
| Task ID | `s8-t7-source-review` |
| Sprint | [Sprint 8: Documentation, Demo and Acceptance](../../sprint-08-documentation-acceptance.md) |
| Branch | `docs/deliverables` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Source review: comments on the non-obvious parts, no hard-coded credentials (search), no leftover bring-up code, `coding-standards.md` followed.

## Acceptance criteria

- [ ] The search and review checklist show no findings.

## Requirements covered

| ID | Requirement |
|----|-------------|
| DEL-1 | Source code in the specified layout, commented, no hard-coded credentials |
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |

## Dependencies

**Depends on:** 
- [`s7-t15-final-gates-run`](../sprint-07/s7-t15-final-gates-run.md) (Final gates run)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-08-documentation-acceptance.md`](../../sprint-08-documentation-acceptance.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
