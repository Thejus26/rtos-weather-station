# Sprint 9: Backlog (Stretch Goals)

## Goal

Hold the optional stretch goals, started only after Sprint 8. They are not scheduled. Each one needs its own short spec in `context/specs/` before work starts.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's (backlog tasks use sprint number 9).

### s9-t1 · DHT22 comparison
- **ID:** s9-t1-dht22-comparison
- **Description:** DHT22 on the RMT peripheral behind the `sensor_read()` interface, compared against the BME280 under the same conditions.
- **Acceptance criteria:**
  - Side-by-side readings exist.
  - A short comparison is in the README.
- **Dependencies:** s8-t10-tag-release
- **Effort:** L
- **Covers:** STR-1, HW-7

### s9-t2 · Sleep and current
- **ID:** s9-t2-sleep-and-current
- **Description:** Light or deep sleep between samples. Measure current with and without sleep, and optionally run from an 18650 and regulator.
- **Acceptance criteria:**
  - A measured current table exists.
  - Any timing regressions are fixed.
- **Dependencies:** s8-t10-tag-release
- **Effort:** L
- **Covers:** STR-2

### s9-t3 · BLE or HTTP dashboard
- **ID:** s9-t3-ble-or-http-dashboard
- **Description:** Serve readings over BLE or an HTTP dashboard.
- **Acceptance criteria:**
  - A phone or browser shows live readings.
- **Dependencies:** s8-t10-tag-release
- **Effort:** L
- **Covers:** STR-3

### s9-t4 · STM32 port
- **ID:** s9-t4-stm32-port
- **Description:** Port the application to STM32 with an external Wi-Fi module, using the notes from s8-t6-reflection-notes.
- **Acceptance criteria:**
  - The same task and queue design runs on the STM32.
- **Dependencies:** s8-t10-tag-release
- **Effort:** L
- **Covers:** STR-4

## Definition of Done

- No sprint-level exit gate is defined in the roadmap. A stretch task is done when its own acceptance criteria above are met.

## Open Questions

- **Scope:** the roadmap says each task needs its own short spec first, so these four entries are placeholders and not ready to implement.
- **s9-t1:** the roadmap says DHT22 "behind the `sensor_read()` interface" but does not name the comparison conditions or how many samples to compare.
- **s9-t2:** the current-measurement tool is not named, and nothing says what sleep period or timing regression threshold is acceptable (TIM-1 jitter is the nearest existing limit).
- **s9-t3:** the roadmap leaves BLE versus HTTP open, with no default.
- **s9-t4:** the roadmap does not name the STM32 board or the Wi-Fi module.
- **Hardware:** parts for these tasks (DHT22, 18650 with regulator, current meter, STM32 board and Wi-Fi module) are not in the Sprint 0 parts check.
