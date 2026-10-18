# Requirements specification

## Scope and assumptions
- Web app, not mobile-native; English-language interface.
- Public feed is readable without signing in; only signed-in users publish.
- Unique case-sensitive usernames (3–30 ASCII letters/digits/underscores); passwords at least 8 characters.
- Posts contain 1–280 characters; latest 100 displayed, ordered by UTC timestamp then ID.
- No account verification, email, follows, likes, replies, image uploads, moderation, password recovery or production deployment in MVP.
- SQLite on a Docker named volume; removing the volume deletes demo data.

## Functional requirements
| ID | Requirement | Acceptance criterion |
|---|---|---|
| FR-01 | Register | Valid unique username and password create a user; duplicate/invalid inputs show errors. |
| FR-02 | Login | Valid credentials establish a session; invalid credentials do not. |
| FR-03 | Logout | Signed-in user can log out; subsequent protected requests redirect to login. |
| FR-04 | Create post | Authenticated user can submit 1–280 non-whitespace characters; post is persisted. |
| FR-05 | View feed | Visitors see all authors' posts, author username, text and UTC creation date, newest first. |
| FR-06 | Protect mutations | Anonymous post requests redirect to login; invalid CSRF tokens are rejected. |

## Non-functional requirements
| ID | Requirement | Verification |
|---|---|---|
| NFR-01 | Credential security | Password hashes use Werkzeug scrypt; no plain-text password stored. |
| NFR-02 | Persistence | Create user/post; recreate app or restart container without deleting volume; data remains. |
| NFR-03 | Reproducibility | `docker compose up --build` starts app on port 8000. |
| NFR-04 | Usability | Responsive interface works at mobile and desktop widths; labeled inputs and feedback. |
| NFR-05 | Quality | Pytest suite passes and CI installs, tests and builds on every push. |
| NFR-06 | Performance | Latest 100 posts displayed; feed queries use timestamp index; no formal load-test SLA claimed. |
| NFR-07 | Safe input | Posts HTML-escaped; max request size enforced; POST forms use CSRF tokens. |

## Traceability
FR-01/02/03 → Identity epic → `tests/test_app.py::test_registration_and_hash`, `test_login_logout`.
FR-04/05 → Posts epic → `test_posts_feed_order_and_validation`, `test_persistence_between_app_instances`.
FR-06/NFR-07 → Security epic → `test_csrf_protection`, `test_xss_is_escaped`.
NFR-03/05 → Delivery epic → Dockerfile, compose.yaml, CI workflow.
