# Start Action

1. Read `context/current-feature.md` and verify Goals are populated.
2. If empty, error: "Run /feature load first".
3. Confirm the build tooling is available: Docker is running (`docker version`) and the `rtos-host-test` image exists (`docker image ls rtos-host-test`). If not, build it: `docker build -f Dockerfile.test -t rtos-host-test .` (PowerShell, from the project root). The `.venv` is only needed for the optional graphify tool.
4. Set Status to "In Progress" in `context/current-feature.md`.
5. Create and check out the feature branch (derive the name from the H1 heading):
   ```bash
   git checkout -b feature/<feature-slug>
   ```
6. **Token-Frugal Implementation Rules**:
   - **Slice reading (max 100 lines)**: never `Read` a whole file over 100 lines. Find the line with `Grep` (or graphify `explain` if a graph exists), then use `offset` and `limit` (20-50 lines).
   - **Offload exploratory research**: if the work needs more than 3 files or pages of unfamiliar ESP-IDF, FreeRTOS or driver documentation, delegate to a subagent (`Explore` or `general-purpose`) and take back a concise summary.
   - **Incremental implementation**: list the goals, then implement one module at a time following `.claude/rules/c-standards.md` and `context/coding-standards.md`. Put decisions in `components/app_logic/` (pure C) with a host test written alongside it. Keep task code in `main/` thin.
   - **Keep docs in step**: when files are added, moved or removed, update `context/project-structure.md` in the same change.
