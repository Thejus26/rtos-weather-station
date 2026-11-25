# Current Feature: Sprint 1 - Pure-C Logic (host only)

## Status
Not Started

## Goals
Spec: `context/specs/sprint-01-pure-c-logic.md`. Branch: `feature/app-logic` (created from `main`, not checked out yet). No hardware needed; no `[HW]` tasks in this sprint.

**Sprint goal:** write and unit-test in the `rtos-host-test` container every decision that can be made without hardware.

### Deliverables (task order, with target files)

| Task | Deliverable | Files | Effort |
|---|---|---|---|
| s1-t1 | Decide D-1 (average before 5 samples) and D-2 (dew point at 0 %RH); log both in roadmap section 10 | `context/specs/spec-roadmap.md` | S |
| s1-t2 | Moving average, window 5, fixed struct, no heap, init/push/value | `components/app_logic/moving_average.[ch]` | S |
| s1-t3 | Moving-average test: first, partial, full, rollover, constant, step | `test/host/test_moving_average.c` | S |
| s1-t4 | Validate: result enum + function (-40..85 C, 0..100 %RH, jump > 10 C, NaN; first sample and exact limits accepted) | `components/app_logic/validate.[ch]` | M |
| s1-t5 | Validate test: every rejection branch hit | `test/host/test_validate.c` | S |
| s1-t6 | Dew point: Magnus formula in `float`, 0 %RH per D-2 | `components/app_logic/dew_point.[ch]` | S |
| s1-t7 | Dew point test: 20 C / 50 %RH about 9.27 C (within 0.1); 100 %RH returns air temp; 0 %RH defined; negative temp | `test/host/test_dew_point.c` | S |
| s1-t8 | Unit convert (C to F) and its test, one deliverable | `components/app_logic/unit_convert.[ch]`, `test/host/test_unit_convert.c` | S |
| s1-t9 | Backoff: 1000 ms start, doubles, caps 60000 ms, resets on success | `components/app_logic/backoff.[ch]` | S |
| s1-t10 | Backoff test: 1,2,4,8,16,32,60,60 s; reset; no overflow after many failures | `test/host/test_backoff.c` | S |
| s1-t11 | Fault policy: plain-struct state machine, re-init at 3 consecutive sensor failures, restart at 10 failed recoveries, reset on success | `components/app_logic/fault_policy.[ch]` | M |
| s1-t12 | Fault policy test: 2 failures nothing, 3 re-init, success resets, 10 failed recoveries restart | `test/host/test_fault_policy.c` | S |
| s1-t13 | Heap policy: settle D-14, ok / warn / restart from free-heap samples vs 20 KB and falling-trend rule; pure function | `components/app_logic/heap_policy.[ch]` | M |
| s1-t14 | Heap policy test: above, below, falling then recovering, falling for N checks | `test/host/test_heap_policy.c` | S |
| s1-t15 | Reading JSON: settle D-11; format into caller buffer with length check, no heap | `components/app_logic/reading_json.[ch]` | M |
| s1-t16 | Reading JSON test: exact output, truncation detection, pre-sync timestamp marker | `test/host/test_reading_json.c` | S |
| s1-t17 | App types header: settle D-3; stdint-only `sample_t`, `reading_t`, `error_event_t`, fault source/code enums | `main/app_types.h` | S |
| s1-t18 | Delete `test_smoke.c`; clean full run; save passing output | `docs/test-results/host-tests.txt` | S |
| s1-t19 | Sync layout lists across overview, README, `project-structure.md` for the five new modules | `context/project-overview.md`, `README.md`, `context/project-structure.md` | S |

### Dependencies
- s1-t1 gates s1-t2, s1-t4, s1-t6, s1-t15.
- s1-t8, s1-t9, s1-t11, s1-t13 depend only on `s0-t4-harness-smoke-test` (done).
- s1-t17 depends on s1-t4.
- s1-t18 needs all seven test tasks (t3, t5, t7, t10, t12, t14, t16); s1-t19 follows s1-t18.

### Definition of Done
- [ ] `make docker-test` green from a clean checkout, no warnings.
- [ ] Every `app_logic` module has a test file.
- [ ] `components/app_logic/` contains no ESP-IDF or FreeRTOS includes.
- [ ] D-1, D-2, D-3, D-11, D-14 outcomes logged in roadmap section 10.
- [ ] Sprint-close checklist in roadmap section 1 complete.

## Notes

### Boundaries
- `components/app_logic/` stays pure C: no ESP-IDF or FreeRTOS includes, its own result enum instead of `esp_err_t`, no heap, no timers or RTOS calls in state machines.
- `main/app_types.h` is stdint-only; `app_logic` functions take plain values (D-3 default).
- Tests: one `test/host/test_<module>.c` per module, plain `assert()`, never define `NDEBUG`, build under `-Wall -Wextra -Werror`.
- Host tests never verify hardware behaviour. Nothing in this sprint claims timing, stack, I2C or Wi-Fi results.

### Config values (from `main/app_config.h`)
- `APP_BACKOFF_MIN_MS` 1000, `APP_BACKOFF_MAX_MS` 60000, `APP_BACKOFF_FACTOR` 2
- `APP_SENSOR_REINIT_AFTER` 3, `APP_RESTART_AFTER_RECOVERIES` 10
- `APP_HEAP_LOW_BYTES` 20 KB (restart rule is D-14)

### Open decisions (recommended defaults from the sprint spec)
- **D-1:** average of the samples received so far before 5 exist.
- **D-2:** clamp humidity to a small minimum (for example 1 %) inside `dew_point`, and document it.
- **D-3:** `main/app_types.h`, stdint-only.
- **D-11:** JSON keys `device_id`, ISO 8601 UTC `ts`, `temperature_c`, `humidity_pct`, `dew_point_c`, with an explicit marker before SNTP sync.
- **D-14:** restart if minimum free heap fell on N consecutive checks; N is not fixed by the roadmap and must be chosen and logged.

### Errors and fault reporting
Pure-C modules return their own result enums (validate has one distinct code per rejection reason: temperature range, humidity range, jump, NaN). Firmware wiring to `error_queue` (zero-timeout send) happens in later sprints, not here.

### Test command (PowerShell, project root)
`docker run --rm --memory 256m --cpus 1 -v "${PWD}:/work" rtos-host-test make test`

### Docs to update
`context/project-structure.md` whenever files are added or removed; README and overview together (s1-t19).

### Setup task s0-t13 status
Tracker now shows the Sprint 1 goals. Branch `feature/app-logic` exists locally (created with `git branch`, still on `main`). Per-task branch creation by `/feature start` would derive a different name, so check out `feature/app-logic` manually when starting Sprint 1 work.

## History
<!-- Append-only. Keep the 3-5 most recent completed features here; archive older ones to context/feature-history.md. -->
- **s0-t7-container-firmware-build** (2026-11-25): documentation-only update recording the measured `espressif/idf:v5.5.6` container firmware build metrics from `s0-t6` (578 s cold full build, 162,208 B `build/weather_station.bin`, 9 s `idf.py size`, zero warnings) in `README.md` Notes ("Toolchain (s0-t5)" and "First firmware build (s0-t6, s0-t7)"), and clarifying `context/specs/tasks/sprint-00/s0-t7-container-firmware-build.md`. Pull time recorded as not measured (image pulled in `s0-t5` without timing). Commit `f7ca894`.
- **s0-t8-sdkconfig-defaults** (2026-11-25): added `sdkconfig.defaults` (`CONFIG_FREERTOS_HZ=1000`, `CONFIG_ESP_TASK_WDT_EN=y`, `CONFIG_ESP_TASK_WDT_INIT=y`, `CONFIG_ESP_TASK_WDT_TIMEOUT_S=10`, `CONFIG_ESP_TASK_WDT_PANIC=y`, no credentials), updated `context/project-structure.md` (`[exists]`), and documented verification in `README.md` Notes. Verified in `espressif/idf:v5.5.6` (`--memory 2g --cpus 2`) after deleting stale `sdkconfig` via `idf.py fullclean set-target esp32 build` (exit 0, 417 s, zero warnings, `weather_station.bin` 162,224 B); generated `sdkconfig` and `build/config/sdkconfig.h` confirm all four values. Watchdog timeout behaviour deferred to `s6-t7` on hardware. Commit `17c2336`.
- **s0-t9-app-config-header** (2026-11-25): added `main/app_config.h` (macros only, no includes: pins, I2C addresses, periods/timeouts in ms, task priorities, stack sizes in bytes, queue depths, backoff, fault recovery, 10 s WDT, 20 KB heap threshold), updated `context/project-structure.md` (`[exists]`), and documented verification in `README.md` Notes. Verified in `rtos-host-test` (`--memory 256m --cpus 1`) with a throwaway `_Static_assert` TU compiled under `-std=c11 -Wall -Wextra -Werror -pedantic -fsyntax-only` (exit 0; negative check exit 1); `APP_WDT_TIMEOUT_S` matches `CONFIG_ESP_TASK_WDT_TIMEOUT_S` in `sdkconfig.defaults`. Commit `d443d4b`.
- **s0-t10-kconfig-menu** (2026-11-25): added `main/Kconfig.projbuild` (`menu "Weather Station"` with `WEATHER_SAMPLE_PERIOD_MS` 5000 [1000..60000], `WEATHER_PUBLISH_PERIOD_MS` 30000 [`WEATHER_SAMPLE_PERIOD_MS`..600000], `WEATHER_DEVICE_ID` `"esp32-weather-01"`, `WEATHER_BME280_I2C_ADDR` 0x76 [0x76..0x77]), updated `context/project-overview.md`, `README.md`, and `context/project-structure.md`. Verified in `espressif/idf:v5.5.6` (`--memory 2g --cpus 2`): `idf.py reconfigure` and `idf.py build` exit 0 with zero warnings (`weather_station.bin` 162,224 B), `sdkconfig` (`# Weather Station`) and `build/config/sdkconfig.h` contain all four `CONFIG_WEATHER_*` defaults, and out-of-range scratch values clamp/fall back with warnings. Interactive `menuconfig` UI not opened; `sdkconfig.defaults` untouched. Commit `47ad481`.
- **s0-t12-adapt-agent-tooling** (2026-11-25): adapted `.claude/` and `.agents/` rules (`c-standards.md`, `build.md`, `graphify.md`), hooks (`guard-c-code.py`, `guard-python-env.py`, `commit-message-lint.py`, `feature-reminder.py`, `graphify-staleness.py`, `settings.json`, `hooks.json`), skills/agents (`/feature`, `cleanup`, `list-components`, `research`, `README`, `code-scanner`, `graphify`), and docs (`context/ai-interaction.md`, `context/code-build.md`, `context/project-structure.md`) for C/ESP-IDF; deleted `error/` skill and Python `single-file-*` examples (14 files). Verified: all 10 hook scripts compile, both JSON configs parse, 29 env-guard/commit-lint cases + 20 C-guard cases + 7 `graphify-staleness.py` scenarios pass, real Stop hook allows stop, and `grep` finds no remaining pytest/ruff/mypy/AssistantError/python-standards text. Not run: `/feature` actions end to end or live `.agents` runtime hooks. Commit `ffdc8fe`.
