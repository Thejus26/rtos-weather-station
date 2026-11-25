# Current Feature

## Status
Not Started

## Goals
<!-- Measurable criteria and deliverables for the active feature. -->

## Notes
<!-- Design constraints, module boundaries, API behavior, or tool-schema requirements. -->

## History
<!-- Append-only. Keep the 3-5 most recent completed features here; archive older ones to context/feature-history.md. -->
- **s0-t4-harness-smoke-test** (2026-11-24): added temporary `test/host/test_smoke.c` (deleted in s1-t18). In the container under `--memory 256m --cpus 1`: a passing assert gives `make test` exit 0; a failing assert stops make with Error 134 (docker exit 2); caps confirmed via `docker inspect` and cgroup (memory.max 268435456, cpu.max 100000 100000); an unused variable fails the compile under `-Wall -Wextra -Werror`. `make docker-test` end to end not run (no GNU make on the Windows host). Header-prerequisite gap still deferred, to s1-t8. Commit `be699b6`.
- **s0-t5-install-esp-idf** (2026-11-24): container route chosen (no native install). `espressif/idf:v5.5.6` pulled; `idf.py --version` prints `ESP-IDF v5.5.6` (exit 0); image 9.22 GB on disk (~5 GB compressed); `i2c_master.h` present (D-4). Caps `--memory 2g --cpus 2` verified via `docker inspect` and cgroup, inside the existing 3 GB / 2 CPU Docker VM limit. Tag pinned in README, project-overview, code-build and AGENTS; decision and numbers in README Notes. Not measured: pull time and first firmware build (deferred to s0-t6 / s0-t7; the 2 GB cap is untested with a real build, exit 137 means raise it). Commit `e50cc1f`.
- **s0-t6-scaffold-project** (2026-11-25): added root `CMakeLists.txt` (`project(weather_station)`), `main/CMakeLists.txt`, and `main/main.c` (boot banner logging project name and ESP-IDF version). Verified in the `espressif/idf:v5.5.6` container under `--memory 2g --cpus 2`: `idf.py set-target esp32 build` succeeds with exit 0 and no compiler warnings. `build/weather_station.bin` produced (162,208 bytes, 85% free in 1MB default partition; DRAM 12,508 B, IRAM 52,943 B). Host test regression (`make test`) verified clean under -Wall -Wextra -Werror. Commit `302e3b1`.
- **s0-t7-container-firmware-build** (2026-11-25): documentation-only update recording the measured `espressif/idf:v5.5.6` container firmware build metrics from `s0-t6` (578 s cold full build, 162,208 B `build/weather_station.bin`, 9 s `idf.py size`, zero warnings) in `README.md` Notes ("Toolchain (s0-t5)" and "First firmware build (s0-t6, s0-t7)"), and clarifying `context/specs/tasks/sprint-00/s0-t7-container-firmware-build.md`. Pull time recorded as not measured (image pulled in `s0-t5` without timing). Commit `f7ca894`.
- **s0-t8-sdkconfig-defaults** (2026-11-25): added `sdkconfig.defaults` (`CONFIG_FREERTOS_HZ=1000`, `CONFIG_ESP_TASK_WDT_EN=y`, `CONFIG_ESP_TASK_WDT_INIT=y`, `CONFIG_ESP_TASK_WDT_TIMEOUT_S=10`, `CONFIG_ESP_TASK_WDT_PANIC=y`, no credentials), updated `context/project-structure.md` (`[exists]`), and documented verification in `README.md` Notes. Verified in `espressif/idf:v5.5.6` (`--memory 2g --cpus 2`) after deleting stale `sdkconfig` via `idf.py fullclean set-target esp32 build` (exit 0, 417 s, zero warnings, `weather_station.bin` 162,224 B); generated `sdkconfig` and `build/config/sdkconfig.h` confirm all four values. Watchdog timeout behaviour deferred to `s6-t7` on hardware. Commit `17c2336`.
