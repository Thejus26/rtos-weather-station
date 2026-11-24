# s0-t10: Kconfig menu

| Field | Value |
|-------|-------|
| Task ID | `s0-t10-kconfig-menu` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Create `main/Kconfig.projbuild` with a "Weather Station" menu: sample period, publish period, device ID, BME280 address. Wi-Fi and MQTT options are added in s5-t1-kconfig-network-options. This file is not in the overview's layout, so update the overview, README and structure doc.

## Acceptance criteria

- [ ] The options appear in `idf.py menuconfig`.
- [ ] The options reach the build as `CONFIG_*`.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |
| FR-1 | Sample temperature and humidity every 5 s |
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |

## Dependencies

**Depends on:** 
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** 
- [`s2-t7-bme280-address-config`](../sprint-02/s2-t7-bme280-address-config.md) (BME280 address config)
- [`s5-t1-kconfig-network-options`](../sprint-05/s5-t1-kconfig-network-options.md) (Kconfig network options)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
