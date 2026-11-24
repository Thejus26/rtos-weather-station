# Sprint 1: Pure-C Logic (host only)

## Goal

Write and unit-test, in the Docker container, every decision that can be made without hardware. Branch: `feature/app-logic`. No hardware needed, so this sprint can run while parts are on order.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s1-t1 · Decide average and dew point
- **ID:** s1-t1-decide-average-and-dewpoint
- **Description:** Settle D-1 (partial moving-average window) and D-2 (dew point at 0 %RH). Log both in roadmap section 10.
- **Acceptance criteria:**
  - Both decisions are written down with the chosen behaviour.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** S
- **Covers:** FR-2, FR-3

### s1-t2 · Moving average
- **ID:** s1-t2-moving-average
- **Description:** `components/app_logic/moving_average.[ch]`: window of 5 in a fixed struct (no heap), init/push/value API, behaviour per D-1.
- **Acceptance criteria:**
  - Compiles with `-Wall -Wextra -Werror`.
  - No ESP-IDF includes.
- **Dependencies:** s1-t1-decide-average-and-dewpoint
- **Effort:** S
- **Covers:** FR-2, NFR-1, NFR-4

### s1-t3 · Moving average test
- **ID:** s1-t3-moving-average-test
- **Description:** `test/host/test_moving_average.c`: first sample, partial window, full window, rollover, constant input, step input.
- **Acceptance criteria:**
  - All assertions pass in the container.
- **Dependencies:** s1-t2-moving-average
- **Effort:** S
- **Covers:** FR-2, BLD-2

### s1-t4 · Validate
- **ID:** s1-t4-validate
- **Description:** `components/app_logic/validate.[ch]`: result enum and a validate function. Reject temperature outside -40 to 85, humidity outside 0 to 100, a jump over 10 C from the previous accepted sample, and NaN. Accept the first sample and the exact limits.
- **Acceptance criteria:**
  - Every rejection reason has a distinct result code.
- **Dependencies:** s1-t1-decide-average-and-dewpoint
- **Effort:** M
- **Covers:** FR-2, ERR-2, NFR-4

### s1-t5 · Validate test
- **ID:** s1-t5-validate-test
- **Description:** `test/host/test_validate.c`: limits accepted (-40, 85, 0, 100), just outside rejected, a jump of exactly 10 accepted and more than 10 rejected, first sample, NaN.
- **Acceptance criteria:**
  - Every rejection branch is hit at least once.
- **Dependencies:** s1-t4-validate
- **Effort:** S
- **Covers:** ERR-2, BLD-2

### s1-t6 · Dew point
- **ID:** s1-t6-dew-point
- **Description:** `components/app_logic/dew_point.[ch]`: Magnus formula in `float`, behaviour at 0 %RH per D-2.
- **Acceptance criteria:**
  - Never returns NaN or infinity for valid input.
- **Dependencies:** s1-t1-decide-average-and-dewpoint
- **Effort:** S
- **Covers:** FR-3, NFR-4

### s1-t7 · Dew point test
- **ID:** s1-t7-dew-point-test
- **Description:** `test/host/test_dew_point.c`: 20 C and 50 %RH gives about 9.27 C (within 0.1); 100 %RH returns the air temperature; 0 %RH is defined; a negative-temperature case.
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s1-t6-dew-point
- **Effort:** S
- **Covers:** FR-3, BLD-2

### s1-t8 · Unit convert
- **ID:** s1-t8-unit-convert
- **Description:** `components/app_logic/unit_convert.[ch]` with Celsius to Fahrenheit, and `test_unit_convert.c` (freezing, boiling, negative values).
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** S
- **Covers:** FR-5, BLD-2

### s1-t9 · Backoff
- **ID:** s1-t9-backoff
- **Description:** `components/app_logic/backoff.[ch]`: next delay starts at 1000 ms, doubles, caps at 60000 ms, resets on success.
- **Acceptance criteria:**
  - Compiles clean.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** S
- **Covers:** TIM-7, FR-7, NFR-4

### s1-t10 · Backoff test
- **ID:** s1-t10-backoff-test
- **Description:** `test/host/test_backoff.c`: sequence 1, 2, 4, 8, 16, 32, 60, 60 seconds; reset; no overflow after many failures.
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s1-t9-backoff
- **Effort:** S
- **Covers:** TIM-7, BLD-2

### s1-t11 · Fault policy
- **ID:** s1-t11-fault-policy
- **Description:** `components/app_logic/fault_policy.[ch]`: count consecutive sensor failures (re-init request at 3), count failed recoveries (restart request at 10), reset counters on success.
- **Acceptance criteria:**
  - The state machine is a plain struct with no timers or RTOS calls.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** M
- **Covers:** FR-8, TIM-8, ERR-1, NFR-4

### s1-t12 · Fault policy test
- **ID:** s1-t12-fault-policy-test
- **Description:** `test/host/test_fault_policy.c`: 2 failures do nothing, 3 request re-init, success resets, 10 failed recoveries request restart.
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s1-t11-fault-policy
- **Effort:** S
- **Covers:** TIM-8, BLD-2

### s1-t13 · Heap policy
- **ID:** s1-t13-heap-policy
- **Description:** Settle D-14. `components/app_logic/heap_policy.[ch]`: decide ok / warn / restart from free-heap samples against the 20 KB threshold and the falling-trend rule.
- **Acceptance criteria:**
  - The decision is a pure function of the supplied samples.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** M
- **Covers:** ERR-6, FR-9, NFR-3, NFR-4

### s1-t14 · Heap policy test
- **ID:** s1-t14-heap-policy-test
- **Description:** `test/host/test_heap_policy.c`: above threshold, below threshold, falling then recovering, falling for N checks.
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s1-t13-heap-policy
- **Effort:** S
- **Covers:** ERR-6, BLD-2

### s1-t15 · Reading JSON
- **ID:** s1-t15-reading-json
- **Description:** Settle D-11. `components/app_logic/reading_json.[ch]`: format a reading into a caller-supplied buffer with length checking (no heap).
- **Acceptance criteria:**
  - Returns an error instead of overflowing a too-small buffer.
- **Dependencies:** s1-t1-decide-average-and-dewpoint
- **Effort:** M
- **Covers:** FR-6, NFR-1, NFR-4

### s1-t16 · Reading JSON test
- **ID:** s1-t16-reading-json-test
- **Description:** `test/host/test_reading_json.c`: exact output for a known reading, truncation detection, pre-sync timestamp marker.
- **Acceptance criteria:**
  - Assertions pass.
- **Dependencies:** s1-t15-reading-json
- **Effort:** S
- **Covers:** FR-6, BLD-2

### s1-t17 · App types header
- **ID:** s1-t17-app-types-header
- **Description:** Settle D-3. `main/app_types.h` (stdint-only): `sample_t`, `reading_t`, `error_event_t`, and fault source/code enums.
- **Acceptance criteria:**
  - Compiles in the firmware build and on the host.
- **Dependencies:** s1-t4-validate
- **Effort:** S
- **Covers:** OBJ-1, OBJ-2, OBJ-3, FR-8

### s1-t18 · Full suite run
- **ID:** s1-t18-full-suite-run
- **Description:** Delete `test_smoke.c`. Run the whole suite from clean. Save the passing output to `docs/test-results/host-tests.txt`.
- **Acceptance criteria:**
  - `make test` exits 0 with no warnings.
  - Output file is saved.
- **Dependencies:** s1-t3-moving-average-test, s1-t5-validate-test, s1-t7-dew-point-test, s1-t10-backoff-test, s1-t12-fault-policy-test, s1-t14-heap-policy-test, s1-t16-reading-json-test
- **Effort:** S
- **Covers:** BLD-2, DEL-3a, ACC-5

### s1-t19 · Sync layout docs
- **ID:** s1-t19-sync-layout-docs
- **Description:** Update the overview's layout, README and `project-structure.md` for the added `app_logic` modules (`unit_convert`, `backoff`, `fault_policy`, `heap_policy`, `reading_json`).
- **Acceptance criteria:**
  - Layout lists match across all three files.
- **Dependencies:** s1-t18-full-suite-run
- **Effort:** S
- **Covers:** none listed

## Definition of Done

- `make docker-test` is green from a clean checkout.
- Every `app_logic` module has a test file.
- `app_logic` contains no ESP-IDF or FreeRTOS includes.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-1** (s1-t1): moving-average output before 5 samples exist. Recommended default: average of the samples received so far.
- **D-2** (s1-t1): dew point at 0 %RH. Recommended default: clamp humidity to a small minimum (for example 1 %) inside `dew_point` and document it.
- **D-3** (s1-t17): where shared types live. Recommended default: `main/app_types.h`, stdint-only, with `app_logic` functions taking plain values.
- **D-11** (s1-t15): JSON schema, timestamp format and pre-sync behaviour. Recommended default: `device_id`, ISO 8601 UTC `ts`, `temperature_c`, `humidity_pct`, `dew_point_c`, with an explicit marker before SNTP sync.
- **D-14** (s1-t13): what "heap continues to fall" means. Recommended default: restart if the minimum free heap fell on N consecutive checks. The roadmap leaves N to be chosen and logged.
- **s1-t8:** the task combines the module and its test in one row, but there is no separate "unit-convert-test" task ID. Treat both as one deliverable.
