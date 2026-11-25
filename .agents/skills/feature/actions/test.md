# Test Action

Per `.agents/rules/build.md`. Run from PowerShell at the project root (Git Bash breaks Docker bind-mount paths).

1. Read `context/current-feature.md` to see what was implemented.
2. Identify which tier applies:
   - Changed `components/app_logic/`, `test/host/`, `Makefile` or `Dockerfile.test` (rebuild the image first if `Dockerfile.test` changed): Tier 1 is required.
   - Changed `main/`, `CMakeLists.txt`, `sdkconfig.defaults` or `Kconfig.projbuild`: Tier 2 is required.
   - Docs or tooling only: no build, but check `context/project-structure.md` against the files on disk.
3. Ensure new or modified logic has host tests in `test/host/test_<module>.c` covering normal, boundary and failure inputs (see `context/coding-standards.md` section 8). Do not define `NDEBUG`.
4. **Tier 1: host unit tests** (always first, under `-Wall -Wextra -Werror`):
   ```powershell
   docker run --rm --memory 256m --cpus 1 -v "${PWD}:/work" rtos-host-test make test
   ```
   One test: `docker run --rm -v "${PWD}:/work" rtos-host-test sh -c "make build-host/test_<module> && ./build-host/test_<module>"`.
5. **Tier 2: firmware build** (only after Tier 1 passes):
   ```powershell
   docker run --rm --memory 2g --cpus 2 -v "${PWD}:/project" -w /project espressif/idf:v5.5.6 idf.py build
   ```
   It must succeed with no new warnings. `idf.py size` reports the image size. In a fresh tree (no `build/` or `sdkconfig` yet), run `idf.py set-target esp32 build` once instead, as in `context/code-build.md` section 3. Do not repeat `set-target` on every build: it cleans the build directory and makes the next build a slow full rebuild.
6. Report the results per tier: command, exit code, warnings. State clearly which checks need the real board (timing, stack headroom, I2C, Wi-Fi, MQTT) and were **not** verified. Do not claim them as verified.
