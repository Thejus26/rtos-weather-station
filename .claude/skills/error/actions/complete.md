# Complete Action

1. **Verify & Stage Changes**:
   - Verify the fix passes the gates through `.venv`:
     ```powershell
     .\.venv\Scripts\python.exe -m pytest -q
     .\.venv\Scripts\python.exe -m ruff check .
     ```
   - Stage ONLY the modified source files, tests, configs, and the error report, by explicit path (the enclosing git repository may be rooted above this project):
     ```bash
     git add <impacted-files> context/errors/
     ```
   - Ensure no `.venv/`, `.env`, `__pycache__/`, tool caches (`.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/`), or `graphify-out/` are staged.

2. **Commit the Fix**:
   - Commit using Conventional Commits format (per `context/ai-interaction.md`):
     ```bash
     git commit -m "fix(<module>): resolve ERR-{NNN} <short description>"
     ```

3. **Update Error Ledger with Commit SHA**:
   - Retrieve the commit SHA (`git rev-parse HEAD` and `git rev-parse --short HEAD`).
   - Update `context/errors/ERR-{NNN}-*.md`:
     - Set **Commit SHA** in the `## Metadata` table to `<short-sha>`. If `git remote get-url origin` returns a URL, make it a link: `[`<short-sha>`](<repo-url>/commit/<full-sha>)`.
   - Update `context/errors/README.md`:
     - Update the corresponding row in `## Chronological Index of Errors` with the same commit SHA.
   - Stage and record the ledger update:
     ```bash
     git add context/errors/
     git commit --amend --no-edit
     ```

4. **Merge to Base Branch**:
   - Determine the base branch (`main` or `master`).
   - Switch to the base branch:
     ```bash
     git checkout main
     ```
   - Merge the fix branch:
     ```bash
     git merge fix/ERR-{NNN}-{slug}
     ```

5. **Push to Remote** (only if an `origin` remote exists):
   - Push all changes to origin:
     ```bash
     git push origin main
     ```
   - If the fix branch was pushed to remote earlier, delete the remote branch:
     ```bash
     git push origin --delete fix/ERR-{NNN}-{slug}
     ```

6. **Clean Up Local Branch**:
   - Delete the merged local fix branch:
     ```bash
     git branch -d fix/ERR-{NNN}-{slug}
     ```

7. **Report Completion**:
   - Display a summary of the resolved error ID, commit SHA, merged branch, and updated error ledger status.
