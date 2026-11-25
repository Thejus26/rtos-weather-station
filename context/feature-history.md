# Feature Execution History Archive

Chronological archive (oldest to newest) of completed features for project 01, the RTOS weather station (ESP32, FreeRTOS). Older entries move here from `context/current-feature.md` when a feature is completed.

## History
- **s0-t1-parts-and-hardware-check** (2026-11-24): parts checklist and I2C breakout notes added to README Notes. Acceptance criteria waived, not met: the owner is building code-only and will not buy hardware, so `[HW]` tasks and the Sprint 7 jitter measurement are deferred. Commit `6ec1ecc`.
- **s0-t2-test-image** (2026-11-24): added `Dockerfile.test` (alpine:3.20, build-base, make, WORKDIR /work) and `.dockerignore`. Build succeeds; image measured 230,623,533 bytes (~231 MB) on Docker 29.8.1, so the documented size was corrected from about 280 MB to about 230 MB across the docs. `make test` under the caps is deferred to s0-t3 and s0-t4. Commit `75dda2a`.
- **s0-t3-makefile** (2026-11-24): added a commented `Makefile` (`test`, `docker-test`, `clean`), identical to the `code-build.md` section 4 reference apart from comments. `make -n test`, `make test` (no test files yet, exit 0) and `make clean` verified in the container from PowerShell; `make docker-test` end to end not run (no GNU make on the Windows host). Known gap, deferred: headers in `components/app_logic/` are not prerequisites, so a header-only edit leaves stale test binaries until `make clean`. Pass/fail asserts are first exercised in s0-t4. Commit `e5440b1`.
