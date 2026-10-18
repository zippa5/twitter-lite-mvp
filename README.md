# Pulse — Twitter Lite MVP

A Flask social media application for the Software Engineering Workshop assessment.

## Run with Docker

```bash
git clone https://github.com/zippa5/twitter-lite-mvp.git
cd twitter-lite-mvp
docker compose up --build
```

Open http://localhost:8000. Register, sign in, create posts, and view the feed. Data persists in the `social_data` Docker volume across restarts. Do not use `docker compose down -v` unless you intend to erase it.

## Stack
Python 3.12, Flask, Flask-Login, Flask-SQLAlchemy, SQLite, Gunicorn, Docker Compose, pytest, GitHub Actions.

## Tests
```bash
pip install -r requirements-dev.txt
pytest -q
```

## Configuration
Copy `.env.example` to `.env` and set a strong `SECRET_KEY`. Never commit `.env`. The Compose fallback key is for local demonstrations only.

See `docs/` for requirements, Kanban plan, architecture, ADR, backlog and presentation outline. No database migration is required for the initial MVP; tables are created at startup.

## Scope
Registration, login/logout, authenticated post creation (1–280 characters), chronological public feed, author and creation date. Likes, follows, messaging and production hosting are out of scope.

## Academic integrity
AI-assisted code and documentation should be reviewed, understood, tested and disclosed according to institutional policy.
