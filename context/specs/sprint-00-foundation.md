# Sprint 0: Foundation and Toolchain

## Goal

Build a reproducible host test loop and an ESP-IDF firmware scaffold that boots on the board, before any feature work. Branch: `chore/foundation`. Hardware: light (parts check and one flash).

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s0-t1 · Parts and hardware check
- **ID:** s0-t1-parts-and-hardware-check
- **Description:** Parts check: ESP32-DevKitC (WROOM-32E, 4 MB), BME280 breakout (note its address strap and whether it has pull-ups), SSD1306 128x64 I2C OLED, push button, LED + 330 ohm resistor, breadboard, jumpers, 4.7 k resistors, USB data cable, logic analyser (needed for the Sprint 7 jitter measurement). Order anything missing now.
- **Acceptance criteria:**
  - Every part is in hand or on order.
  - Pull-up presence on the breakouts is noted.
- **Dependencies:** None
- **Effort:** S
- **Covers:** HW-1, HW-2, HW-3, HW-4, HW-5, HW-6

### s0-t2 · Test image
- **ID:** s0-t2-test-image
- **Description:** Install Docker. Create `Dockerfile.test` (`alpine:3.20`, `build-base`, `make`, `WORKDIR /work`) and `.dockerignore`.
- **Acceptance criteria:**
  - `docker build -f Dockerfile.test -t rtos-host-test .` succeeds.
  - Image size is about 230 MB.
- **Dependencies:** None
- **Effort:** S
- **Covers:** BLD-1

### s0-t3 · Makefile
- **ID:** s0-t3-makefile
- **Description:** Create `Makefile` with `test`, `docker-test`, `clean`, from the reference in `code-build.md` section 4. Recipe lines use tabs. Host binaries go to `build-host/`.
- **Acceptance criteria:**
  - `make` parses.
  - Targets match the reference.
- **Dependencies:** s0-t2-test-image
- **Effort:** S
- **Covers:** BLD-2

### s0-t4 · Harness smoke test
- **ID:** s0-t4-harness-smoke-test
- **Description:** Add a temporary `test/host/test_smoke.c`. Prove a passing test exits 0 and a deliberately failing `assert` stops `make` with a non-zero exit, under `--memory 256m --cpus 1`.
- **Acceptance criteria:**
  - Both outcomes (pass and fail) are observed.
  - Resource caps (256 MB, 1 CPU) are respected.
- **Dependencies:** s0-t3-makefile
- **Effort:** S
- **Covers:** BLD-1, BLD-2

### s0-t5 · Install ESP-IDF
- **ID:** s0-t5-install-esp-idf
- **Description:** Install ESP-IDF v5.x natively (or commit to the container route) and record the exact version.
- **Acceptance criteria:**
  - `idf.py --version` prints a v5.x version.
- **Dependencies:** None
- **Effort:** M
- **Covers:** PLT-1, BLD-3

### s0-t6 · Scaffold project
- **ID:** s0-t6-scaffold-project
- **Description:** Scaffold the ESP-IDF project: root `CMakeLists.txt`, `main/CMakeLists.txt`, `main/main.c` (boot banner only). Run `idf.py set-target esp32` then `idf.py build`.
- **Acceptance criteria:**
  - Clean build with no warnings.
- **Dependencies:** s0-t5-install-esp-idf
- **Effort:** S
- **Covers:** PLT-1, BLD-3

### s0-t7 · Container firmware build (optional)
- **ID:** s0-t7-container-firmware-build
- **Description:** Optional: pull the pinned `espressif/idf` image and build the scaffold in it. Record image size and first-build time, and replace the "not pulled or measured" notes in the docs with the numbers.
- **Acceptance criteria:**
  - Container build produces `build/*.bin`.
  - Image size and first-build time are recorded.
- **Dependencies:** s0-t6-scaffold-project
- **Effort:** S
- **Covers:** BLD-3

### s0-t8 · `sdkconfig.defaults`
- **ID:** s0-t8-sdkconfig-defaults
- **Description:** Create `sdkconfig.defaults`: FreeRTOS tick 1000 Hz, task watchdog enabled with a 10 s timeout and restart on timeout. No credentials.
- **Acceptance criteria:**
  - After `fullclean` and a rebuild, the generated `sdkconfig` shows those values.
- **Dependencies:** s0-t6-scaffold-project
- **Effort:** S
- **Covers:** TIM-10, TIM-9, FR-9

### s0-t9 · `app_config.h`
- **ID:** s0-t9-app-config-header
- **Description:** Create `main/app_config.h`: pins (GPIO21, 22, 4, 2), I2C addresses, sample/display/publish periods, task priorities and stack sizes in bytes, queue depths, mutex timeout, backoff limits, watchdog and heap thresholds.
- **Acceptance criteria:**
  - Values match the overview tables.
  - No magic numbers are planned outside this file.
- **Dependencies:** s0-t6-scaffold-project
- **Effort:** S
- **Covers:** HW-4, HW-5, HW-6, TSK-1 to TSK-5, OBJ-1, OBJ-2, OBJ-3, TIM-6

### s0-t10 · Kconfig menu
- **ID:** s0-t10-kconfig-menu
- **Description:** Create `main/Kconfig.projbuild` with a "Weather Station" menu: sample period, publish period, device ID, BME280 address. Wi-Fi and MQTT options are added in s5-t1-kconfig-network-options. This file is not in the overview's layout, so update the overview, README and structure doc.
- **Acceptance criteria:**
  - The options appear in `idf.py menuconfig`.
  - The options reach the build as `CONFIG_*`.
- **Dependencies:** s0-t6-scaffold-project
- **Effort:** S
- **Covers:** FR-10, FR-1, FR-6

### s0-t11 · Flash scaffold [HW]
- **ID:** s0-t11-flash-scaffold
- **Description:** Flash the scaffold and open the monitor from the host. Note the COM port.
- **Acceptance criteria:**
  - Boot banner appears on the serial monitor.
- **Dependencies:** s0-t1-parts-and-hardware-check, s0-t6-scaffold-project
- **Effort:** S
- **Covers:** BLD-4, HW-1

### s0-t12 · Adapt agent tooling
- **ID:** s0-t12-adapt-agent-tooling
- **Description:** Adapt or remove the inherited Python-template tooling (`.claude/` and `.agents/` rules, hooks, `/feature` actions, graphify Stop hook, which now ignores docs-only commits) so the workflow gates match `code-build.md`. Decide whether to keep graphify. Remove the precedence note in `ai-interaction.md` when done.
- **Acceptance criteria:**
  - Hooks and rules no longer contradict the C workflow.
  - The Stop hook no longer fires spuriously.
- **Dependencies:** None
- **Effort:** M
- **Covers:** none listed

### s0-t13 · Load Sprint 1
- **ID:** s0-t13-load-sprint-1
- **Description:** Load Sprint 1 into `context/current-feature.md` and create branch `feature/app-logic`.
- **Acceptance criteria:**
  - Tracker shows the Sprint 1 goals.
  - The branch exists.
- **Dependencies:** s0-t4-harness-smoke-test
- **Effort:** S
- **Covers:** none listed

## Definition of Done

- The Docker harness works both ways (pass and fail).
- The scaffold builds without warnings and boots on the board.
- `app_config.h`, `sdkconfig.defaults` and `Kconfig.projbuild` exist.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

- **s0-t5:** native ESP-IDF install or the container route? The roadmap allows either and asks only that the choice and exact version be recorded.
- **s0-t7:** is the optional container build wanted? It is the only task that replaces the "not pulled or measured" notes with real numbers.
- **s0-t12:** keep or remove graphify? The roadmap asks for a decision but gives no default.
