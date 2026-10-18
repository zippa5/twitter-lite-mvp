# Test plan and assessment evidence

## Automated verification
From the repository root on Windows PowerShell with Python 3.12:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Record the final number of tests passed, command output and date. The tests cover registration and password hashing, duplicate/invalid registration, correct/incorrect login, logout, guest restrictions, public feed, newest-first order, post validation, and CSRF protection.

## Manual acceptance test cases

| Test ID | Related requirement | Steps | Expected outcome |
|---|---|---|---|
| T-01 | FR-01 | Register a new valid username/password | User created and signed in |
| T-02 | FR-01 | Register an already-used username | Duplicate rejected |
| T-03 | FR-01 | Use a too-short password | Validation error; no account created |
| T-04 | FR-02 | Log out then log in with correct credentials | Authenticated session restored |
| T-05 | FR-02 | Attempt login with incorrect password | Rejected with error |
| T-06 | FR-03 | Click Log out | Username and post form disappear |
| T-07 | FR-04 | Open feed in private/incognito window | Posts visible without login; author and date displayed |
| T-08 | FR-04 | Create two posts sequentially | Most recent post appears first |
| T-09 | FR-05 | Publish a 1–280 character post | Post displayed in feed |
| T-10 | FR-05 | Submit empty or 281-character post | Rejected; no new post |
| T-11 | FR-05 | Attempt posting when signed out | Redirect to login or request rejected |
| T-12 | FR-06 | Create user and post, stop and restart Compose | Both still exist after restart |
| T-13 | NFR-04 | Run `docker compose up --build` | Application responds at localhost:8000 |
| T-14 | NFR-06 | Push a commit to GitHub | Actions job runs pytest and Docker build successfully |

## Persistence test — preserve your data
From the repository folder:

```powershell
docker compose down
docker compose up -d --build
docker compose ps
```

Refresh http://localhost:8000, log in using the same account, and verify the earlier post remains. **Never use `docker compose down -v` for this test**, as `-v` deletes the named database volume.

## CI verification
Open https://github.com/zippa5/twitter-lite-mvp/actions and select the latest **CI** run on the main branch. Confirm the steps **Install dependencies**, **Run tests**, and **Build Docker image** are green. Capture a screenshot of the successful run. A workflow file existing is **not** proof the workflow passed.

## Evidence record (fill with real observations)

| Test group | Actual result | Evidence location / screenshot | Date |
|---|---|---|---|
| Registration and password hashing | Not yet recorded | | |
| Login, incorrect password, logout | Not yet recorded | | |
| Post creation and chronological feed | Not yet recorded | | |
| Persistence after Compose restart | Not yet recorded | | |
| Automated pytest | Not yet recorded | | |
| GitHub Actions CI | Not yet recorded | | |
| Public Kanban board | Owner reported public; verify with anonymous browser | https://github.com/users/zippa5/projects/2/views/1 | |

When a test passes, update the matching issue and move its GitHub Project card to **Done**. Do not claim a pass based only on the presence of code.
