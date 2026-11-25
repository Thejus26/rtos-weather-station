# Skills

Custom skills and commands for the **RTOS weather station** (ESP32, ESP-IDF v5.x, FreeRTOS, C), built with Docker host tests and a containerised firmware build. Python is used only for the optional graphify tool and the hook scripts.

Each skill resides in its own subfolder with a `SKILL.md` instruction file:

- `feature/` - Full lifecycle workflow: load a roadmap task, start a feature branch, implement module by module, test (Tier 1 host tests, Tier 2 firmware build), review against `rules/c-standards.md`, explain, and complete.
- `research/` - Researches ESP-IDF, FreeRTOS, driver, MQTT or datasheet questions and writes the findings into `docs/` or `context/`.
- `cleanup/` - C housekeeping: debug prints, dead code, stale TODOs, orphaned files, layering and fault-handling rules, secrets, doc sync.
- `list-components/` - Lists the app_logic modules, tasks, shared RTOS objects, drivers, config and tests with a one-line description each.

The `/graphify` command (`../workflows/graphify.md`) refreshes the optional knowledge graph.
