# Prioritized backlog / issue templates

These entries are ready to convert into GitHub Issues and add to a GitHub Project board. Initial status is **To Do** until work and evidence are reviewed; update statuses on the live board.

| ID | Epic | Story / task | Priority | Initial status | Acceptance criteria |
|---|---|---|---|---|---|
| US-01 | Foundation | As a developer, I want a reproducible repository so I can collaborate and deliver. | P0 | To Do | README, ignore rules and clean structure present. |
| US-02 | Identity | As a visitor, I want to register so I can publish. | P0 | To Do | Unique username; password hashed; invalid data rejected. |
| US-03 | Identity | As a member, I want to log in and out to protect my account. | P0 | To Do | Correct password grants session; logout clears it. |
| US-04 | Posts | As a member, I want to publish a post to share an update. | P0 | To Do | 1–280 chars; anonymous requests blocked; stored. |
| US-05 | Posts | As a visitor, I want to see posts from everyone to discover updates. | P0 | To Do | Author, text, UTC date; newest first. |
| US-06 | Persistence | As a member, I want my data retained after restarts. | P0 | To Do | Named volume retains users and posts. |
| US-07 | Delivery | As a lecturer, I want a one-command setup. | P0 | To Do | Compose build and run on port 8000. |
| US-08 | Quality | As a developer, I want tests and CI to catch regressions. | P0 | To Do | Tests and Docker build on every push. |
| US-09 | Documentation | As an assessor, I want requirements, architecture and ADR. | P0 | To Do | Docs linked from README; decision trade-offs recorded. |
| US-10 | Experience | As a user, I want a readable mobile layout. | P1 | To Do | Forms/feed usable on narrow screens. |
| US-11 | Extras | As a member, I want likes and follows. | P3 | Backlog | Deliberately excluded from MVP. |

Suggested GitHub issue labels: `epic:identity`, `epic:posts`, `epic:delivery`, `priority:P0`, `priority:P1`, `type:documentation`, `type:test`. Create project columns Backlog, To Do, In Progress, Review / Testing, Done. Keep evidence screenshots of board changes.
