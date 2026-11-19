# Complete Action

1. Stage all changes and commit with a descriptive conventional commit message (per `context/ai-interaction.md`):
   - Stage by explicit path. The enclosing git repository may be rooted above this project, so never `git add .` or `-A` from a parent directory.
   - Only stage relevant Python source, `requirements*.txt`, config files, tests, and documentation.
   - Never stage `.venv/`, `.env`, `__pycache__/`, tool caches (`.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/`), or `graphify-out/`.
2. Switch to `main` (or `master`) and merge the feature branch (no push yet):
   ```bash
   git checkout main
   git merge feature/<feature-slug>
   ```
3. Delete the local feature branch:
   ```bash
   git branch -d feature/<feature-slug>
   ```
4. Reset `context/current-feature.md`:
   - Change H1 back to `# Current Feature`
   - Clear Goals and Notes sections (keep placeholder comments)
   - Add the feature summary to History; keep `current-feature.md` lean by retaining the 3–5 most recent features and archiving older entries to `context/feature-history.md`
5. Commit the reset: `chore: reset current-feature.md after completing [feature]`
6. Update the graphify knowledge graph incrementally:
   ```powershell
   & .\.venv\Scripts\graphify.exe . --update --code-only
   ```
7. If an `origin` remote exists, push main to origin ONCE (single push with all changes)
8. If the feature branch was previously pushed, delete it from origin
