# Architecture

## Decision
Server-rendered monolithic Flask web application backed by SQLite. No separate frontend build step.

```mermaid
flowchart TD
  U[Browser] -->|HTTP / HTML forms| W[Flask + Jinja templates]
  W --> A[Flask-Login sessions + CSRF]
  W --> M[SQLAlchemy models]
  M --> D[(SQLite database)]
  D --> V[Docker named volume]
  G[GitHub push] --> C[GitHub Actions]
  C --> T[pytest + Docker build]
```

## Components
- Templates and CSS render responsive pages.
- Routes implement registration, login/logout, feed and posting.
- Flask-Login protects post creation; Werkzeug scrypt hashes credentials.
- SQLAlchemy persists User and Post entities in SQLite.
- Docker Compose maps localhost:8000 and mounts the named volume.

## Data model
User(id PK, username UNIQUE, password_hash); Post(id PK, author_id FK → User.id, body, created_at). One user has many posts.

## Trade-offs
A monolith is easy to run and debug but scales less flexibly than separated services. SQLite is sufficient for local MVP but less suitable for high-write concurrency. Production deployment requires hardened secret management, HTTPS, migrations and operational monitoring.
