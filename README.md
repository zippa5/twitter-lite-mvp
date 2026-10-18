# Pulse — Twitter Lite MVP

A Flask social media application for a Software Engineering Workshop assessment.

## Features
- Register with a unique username and securely hashed password
- Log in and log out using session authentication
- Read the public newest-first feed with authors and timestamps
- Publish short posts (1–280 characters) while authenticated
- Persist users and posts in a Docker named volume

## Quick start (Windows PowerShell)
Install Docker Desktop with WSL 2 and Git for Windows. In PowerShell:

```powershell
git clone https://github.com/zippa5/twitter-lite-mvp.git
cd twitter-lite-mvp
docker compose up --build
```

Open **http://localhost:8000**. If the repo is already cloned, use `git pull` in its directory instead of cloning again.

To run in the background: `docker compose up -d --build`.
To stop without deleting data: `docker compose down`.
**Do not run `docker compose down -v` unless you intend to delete the database volume.**

## Automated tests
Using Python 3.12 in a local virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

GitHub Actions also runs pytest and builds the Docker image on pushes and pull requests. Inspect the [Actions page](https://github.com/zippa5/twitter-lite-mvp/actions) to confirm the latest run's result.

## Project and assessment artifacts
- [GitHub Kanban board](https://github.com/users/zippa5/projects/2/views/1)
- [GitHub Issues backlog](https://github.com/zippa5/twitter-lite-mvp/issues)
- [Requirements and acceptance criteria](docs/requirements.md)
- [Kanban methodology](docs/methodology.md)
- [Prioritized backlog](docs/backlog.md)
- [Architecture diagram](docs/architecture.md)
- [Architecture Decision Record](docs/adr-001.md)
- [Manual testing and evidence checklist](docs/testing.md)
- [Ten-minute presentation plan](docs/presentation.md)

## Technology
Python 3.12, Flask, Flask-Login, Flask-SQLAlchemy, SQLite, Gunicorn, Docker Compose, pytest, GitHub Actions.

## Configuration and limitations
Copy `.env.example` to `.env` and replace `SECRET_KEY` with a long, random secret. Never commit `.env`. The Compose fallback secret is only for a local classroom demo. Production would need HTTPS, stronger secret management, migrations, and operational monitoring. Likes, follows, direct messages and production hosting are out of scope.

## Academic integrity
AI-assisted code and documentation should be reviewed, understood, tested, and disclosed according to institutional policy.
