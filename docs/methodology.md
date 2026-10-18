# Development methodology — Kanban

## Rationale
Kanban was selected for this small Software Engineering Workshop MVP because it supports continuous delivery, visible priorities, and a short deadline without requiring fixed-length Scrum sprints. Requirements and implementation evidence can be reviewed incrementally.

## Actual GitHub Project
- [Pulse MVP – Software Engineering Kanban](https://github.com/users/zippa5/projects/2/views/1)
- [GitHub Issues backlog](https://github.com/zippa5/twitter-lite-mvp/issues)
- Repository: [zippa5/twitter-lite-mvp](https://github.com/zippa5/twitter-lite-mvp)

The project was created and its nine repository issues were added. Project visibility was reported as public by the owner; viewers should verify access using the link.

## Workflow and policies
The board uses **Backlog → Ready → In progress → In review → Done**.

- **Backlog:** identified but not yet scheduled.
- **Ready:** requirements and acceptance criteria understood; available to start.
- **In progress:** implementation or active investigation underway.
- **In review:** code/docs implemented, awaiting acceptance checks or evidence.
- **Done:** acceptance criteria verified; tests and evidence recorded.

Use a work-in-progress limit of **3** for In progress, and avoid exceeding it. Move issues based on real progress rather than closing them simply because code exists. Record a test result, commit, or screenshot as evidence when completing an issue.

## Prioritization
All nine core assessment items are **Must** for submission. Implement and verify authentication and posting first, followed by persistence and CI, then assessment documentation and presentation. See [prioritized backlog](backlog.md).

## Process evidence
Issues #1–#9 contain acceptance criteria. The board records their current status; [testing checklist](testing.md) records verification steps. Screenshots of the project board, running app, and successful Actions run should be included in the final assessment.

## Limitations
The written backlog is a planning snapshot, not a live feed of GitHub Project statuses. Refer to the board for current state. Do not mark CI, database restart persistence, or all acceptance criteria as passed until demonstrated.
