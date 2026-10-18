# Requirements specification

## Assumptions
Web application; usernames are unique and case-sensitive; posts are public; no email verification; max 280 characters; local classroom demo rather than production service.

## Functional requirements
| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-01 | Register | Valid unique username (3–30 ASCII letters/digits/underscores) and password (8+ chars) create account; duplicates rejected |
| FR-02 | Login | Correct credentials establish authenticated session; incorrect credentials rejected |
| FR-03 | Logout | Authenticated user can terminate session |
| FR-04 | Feed | Everyone can view posts from all users with author, text, UTC date, newest first |
| FR-05 | Publish | Authenticated users can publish 1–280 characters; guests cannot |
| FR-06 | Persistence | Users and posts survive container restart with volume retained |

## Non-functional requirements
| ID | Requirement | Verification |
|---|---|---|
| NFR-01 | Security | Scrypt password hashes, session cookies, CSRF token and authenticated posting |
| NFR-02 | Usability | Responsive mobile and desktop layout; readable labels and errors |
| NFR-03 | Performance | Feed limited to newest 100 posts to bound page size |
| NFR-04 | Reproducibility | Docker Compose builds and starts on port 8000 |
| NFR-05 | Reliability | SQLite stored on named Docker volume |
| NFR-06 | Quality | Automated pytest tests and Docker build on pushes |

## Out of scope
Likes, follows, images, notifications, moderation, password reset, email verification, production scaling.
