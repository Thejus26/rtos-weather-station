# s9-t1: DHT22 comparison

| Field | Value |
|-------|-------|
| Task ID | `s9-t1-dht22-comparison` |
| Sprint | [Sprint 9: Backlog (Stretch Goals)](../../sprint-09-backlog.md) |
| Branch | none (backlog, not scheduled) |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

DHT22 on the RMT peripheral behind the `sensor_read()` interface, compared against the BME280 under the same conditions.

## Acceptance criteria

- [ ] Side-by-side readings exist.
- [ ] A short comparison is in the README.

## Requirements covered

| ID | Requirement |
|----|-------------|
| STR-1 | Stretch: DHT22 on the RMT peripheral, compared with the BME280 |
| HW-7 | Alternate sensors (SHT31) can replace the BME280 |

## Dependencies

**Depends on:** 
- [`s8-t10-tag-release`](../sprint-08/s8-t10-tag-release.md) (Tag release)

**Blocks:** none in the roadmap

## Open questions

- the roadmap says DHT22 "behind the `sensor_read()` interface" but does not name the comparison conditions or how many samples to compare.

## Source

Derived from [`sprint-09-backlog.md`](../../sprint-09-backlog.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
