# s5-t3: NVS config

| Field | Value |
|-------|-------|
| Task ID | `s5-t3-nvs-config` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

NVS initialisation with erase-and-retry on a version mismatch, and reading of the configuration values.

## Acceptance criteria

- [ ] The boot log shows config loaded.
- [ ] No credentials are printed.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |

## Dependencies

**Depends on:** 
- [`s5-t1-kconfig-network-options`](s5-t1-kconfig-network-options.md) (Kconfig network options)

**Blocks:** 
- [`s5-t4-wifi-station`](s5-t4-wifi-station.md) (Wi-Fi station)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
