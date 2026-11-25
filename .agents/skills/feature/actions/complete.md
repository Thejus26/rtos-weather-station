# Complete Action

`context/ai-interaction.md` says to ask before committing, before deleting a merged branch, and (as a remote action) before pushing. Ask at each marked step and wait for a yes. Running `/feature complete` does not answer those questions.

1. Check the quality gates for the change passed (`/feature test`). Show the file list and the proposed message, **ask for confirmation**, then stage and commit with a descriptive conventional commit message (per `context/ai-interaction.md`):
   - Stage by explicit path. The enclosing git repository may be rooted above this project, so never `git add .` or `-A` from a parent directory.
   - Stage only relevant source (`main/`, `components/`, `test/`), build and config files (`CMakeLists.txt`, `Makefile`, `Dockerfile.test`, `sdkconfig.defaults`, `Kconfig.projbuild`), and documentation.
   - Never stage `build/`, `build-host/`, `managed_components/`, `sdkconfig`, `sdkconfig.old`, `.venv/`, `.env`, `__pycache__/`, or `graphify-out/`.
2. Switch to `main` (or `master`) and merge the feature branch (no push yet):
   ```bash
   git checkout main
   git merge feature/<feature-slug>
   ```
3. **Ask for confirmation**, then delete the local feature branch:
   ```bash
   git branch -d feature/<feature-slug>
   ```
4. Reset `context/current-feature.md`:
   - Change H1 back to `# Current Feature`.
   - Clear Goals and Notes (keep the placeholder comments).
   - Add the feature summary to History (what changed, how it was verified, what was not verified on hardware, commit hash). Keep the 3-5 most recent entries and archive older ones to `context/feature-history.md`.
5. Commit the reset (it is part of the commit approved in step 1; ask again if the message or files changed): `chore: reset current-feature.md after completing [feature]`.
6. Optional, only if graphify is installed and C source changed: refresh the graph.
   ```powershell
   & .\.venv\Scripts\graphify.exe . --update --code-only
   ```
7. If an `origin` remote exists, **ask for confirmation**, then push main to origin ONCE (single push with all changes).
8. If the feature branch was previously pushed, **ask for confirmation**, then delete it from origin.
