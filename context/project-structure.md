# Project Structure

Last updated: 2026-11-19. Project status: **Not started** (specification only, no source code yet).

Legend: `[exists]` is in the repository now. `[planned]` is defined in [project-overview.md](project-overview.md) or [code-build.md](code-build.md) but not created yet. Change a tag to `[exists]` when the file is added.

## Current state

```
01-rtos-based-applications/
├── README.md                       [exists]  Project summary. Mirrors project-overview.md, plus Status and Notes.
├── AGENTS.md                       [exists]  Shared context and rules for AI agents.
├── CLAUDE.md                       [exists]  Imports AGENTS.md, plus Claude Code notes.
├── .claude/                        [exists]  Claude Code config: rules, hooks, skills, agents. Inherited from a Python template, not yet adapted to this project.
├── .agents/                        [exists]  Mirror of .claude/ for other agents. Same status.
├── .venv/                          [exists]  Python 3.10 environment for the optional graphify tool only. Not tracked.
├── requirements-dev.txt            [exists]  Pins graphifyy==0.9.110 (dev tooling, see code-build.md section 9).
├── .gitignore                      [exists]  See the target structure below for what it ignores.
├── graphify-out/                   [exists]  Generated knowledge graph. Not tracked.
└── context/
    ├── project-overview.md         [exists]  Full specification (requirements, hardware, architecture, Docker workflow).
    ├── project-structure.md        [exists]  This file.
    ├── code-build.md               [exists]  Build tiers, Docker test container, firmware build, quality gates.
    ├── coding-standards.md         [exists]  C style, naming, RTOS rules, fault handling, testing standards.
    ├── ai-interaction.md           [exists]  Working agreement: workflow, branching, commits, review checklist.
    ├── current-feature.md          [exists]  Tracker for the feature in progress.
    ├── feature-history.md          [exists]  Archive of completed features.
    └── specs/                      [exists]  Feature specs (for example for `/feature load`) go here.
        ├── spec-roadmap.md         [exists]  Sprint-by-sprint implementation roadmap with requirement traceability.
        ├── spec-00-foundation.md   [exists]  Sprint 0: Docker test loop, ESP-IDF scaffold, config files.
        ├── spec-01-app-logic.md    [exists]  Sprint 1: pure-C modules with host unit tests.
        ├── spec-02-drivers.md      [exists]  Sprint 2: hardware bring-up and drivers.
        ├── spec-03-rtos-core.md    [exists]  Sprint 3: shared objects, tasks, sensing pipeline.
        ├── spec-04-display-button.md [exists]  Sprint 4: OLED task, button ISR and semaphore.
        ├── spec-05-connectivity.md [exists]  Sprint 5: Wi-Fi, SNTP, MQTT, configuration.
        ├── spec-06-reliability.md  [exists]  Sprint 6: monitor, recovery, watchdog, heap, LED, fault injection.
        ├── spec-07-verification.md [exists]  Sprint 7: timing, stack, fault and soak evidence.
        ├── spec-08-docs-acceptance.md [exists]  Sprint 8: documentation, demo, acceptance checks.
        ├── sprint-00-foundation.md [exists]  Sprint 0 task spec (per-task description, acceptance criteria, dependencies, effort).
        ├── sprint-01-pure-c-logic.md [exists]  Sprint 1 task spec.
        ├── sprint-02-hardware-bring-up.md [exists]  Sprint 2 task spec.
        ├── sprint-03-rtos-core.md  [exists]  Sprint 3 task spec.
        ├── sprint-04-display-button.md [exists]  Sprint 4 task spec.
        ├── sprint-05-connectivity.md [exists]  Sprint 5 task spec.
        ├── sprint-06-reliability.md [exists]  Sprint 6 task spec.
        ├── sprint-07-verification.md [exists]  Sprint 7 task spec.
        ├── sprint-08-documentation-acceptance.md [exists]  Sprint 8 task spec.
        ├── sprint-09-backlog.md    [exists]  Backlog (stretch) task spec. Placeholders, not scheduled.
        └── tasks/                  [exists]  One spec per roadmap task (129 files) in sprint-00/ to sprint-09/, named <task-id>.md, plus README.md as the index.
```

## Target structure

```
01-rtos-based-applications/
├── README.md                       [exists]
├── AGENTS.md                       [exists]
├── CLAUDE.md                       [exists]
├── CMakeLists.txt                  [planned]  ESP-IDF project entry point.
├── sdkconfig.defaults              [planned]  Defaults: FreeRTOS tick 1000 Hz, task watchdog on. No credentials.
├── Dockerfile.test                 [exists]   Lightweight host build/test image (Alpine + GCC).
├── requirements-dev.txt            [exists]
├── .dockerignore                   [exists]   Excludes build/, build-host/, managed_components/, sdkconfig, .venv/, graphify-out/.
├── .gitignore                      [exists]   Ignores build/, build-host/, managed_components/, sdkconfig, sdkconfig.old, .venv/, graphify-out/, Python caches, .claude/settings.local.json.
├── Makefile                        [exists]   `make test` (host), `make docker-test` (in container), `make clean`.
├── context/                        [exists]   See "Current state" for the file list.
├── main/                           [planned]  Firmware. Built only by the ESP-IDF toolchain.
│   ├── main.c                      Creates queues, mutexes, event group and tasks.
│   ├── app_config.h                Pins, periods, priorities, queue sizes.
│   ├── tasks/                      sensor, process, display, comms, monitor tasks.
│   └── drivers/                    bme280 and ssd1306 wrappers.
├── components/
│   └── app_logic/                  [planned]  Pure C, no ESP-IDF or FreeRTOS includes.
│       └── (moving_average, validate, dew_point)
├── test/
│   └── host/                       [exists]   Host unit tests for app_logic: test_<module>.c.
│       └── test_smoke.c            [exists]   TEMPORARY harness smoke test (s0-t4); deleted in s1-t18.
└── docs/                           [planned]  Wiring diagram, task diagram, test results, measured stack high-water marks.
```

## Where code is built

| Path | Test container (Alpine + GCC) | ESP-IDF toolchain |
|------|:----:|:----:|
| `components/app_logic/` | yes | yes |
| `test/host/` | yes | no |
| `main/` (tasks, drivers) | no | yes |

## Module boundaries

These follow the task and communication design in the overview.

- **`components/app_logic/`** depends only on the C standard library and `libm`. It never includes FreeRTOS or ESP-IDF headers, and it returns plain C results (not `esp_err_t`).
- **`main/drivers/`** (`bme280`, `ssd1306`) talk to the I2C bus through ESP-IDF. They do not take mutexes themselves: the calling task holds `i2c_mutex` around each transaction.
- **`main/tasks/`** may use `app_logic`, the drivers, `app_config.h`, and FreeRTOS/ESP-IDF. Tasks do not call each other. They communicate only through the shared objects in the overview (`raw_queue`, `publish_queue`, `error_queue`, `i2c_mutex`, `data_mutex`, `button_sem`, `sys_events`, and `latest` under `data_mutex`).
- **`main/main.c`** creates every shared object and task at startup.
- **`main/app_config.h`** is the single place for pins, periods, priorities, stack sizes, queue depths and timeouts.
- **`test/host/`** may include only `app_logic` headers.

Naming conventions are in [coding-standards.md](coding-standards.md) section 3.

## Generated and local-only (not tracked)

- `build/`: ESP-IDF build output.
- `build-host/`: host unit-test binaries from `make test`. Kept apart from `build/`.
- `managed_components/`: downloaded ESP-IDF components.
- `.venv/` and `graphify-out/`: graphify's environment and generated graph.
- `sdkconfig`, `sdkconfig.old`: generated by `menuconfig`. They can hold Wi-Fi credentials and must not be committed. Keep shared defaults in `sdkconfig.defaults`.

## Keeping this file current

Update it in the same change that adds, moves or removes a file or directory. The target structure here must stay consistent with the "Suggested Project Layout" in `project-overview.md` and `README.md`. Where this file adds entries the overview does not list (`context/`, `.gitignore`, `build-host/`, `AGENTS.md`, `CLAUDE.md`), they are additions, not conflicts.
