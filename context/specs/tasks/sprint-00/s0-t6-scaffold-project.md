# s0-t6: Scaffold project

| Field | Value |
|-------|-------|
| Task ID | `s0-t6-scaffold-project` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Scaffold the ESP-IDF project: root `CMakeLists.txt`, `main/CMakeLists.txt`, `main/main.c` (boot banner only). Run `idf.py set-target esp32` then `idf.py build`.

## Acceptance criteria

- [ ] Clean build with no warnings.

## Requirements covered

| ID | Requirement |
|----|-------------|
| PLT-1 | ESP32-DevKitC, ESP-IDF v5.x, native FreeRTOS (not the Arduino framework) |
| BLD-3 | Firmware build with ESP-IDF v5.x, natively or in the `espressif/idf` container |

## Dependencies

**Depends on:** 
- [`s0-t5-install-esp-idf`](s0-t5-install-esp-idf.md) (Install ESP-IDF)

**Blocks:** 
- [`s0-t7-container-firmware-build`](s0-t7-container-firmware-build.md) (Container firmware build (optional))
- [`s0-t8-sdkconfig-defaults`](s0-t8-sdkconfig-defaults.md) (`sdkconfig.defaults`)
- [`s0-t9-app-config-header`](s0-t9-app-config-header.md) (`app_config.h`)
- [`s0-t10-kconfig-menu`](s0-t10-kconfig-menu.md) (Kconfig menu)
- [`s0-t11-flash-scaffold`](s0-t11-flash-scaffold.md) (Flash scaffold)
- [`s2-t2-choose-i2c-api`](../sprint-02/s2-t2-choose-i2c-api.md) (Choose I2C API)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
