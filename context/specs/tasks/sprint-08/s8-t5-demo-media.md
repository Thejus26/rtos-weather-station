# s8-t5: Demo media

| Field | Value |
|-------|-------|
| Task ID | `s8-t5-demo-media` |
| Sprint | [Sprint 8: Documentation, Demo and Acceptance](../../sprint-08-documentation-acceptance.md) |
| Branch | `docs/deliverables` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Demo: a short video or screenshots of the OLED, the serial log and the MQTT subscriber output.

## Acceptance criteria

- [ ] Media is saved.
- [ ] It is referenced from the README.

## Requirements covered

| ID | Requirement |
|----|-------------|
| DEL-4 | Demo: video or screenshots of OLED, serial log and MQTT subscriber output |
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |

## Dependencies

**Depends on:** 
- [`s7-t15-final-gates-run`](../sprint-07/s7-t15-final-gates-run.md) (Final gates run)

**Blocks:** none in the roadmap

## Open questions

- the roadmap allows "video or screenshots" without a preference or a size limit for the repository.

## Source

Derived from [`sprint-08-documentation-acceptance.md`](../../sprint-08-documentation-acceptance.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
