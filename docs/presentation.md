# Pulse MVP — 10-minute assessment presentation

## Presentation run-of-show

| Time | Topic | What to demonstrate |
|---|---|---|
| 0:00–1:00 | Problem and scope | Pulse is a minimal public social feed; explain MVP exclusions |
| 1:00–2:00 | Requirements | Open [requirements](requirements.md); discuss FR-01 to FR-06 and measurable acceptance criteria |
| 2:00–3:00 | Kanban and backlog | Show [live board](https://github.com/users/zippa5/projects/2/views/1) and [nine issues](https://github.com/zippa5/twitter-lite-mvp/issues); explain WIP and Definition of Done |
| 3:00–4:00 | Architecture / ADR | Show [architecture](architecture.md) and [ADR-001](adr-001.md); explain Flask, SQLite and Docker volume trade-offs |
| 4:00–7:00 | Live product demonstration | Show anonymous feed, register new user, log out/in, reject wrong password, publish a post and see newest-first feed |
| 7:00–8:00 | Docker persistence | Show `docker compose ps`; demonstrate data after safe restart, without deleting volume |
| 8:00–9:00 | Tests and CI | Show `python -m pytest -q` and [Actions](https://github.com/zippa5/twitter-lite-mvp/actions) with actual run conclusion |
| 9:00–10:00 | Reflection | What worked, trade-offs, risks, future improvements and AI-assistance disclosure |

## Demo preparation
1. Open the Pulse site at http://localhost:8000 and the GitHub repository.
2. Confirm Docker Desktop is running; use `docker compose up -d --build` in the repository folder.
3. Prepare a unique demonstration username and password (at least 8 characters).
4. Verify that a successful CI run exists before saying CI passed.
5. Keep screenshots of the Kanban board, GitHub Actions result, test output, and the running application.
6. Rehearse with a timer; keep a fallback screenshot if the live demo has network or Docker issues.

## Evidence table
| Requirement area | Evidence |
|---|---|
| Requirements | `docs/requirements.md` |
| Methodology and backlog | `docs/methodology.md`, `docs/backlog.md`, issues #1–#9 |
| Project management | GitHub Project #2 and issue statuses |
| Architecture | Mermaid diagram and ADR-001 |
| Version control | Repository history and tracked files |
| MVP | Browser demonstration at localhost:8000 |
| Testing | `tests/test_app.py`, terminal pytest output |
| CI / Docker | Actions workflow conclusion, `compose.yaml`, named volume restart demonstration |

## Academic integrity
Review, understand, and be prepared to explain all submitted code and documentation. Disclose AI assistance in accordance with your institution's policy. Do not represent proposed checks as verified results.
