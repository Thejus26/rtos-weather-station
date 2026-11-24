# Current Feature: s0-t3-makefile

## Status
In Progress

## Goals
Spec: `context/specs/tasks/sprint-00/s0-t3-makefile.md` (Sprint 0, branch `chore/foundation`, size S, not `[HW]`). Requirement covered: **BLD-2** (`make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure).

**Deliverable**
1. `Makefile` at the project root, copied from the reference in `context/code-build.md` section 4. Targets: `test`, `docker-test`, `clean`.

**Reference content** (code-build.md section 4, verified in a scratch container on 2026-11-19):

```make
CC     ?= gcc
CFLAGS := -std=c11 -Wall -Wextra -Werror -O0 -g -Icomponents/app_logic
BUILD  := build-host
LOGIC  := $(wildcard components/app_logic/*.c)
TESTS  := $(wildcard test/host/test_*.c)
BINS   := $(patsubst test/host/%.c,$(BUILD)/%,$(TESTS))

.PHONY: test docker-test clean

test: $(BINS)
	@set -e; for t in $(BINS); do echo "== $$t"; $$t; done

$(BUILD)/%: test/host/%.c $(LOGIC) | $(BUILD)
	$(CC) $(CFLAGS) $^ -o $@ -lm

$(BUILD):
	mkdir -p $@

docker-test:
	docker build -f Dockerfile.test -t rtos-host-test .
	docker run --rm --memory 256m --cpus 1 -v "$(CURDIR):/work" rtos-host-test make test

clean:
	rm -rf $(BUILD)
```

**Acceptance criteria**
- [ ] `make` parses (check with `make -n test` in the container; a "missing separator" error means spaces were used instead of tabs).
- [ ] Targets match the reference (`test`, `docker-test`, `clean`, plus the `$(BUILD)` directory rule and the `$(BUILD)/%` pattern rule).

**Files touched**
- Add: `Makefile`.
- Update `context/project-structure.md` in the same change: move `Makefile` from `[planned]` to `[exists]`.

**Verification (host only, no hardware involved)**
- Parse check from PowerShell, because GNU make is not assumed on the Windows host: `docker run --rm -v "${PWD}:/work" rtos-host-test make -n test` (rebuild the image first if `rtos-host-test` is missing: `docker build -f Dockerfile.test -t rtos-host-test .`).
- `make test` with no test files must exit 0 (empty `BINS`, the loop body never runs). The real pass/fail check belongs to s0-t4 (harness smoke test), so do not add test files here.
- `make clean` leaves no `build-host/`.

## Notes
**Dependencies**
- Depends on `s0-t2-test-image` (done, commit `75dda2a`: `Dockerfile.test` is on `alpine:3.20` with `build-base`, `make`, `WORKDIR /work`).
- Blocks `s0-t4-harness-smoke-test`, which adds the first `test/host/test_*.c` and the first `components/app_logic/` source and runs the passing and failing assert checks.

**Constraints**
- Recipe lines start with a **tab**. Check after saving, since editors may convert tabs.
- Do **not** define `NDEBUG`: it turns `assert()` into a no-op and failing tests would pass silently.
- Host binaries go to `build-host/`, never `build/` (ESP-IDF owns that). Check that `.gitignore` or `.dockerignore` covers `build-host/` if either exists (`.dockerignore` was added in s0-t2).
- `components/app_logic/` stays pure C. The Makefile only builds `components/app_logic/*.c` and `test/host/test_*.c`. Nothing from `main/` builds here.
- The Makefile uses POSIX tools (`mkdir -p`, `rm -rf`, `for`). It targets the Alpine container, not native Windows. On this machine run `make test` through `docker run`, from PowerShell, not Git Bash (path translation breaks bind mounts).
- `docker-test` is a wrapper that runs `docker build` then `docker run` with `--memory 256m --cpus 1`. It is invoked from a host with `make` and Docker. The roadmap wins if this file and `spec-roadmap.md` disagree.

**Scope and claims**
- A parse check is all this task can prove. Do not claim `make test` passes real tests until s0-t4. The size and caps for `make test` under the container were deferred here from s0-t2 and complete in s0-t4.
- No hardware is involved. The owner is building code-only (see memory `no-hardware-code-only`).

**Open questions**
- None. One thing to watch: the Windows host likely has no GNU make, so `make docker-test` may only be runnable inside a container or WSL. Record the finding in the commit message or `README.md` Notes if confirmed.

## History
<!-- Append-only. Keep the 3-5 most recent completed features here; archive older ones to context/feature-history.md. -->
- **s0-t1-parts-and-hardware-check** (2026-11-24): parts checklist and I2C breakout notes added to README Notes. Acceptance criteria waived, not met: the owner is building code-only and will not buy hardware, so `[HW]` tasks and the Sprint 7 jitter measurement are deferred. Commit `6ec1ecc`.
- **s0-t2-test-image** (2026-11-24): added `Dockerfile.test` (alpine:3.20, build-base, make, WORKDIR /work) and `.dockerignore`. Build succeeds; image measured 230,623,533 bytes (~231 MB) on Docker 29.8.1, so the documented size was corrected from about 280 MB to about 230 MB across the docs. `make test` under the caps is deferred to s0-t3 and s0-t4. Commit `75dda2a`.
