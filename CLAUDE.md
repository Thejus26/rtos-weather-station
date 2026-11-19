# CLAUDE.md

@AGENTS.md

## Claude Code notes

- The project context lives in `AGENTS.md` (imported above). It is the shared file for all agents, so make project-wide changes there, not here.
- Before designing or changing behaviour, read `context/project-overview.md`. Use `context/project-structure.md` to see which files exist.
- The repository is at the specification stage. Do not describe planned files (Dockerfile, Makefile, `main/`, `components/`) as if they exist. Check first.
- Run host unit tests through Docker from PowerShell on this Windows machine, not Git Bash (path translation breaks bind mounts).
- Keep `README.md` and `context/project-overview.md` in sync when editing either.
- Do not commit unless asked. This directory's parent repository has many unrelated untracked files, so stage only paths inside this project.
