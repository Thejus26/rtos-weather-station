# Load Action

1. Check `$ARGUMENTS` (after "load"):
   - If it is a path or filename: read that spec. Task specs live in `context/specs/tasks/sprint-NN/` and sprint specs in `context/specs/`.
   - If it is multiple words: use it as an inline feature description and generate goals.
   - If empty: error - "load" requires a spec file or feature description.

2. **Context discovery (token-frugal)**:
   - Read `context/project-overview.md` and `context/coding-standards.md` only for the sections the feature touches.
   - Check `context/project-structure.md` for which files exist (`[exists]`) and which are only planned.
   - If `graphify-out/graph.json` exists, use `& .\.venv\Scripts\graphify.exe query "<module>"` / `explain "<symbol>"` for callers and signatures instead of opening many files. If there is no graph, skip this.
   - If the task is marked `[HW]` in the roadmap and no board exists, say so and note it in Goals. Do not mark it done.

3. Update `context/current-feature.md`:
   - Update the H1 heading to include the feature name (for example `# Current Feature: s1-t3-dew-point`).
   - Compile a self-contained, actionable **Technical Brief** under `## Goals` and `## Notes`:
     - **Deliverables**: enumerated, with target file paths (`components/app_logic/...`, `main/...`, `test/host/...`).
     - **Key Signatures**: exact C function, struct and enum declarations, taken from the spec or existing headers.
     - **Errors**: the result enum values or `esp_err_t` codes involved, and how each fault is reported (`error_queue`, log, status LED).
     - **Interfaces**: queues, mutexes, semaphores, event bits, task priority and stack size from `main/app_config.h` and the overview.
     - **Test Scenarios**: concrete `test/host/test_<module>.c` cases (normal, boundary, failure inputs), plus the firmware and hardware checks that apply. Mark hardware checks as not verifiable on the host.
     - **Boundaries**: module boundaries (`app_logic` stays pure C), config values, and which docs to update (`project-structure.md`, README and overview in sync).
   - Set Status to `Not Started`.

4. Confirm the spec is loaded and display the feature summary.
