# Host (Tier 1) unit-test build for the RTOS weather station.
#
# Scope: only components/app_logic/ (pure C, no ESP-IDF or FreeRTOS includes)
# and test/host/ build here. Firmware in main/ needs ESP-IDF and is built with
# `idf.py build`, not this Makefile (see context/code-build.md sections 4-5).
#
# Targets:
#   make test         build and run every test/host/test_*.c on this machine
#   make docker-test  same, inside the Alpine + GCC container (Dockerfile.test)
#   make clean        delete the host build output
#
# On Windows, run `make test` through Docker from PowerShell, not Git Bash
# (path translation breaks bind mounts).
#
# Recipe lines MUST start with a tab, not spaces.

# C compiler. `?=` lets the caller override it, e.g. `make CC=clang`.
CC     ?= gcc

# -Wall -Wextra -Werror: any warning fails the build (requirement BLD-2).
# -O0 -g: no optimisation, with debug info, for readable failures.
# Do NOT add -DNDEBUG: it turns assert() into a no-op, so failing tests
# would pass silently.
CFLAGS := -std=c11 -Wall -Wextra -Werror -O0 -g -Icomponents/app_logic

# Host binaries go here, never into ESP-IDF's build/ directory.
BUILD  := build-host

# Pure-C sources under test, linked into every test binary.
LOGIC  := $(wildcard components/app_logic/*.c)

# One test file per module: test/host/test_<module>.c, each with its own main().
TESTS  := $(wildcard test/host/test_*.c)

# test/host/test_foo.c -> build-host/test_foo
BINS   := $(patsubst test/host/%.c,$(BUILD)/%,$(TESTS))

.PHONY: test docker-test clean

# Build all test binaries, then run them one by one. `set -e` stops at the
# first non-zero exit, so a failed assert() fails the whole make run.
test: $(BINS)
	@set -e; for t in $(BINS); do echo "== $$t"; $$t; done

# Build one test binary from its test file plus all app_logic sources.
# $^ is every normal prerequisite (the order-only $(BUILD) is excluded).
# -lm links the math library for logic such as dew point.
$(BUILD)/%: test/host/%.c $(LOGIC) | $(BUILD)
	$(CC) $(CFLAGS) $^ -o $@ -lm

# Order-only prerequisite above: create the output directory once, without
# rebuilding every binary when its timestamp changes.
$(BUILD):
	mkdir -p $@

# Run `make test` in the lightweight container, with the same resource caps
# every time. Needs Docker. $(CURDIR) is the project root, mounted at /work.
docker-test:
	docker build -f Dockerfile.test -t rtos-host-test .
	docker run --rm --memory 256m --cpus 1 -v "$(CURDIR):/work" rtos-host-test make test

# Remove host build output only.
clean:
	rm -rf $(BUILD)
