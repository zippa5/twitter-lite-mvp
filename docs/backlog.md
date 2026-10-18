# Prioritized product backlog

The authoritative **live status** is on the [GitHub Kanban board](https://github.com/users/zippa5/projects/2/views/1). The table below is a **recommended triage snapshot**; updating this Markdown file does not move a GitHub Project card.

| ID | GitHub Issue | User story / engineering task | Priority | Recommended board status | Definition of acceptance |
|---|---|---|---|---|---|
| US-01 | [#1](https://github.com/zippa5/twitter-lite-mvp/issues/1) | As a visitor, I can register to participate | Must | In review | Unique username, validation, scrypt password hash, duplicates rejected |
| US-02 | [#2](https://github.com/zippa5/twitter-lite-mvp/issues/2) | As a user, I can log in and out securely | Must | In review | Valid login, invalid login rejected, logout ends session |
| US-03 | [#3](https://github.com/zippa5/twitter-lite-mvp/issues/3) | As a visitor, I can read the public feed | Must | In review | Author, text, UTC timestamp, newest-first ordering |
| US-04 | [#4](https://github.com/zippa5/twitter-lite-mvp/issues/4) | As a user, I can publish a short post | Must | In progress | Login required, 1–280 characters, saved and shown |
| ENG-01 | [#5](https://github.com/zippa5/twitter-lite-mvp/issues/5) | Reproducible Docker and persistent database | Must | In progress | Compose starts; users and posts survive restart |
| ENG-02 | [#6](https://github.com/zippa5/twitter-lite-mvp/issues/6) | Automated tests and CI | Must | In progress | Push runs pytest and Docker build; green workflow verified |
| ENG-03 | [#7](https://github.com/zippa5/twitter-lite-mvp/issues/7) | Requirements, architecture and ADR | Must | In review | Complete docs and coherent architecture decision |
| ENG-04 | [#8](https://github.com/zippa5/twitter-lite-mvp/issues/8) | Kanban project board | Must | Ready | Publicly accessible board; issues distributed by actual status |
| ENG-05 | [#9](https://github.com/zippa5/twitter-lite-mvp/issues/9) | Ten-minute assessment presentation | Must | Backlog | Timed walkthrough, demo and evidence captured |

## Definition of Done
1. Acceptance criteria are satisfied.
2. Appropriate automated and/or manual test evidence is recorded.
3. Relevant changes are committed to GitHub.
4. Issue is updated and moved to **Done** on the GitHub Project board.
5. Presentation evidence is available where applicable.

## Traceability
- Requirements: [requirements.md](requirements.md)
- Architecture and decision: [architecture.md](architecture.md), [adr-001.md](adr-001.md)
- Verification: [testing.md](testing.md)
- Delivery: [GitHub Actions](https://github.com/zippa5/twitter-lite-mvp/actions)

**Note:** Recommended statuses are not verified live board statuses or claims that tests have passed.
