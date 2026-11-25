# Review Action

1. Read `context/current-feature.md` to understand the target deliverables and constraints.
2. Review the diff summary on the feature branch (`git diff main --stat`, or `master` if that is the base).
3. **Subagent delegation for the deep code audit (token preservation)**:
   - Offload line-by-line auditing to the `code-scanner` subagent (`.agents/agents/code-scanner/agent.md`). It runs in an isolated context, so the analysis does not fill the main conversation.
   - The subagent audits against `.agents/rules/c-standards.md` and `context/coding-standards.md`:
     - 🧱 Layering (`components/app_logic/` is pure C, no ESP-IDF or FreeRTOS includes)
     - 🔒 RTOS rules (no allocation in steady state, `FromISR` only in ISRs, one mutex at a time, `vTaskDelayUntil` for periodic work)
     - ⚠️ Fault handling (`ESP_ERROR_CHECK` only at startup, zero-timeout sends to `error_queue`, results checked, loops keep running)
     - 🔑 Secrets (no credentials, broker URLs or device IDs in source, logs or `sdkconfig.defaults`)
     - 🧪 Tests (normal, boundary and failure cases, no `NDEBUG`)
     - 🚫 Scope creep (Arduino framework, extra dependencies, features outside the overview)
   - The primary agent receives only the synthesized findings report.
4. Verify the quality gates in `context/code-build.md` section 6 (commands are in `.agents/rules/build.md`):
   - Host tests pass under `-Wall -Wextra -Werror` when `app_logic` or `test/host` changed.
   - The firmware build succeeds with no new warnings when `main/` or firmware files changed.
   - Hardware checks: list what needs the board and state that it was not verified.
   - Docs in sync: `context/project-structure.md` matches the files, and `README.md` agrees with `context/project-overview.md`.
5. Final verdict: **Ready to complete** or **Action items required**.
6. **Output format (chat only, do not save a report file)**: give the review in chat twice, in this order:
   - **Agent-friendly block**: one fenced block with the verdict, the counts, and the open findings. Give each finding a stable ID (keep IDs across rounds), a severity, and these labelled lines: `where` (`file:line`), `problem`, `scenario`, `fix`, `done_when` (the host test or build result that proves it is fixed). List deferred items with the subtask they move to.
   - **Prose summary**: a short human-readable summary of the verdict, what was fixed, the blockers and the recommendation.
