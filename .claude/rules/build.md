## Build & Verification Policy (C, ESP-IDF, Docker)

The build specification is `context/code-build.md`. This file is the short version for agents. Run commands from PowerShell at the project root (Git Bash breaks Docker bind-mount paths, or set `MSYS_NO_PATHCONV=1`).

### Tiers

| Tier | When | Command |
|---|---|---|
| 1. Host unit tests | Every change to `components/app_logic/`, `test/host/`, `Makefile` or `Dockerfile.test`, and before any firmware build | `docker run --rm --memory 256m --cpus 1 -v "${PWD}:/work" rtos-host-test make test` |
| 2. Firmware build | Any change to `main/` or other firmware-side files | `docker run --rm --memory 2g --cpus 2 -v "${PWD}:/project" -w /project espressif/idf:v5.5.6 idf.py build` (first build in a fresh tree: `idf.py set-target esp32 build`) |
| 3. Hardware | Task, queue, timing or fault changes | Board only. Flash and monitor from the host: `idf.py -p COMx flash monitor` (not from Docker) |

### Rules

1. **Order**: run Tier 1 first. Do not build firmware while host tests fail.
2. **Warnings are errors** on the host (`-Wall -Wextra -Werror`). Firmware builds must add no new warnings.
3. **Pinned toolchain**: `espressif/idf:v5.5.6`, never `latest`. Always run it with `--memory 2g --cpus 2`.
4. **Hardware claims**: a passing Tier 1 or Tier 2 run does not verify hardware behaviour. The project has no board at present, so `[HW]` tasks are deferred and must not be reported as done.
5. **Secrets**: never in source, logs, tests, `sdkconfig.defaults` or commits. `sdkconfig` is git-ignored.
6. **Docs in sync**: when files are added, moved or removed, update `context/project-structure.md`. `README.md` and `context/project-overview.md` change together.
7. **Git scope**: always `git add` explicit paths inside this project, never `git add .` or `-A`. Never stage `build/`, `build-host/`, `managed_components/`, `sdkconfig`, `.venv/` or `graphify-out/`. Do not commit unless asked.

### Python (optional graphify tooling only)

Python is used only for the optional graphify knowledge graph (`context/code-build.md` section 9) and for the standard-library hook scripts.

- Run `python`, `pip` and `graphify` only through `.\.venv\Scripts\` (`python -m venv .venv` is the one allowed global use). The `guard-python-env.py` hook denies global use.
- Hook scripts in `.claude/hooks/` use only the standard library, so they run on any Python 3.10+ interpreter.
- Pin any package in `requirements-dev.txt`. Add one only when the current work needs it.
