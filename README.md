# Pulse — Twitter Lite Social Media MVP

A responsive, server-rendered social media MVP for the Software Engineering Workshop. Users register, sign in/out, create short posts and read a public feed ordered newest first. Users and posts persist in SQLite on a Docker named volume.

## Quick start (Docker)

Prerequisite: Docker Desktop or Docker Engine with Compose plugin.

```bash
git clone <YOUR-REPOSITORY-URL>
cd twitter-lite-mvp
docker compose up --build
```

Open **http://localhost:8000**. No migration or seed step required; database tables are created on first boot. For a stronger local session secret, copy `.env.example` to `.env` and replace `SECRET_KEY` with a long random string. The default Compose secret is **only for local classroom demonstrations**, not public deployment. Never commit `.env`.

Stop with `Ctrl+C`, or `docker compose down`. Restart with `docker compose up --build`: posts remain. **Do not use `docker compose down -v`**, which deletes the named data volume.

## Features
- Register with a unique username and password (minimum 8 characters, stored as a scrypt hash).
- Log in and log out using cookie sessions.
- Publish 1–280-character posts when authenticated.
- Public feed shows up to 100 newest posts with author and UTC date.
- Responsive desktop/mobile UI; CSRF protection and HTML escaping.

## Local development and tests

Requires Python 3.12+.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest -q
```

For a local non-Docker run, set `DATABASE_URL` to a writable SQLite path and `SECRET_KEY` to a random value, then run `python run.py`. For example on macOS/Linux:

```bash
mkdir -p data
export DATABASE_URL=sqlite:///data/social.db
export SECRET_KEY=local-development-only-replace-me
python run.py
```

## Configuration
| Variable | Example | Purpose |
|---|---|---|
| `DATABASE_URL` | `sqlite:////data/social.db` | SQLite file in Docker named volume |
| `SECRET_KEY` | long random secret | Signs user sessions; replace local fallback before deployment |
| Port | `8000` | Browser URL http://localhost:8000 |

## Continuous integration
`.github/workflows/ci.yml` runs on every push and pull request: install Python dependencies → run pytest → build Docker image. Confirm the **actual** run is green in the GitHub Actions tab; a workflow file alone is not proof of success.

## Engineering deliverables
- [Requirements & acceptance criteria](docs/requirements.md)
- [Kanban methodology](docs/methodology.md)
- [Prioritized backlog & board setup](docs/backlog.md)
- [Architecture diagram & data model](docs/architecture.md)
- [ADR-001: architecture decision](docs/adr-001.md)
- [10-minute presentation plan](docs/presentation.md)

## Troubleshooting
- Port 8000 occupied: change `8000:8000` to `8001:8000` in Compose and open port 8001.
- Docker not running: start Docker Desktop and retry.
- Data missing: check whether the named volume was removed with `down -v`.
- Changed secret: previous sessions are invalidated; log in again.
- Failed CI: inspect Actions logs, run `python -m pytest -q` and `docker build -t pulse .` locally.

## Deliberately excluded
Likes, follows, replies, media uploads, search, email verification, password reset, moderation and production deployment. The project is a local demonstration, not a production-hardened social network. Additional work would include TLS, rate limiting, production session-secret management, migrations, accessibility audit and load testing.

## Academic integrity
This starter implementation and supporting documentation were prepared with AI assistance. Students should inspect, test, understand, adapt and disclose assistance according to their institution's academic integrity policy. Record actual personal contributions, board activity, test evidence and CI results.
