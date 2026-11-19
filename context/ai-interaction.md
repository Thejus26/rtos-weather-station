# AI Interaction Guidelines: RTOS Weather Station (ESP32 / FreeRTOS, C)

## Communication

- Be concise, direct, and explain concepts simply (like I'm 15) using intuitive, real-world analogies and plain English.
- **Local Toolchain Note**: Host unit tests run in the Docker test container, started from PowerShell (see [`code-build.md`](code-build.md)). Firmware builds use ESP-IDF v5.x (`idf.py`), natively or in the `espressif/idf` container. Flashing runs on the host. Do not install toolchains globally without asking.
- Explain non-obvious design decisions clearly. This is a learning project, so say *why*, not just *what*. For RTOS choices (priorities, stack sizes, which synchronisation object), explain the trade-off.
- Ask before large refactors or architectural changes.
- Don't add features or dependencies not in the project scope ([`project-overview.md`](project-overview.md)). Stay on ESP-IDF v5.x with native FreeRTOS: no Arduino framework, no platform change.
- Never delete files without explicit confirmation.
- **Precedence**: the files in `context/` are authoritative for this project. The Python-specific rules, hooks and skills under `.claude/` and `.agents/` come from an earlier Python template. Do not follow their pytest, ruff or mypy instructions here. The project-local `.venv` exists only for the optional graphify tool ([`code-build.md`](code-build.md) section 9). (Remove this note once those files are adapted.)

---

## Workflow

This is the standard workflow used for every feature, task, driver or bug fix:

1. **Document** - Document the feature/task in `context/current-feature.md`: requirement IDs (FR-n), files, objects touched, test scenarios.
2. **Branch** - Create a new git branch for the feature/fix (e.g., `feature/[feature-name]` or `fix/[fix-name]`).
3. **Implement** - Implement the feature/fix adhering to [`coding-standards.md`](coding-standards.md) and the module boundaries in [`project-structure.md`](project-structure.md).
4. **Verify** - Run the quality gates in [`code-build.md`](code-build.md) section 6: host unit tests in the container, `idf.py build` when firmware changed, and the matching hardware checks when RTOS behaviour changed.
5. **Iterate** - Refine logic, timing values, error handling and log messages as needed.
6. **Commit** - Only after the code is verified and the gates pass.
7. **Merge** - Merge into `main`.
8. **Delete Branch** - Clean up the feature branch once merged.
9. **Review** - Review generated code periodically and on demand.
10. **Update Tracker** - Mark as completed in `context/current-feature.md` and add an entry to history.
11. **Learn** - Add what failed and what you learned (priority inversion, stack sizing, STM32 porting notes) to the project `README.md` ("Notes" section).

> Do NOT commit without permission and until the verification criteria pass. If a host test fails or the build breaks, resolve the issue first.

---

## Branching

- Create a new branch for every feature or fix.
- Name branches following the pattern:
  - `feature/[feature-name]` (e.g., `feature/dew-point`, `feature/sensor-task`)
  - `fix/[fix-name]` (e.g., `fix/i2c-mutex-timeout`, `fix/publish-queue-drop-oldest`)
  - `refactor/[module-name]` (e.g., `refactor/app-logic`)
- Ask to delete the branch once merged into `main`.
- The enclosing git repository may be rooted above this folder. Always stage explicit paths inside this project; never `git add .` or `git add -A` from a parent directory.

---

## Commits

- Ask before committing (do not auto-commit).
- Use Conventional Commits format (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`).
  - Example: `feat(app_logic): add dew point calculation`
  - Example: `fix(sensor): release i2c_mutex when the read times out`
  - Example: `test(app_logic): cover moving average window rollover`
- Keep commits atomic and focused (one logical change per commit).
- Never include AI attribution watermarks in commit messages.
- Never commit `sdkconfig`, `build/`, `build-host/`, `managed_components/`, Wi-Fi credentials or broker secrets.

---

## When Stuck

- If something is not resolving after 2–3 attempts, stop and explain the issue clearly.
- Avoid trial-and-error guessing with ESP-IDF and FreeRTOS APIs. Read the official ESP-IDF and FreeRTOS documentation, and compare against the exact serial log, backtrace or build error.
- For crashes and watchdog resets, start from the panic backtrace and the failing task's name and stack high-water mark.
- Ask for clarification if the hardware (board, sensor variant, I2C address) or the expected behaviour is ambiguous.

---

## Code Changes

- Make minimal, targeted changes to accomplish the task.
- Do not refactor unrelated modules unless explicitly asked.
- Avoid unnecessary dependencies. Every extra component or managed component needs a reason.
- Maintain the module boundaries and naming conventions in [`project-structure.md`](project-structure.md) and [`coding-standards.md`](coding-standards.md) section 3.
- Keep `README.md` and `context/project-overview.md` in sync, and update `context/project-structure.md` when files are added, moved or removed.

---

## Code Review & Quality Checklist

Review code periodically against [`coding-standards.md`](coding-standards.md), specifically ensuring:

- **RTOS Correctness**:
  - Priorities, stack sizes and queue depths match the overview.
  - Mutexes are held briefly, never two at once (`i2c_mutex` before `data_mutex` if unavoidable), with a 100 ms timeout on `i2c_mutex`.
  - ISRs use only `FromISR` APIs, and `FromISR` APIs are used only in the ISR.
  - Periodic sampling uses `vTaskDelayUntil`.
- **Memory**:
  - No dynamic allocation in steady state.
  - Each task keeps at least 25% stack headroom, measured with `uxTaskGetStackHighWaterMark`.
- **Fault Handling**:
  - Every failure that can happen is checked and reported to `error_queue` with a zero timeout.
  - No `ESP_ERROR_CHECK` in steady-state paths.
  - Wi-Fi or broker loss never stops sampling and display.
- **Secrets & Privacy**:
  - Credentials and broker settings come from `menuconfig`/NVS, never from source, logs, tests or commits.
- **Logging**:
  - `ESP_LOG*` with a tag per file. No logging in ISRs.
- **Module Boundaries**:
  - `components/app_logic/` has no ESP-IDF or FreeRTOS includes.
- **Tests**:
  - Host tests for the moving average, validation and dew-point logic, including boundaries and failure paths. Hardware claims (timing, stack, recovery) are backed by measurements in `docs/`, not by host tests.
