# Current Feature

## Status
Not Started

## Goals
<!-- Populated by `/feature load <spec-name | description>` or by hand: deliverables with file paths, the requirement IDs covered (FR-n), key function and type signatures, the task/queue/mutex objects touched, host test scenarios, and hardware checks with pass criteria taken from the overview's timing table. -->

## Notes
<!-- Populated by `/feature load` or by hand: module boundaries (what may include what), config values from main/app_config.h (periods, priorities, stack sizes, queue depths, timeouts), the faults handled and their responses, open questions. -->

## History
<!-- Append-only. Keep the 3-5 most recent completed features here; archive older ones to context/feature-history.md. -->
- **s0-t2-test-image** (2026-11-24): added `Dockerfile.test` (alpine:3.20, build-base, make, WORKDIR /work) and `.dockerignore`. Build succeeds; image measured 230,623,533 bytes (~231 MB) on Docker 29.8.1, so the documented size was corrected from about 280 MB to about 230 MB across the docs. `make test` under the caps is deferred to s0-t3 and s0-t4. Commit `75dda2a`.
- **s0-t3-makefile** (2026-11-24): added a commented `Makefile` (`test`, `docker-test`, `clean`), identical to the `code-build.md` section 4 reference apart from comments. `make -n test`, `make test` (no test files yet, exit 0) and `make clean` verified in the container from PowerShell; `make docker-test` end to end not run (no GNU make on the Windows host). Known gap, deferred: headers in `components/app_logic/` are not prerequisites, so a header-only edit leaves stale test binaries until `make clean`. Pass/fail asserts are first exercised in s0-t4. Commit `e5440b1`.
- **s0-t4-harness-smoke-test** (2026-11-24): added temporary `test/host/test_smoke.c` (deleted in s1-t18). In the container under `--memory 256m --cpus 1`: a passing assert gives `make test` exit 0; a failing assert stops make with Error 134 (docker exit 2); caps confirmed via `docker inspect` and cgroup (memory.max 268435456, cpu.max 100000 100000); an unused variable fails the compile under `-Wall -Wextra -Werror`. `make docker-test` end to end not run (no GNU make on the Windows host). Header-prerequisite gap still deferred, to s1-t8. Commit `be699b6`.
- **s0-t5-install-esp-idf** (2026-11-24): container route chosen (no native install). `espressif/idf:v5.5.6` pulled; `idf.py --version` prints `ESP-IDF v5.5.6` (exit 0); image 9.22 GB on disk (~5 GB compressed); `i2c_master.h` present (D-4). Caps `--memory 2g --cpus 2` verified via `docker inspect` and cgroup, inside the existing 3 GB / 2 CPU Docker VM limit. Tag pinned in README, project-overview, code-build and AGENTS; decision and numbers in README Notes. Not measured: pull time and first firmware build (deferred to s0-t6 / s0-t7; the 2 GB cap is untested with a real build, exit 137 means raise it). Commit `e50cc1f`.
