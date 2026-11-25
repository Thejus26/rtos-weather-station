---
name: cleanup
description: Clean up C/ESP-IDF codebase housekeeping tasks (add "run" to execute fixes)
argument-hint: run|check
---

Review the codebase and project context for cleanup tasks:

1. **Feature Tracker Order**: Verify that the history in `context/current-feature.md` is strictly in chronological order (oldest to newest).
2. **Debug Output**: Find leftover `printf`, `puts` and ad-hoc debug prints in `main/` and `components/` (use `ESP_LOGx` in firmware), and logging inside ISRs or while holding a mutex.
3. **Dead Code**: Find unused functions, `static` helpers, macros in `main/app_config.h`, and headers that nothing includes.
4. **Stale TODOs**: Identify unresolved `TODO`, `FIXME`, or `HACK` comments.
5. **Orphaned Files**: Find source files not listed in a `CMakeLists.txt`, test files with no matching module, and stray scratch files.
6. **Context Alignment**: Verify that `context/project-structure.md` matches the files on disk (`[exists]` vs `[planned]`), `README.md` and `context/project-overview.md` agree, and no document still describes another stack.
7. **Layering Audit**: Find ESP-IDF or FreeRTOS includes in `components/app_logic/`, and `FromISR` calls outside an ISR (or non-`FromISR` calls inside one).
8. **Fault-Handling Audit**: Find `ESP_ERROR_CHECK` in steady-state paths, unchecked results from `xQueueSend` / `xSemaphoreTake` / I2C calls, sends to `error_queue` with a non-zero timeout, and `malloc` / `free` outside startup.
9. **Secrets Audit**: Find hard-coded Wi-Fi credentials, broker URLs or device IDs in source or `sdkconfig.defaults`, and check that `sdkconfig` is in `.gitignore`.
10. **Conventions**: Pins, periods, priorities and queue sizes belong in `main/app_config.h`. Flag magic numbers in task code and public functions without a module prefix.

**Mode: $ARGUMENTS**

If no argument or argument is "check":
- Only report findings with line numbers and file paths; do not modify any files.
- Categorize what WOULD be cleaned up.

If the argument is "run" or "fix":
- First, report all findings in a numbered list.
- Then ask: "Which items would you like me to fix? (enter numbers like 1,3,5 or 'all' or 'none')"
- Wait for user response before making any changes.
- Only modify the specific items requested by the user.
- Summarize all completed fixes clearly.
