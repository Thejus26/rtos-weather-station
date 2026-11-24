# s8-t8: Acceptance walkthrough

| Field | Value |
|-------|-------|
| Task ID | `s8-t8-acceptance-walkthrough` |
| Sprint | [Sprint 8: Documentation, Demo and Acceptance](../../sprint-08-documentation-acceptance.md) |
| Branch | `docs/deliverables` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Acceptance walk-through: check FR-1 to FR-10 and ACC-1 to ACC-5, each against a named piece of evidence.

## Acceptance criteria

- [ ] A checklist exists with a link beside every item.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ACC-1 | All functional requirements FR-1 to FR-10 pass |
| ACC-2 | All timing requirements are met in measurement |
| ACC-3 | Recovers from every fault in the error-handling table without manual intervention |
| ACC-4 | No task stack above 75% usage |
| ACC-5 | `make docker-test` passes in the lightweight container with no warnings |
| FR-1 | Sample temperature and humidity every 5 s |
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| FR-3 | Calculate dew point from the filtered values |
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |
| FR-5 | Push button toggles C/F, via ISR and semaphore |
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |

## Dependencies

**Depends on:** 
- [`s8-t3-stack-table`](s8-t3-stack-table.md) (Stack table)
- [`s8-t4-collect-test-evidence`](s8-t4-collect-test-evidence.md) (Collect test evidence)

**Blocks:** 
- [`s8-t9-finalise-docs-status`](s8-t9-finalise-docs-status.md) (Finalise docs status)

## Source

Derived from [`sprint-08-documentation-acceptance.md`](../../sprint-08-documentation-acceptance.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
