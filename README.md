# FastApi_Project

A small FastAPI backend built incrementally with SQLAlchemy, SQLite, Alembic, JWT authentication, tests, CI, and Docker.

## Architecture

![FastAPI Architecture](./docs/architecture.svg)

## Features

- FastAPI REST API
- SQLAlchemy database layer
- SQLite for local development
- Alembic database migrations
- User creation and search
- Duplicate-email validation
- Password hashing with Argon2
- JWT access-token authentication
- Isolated SQLite test database
- GitHub Actions CI
- Docker and Docker Compose

## Project structure

~~~text
app/
  core/
    config.py
  db/
    base.py
    database.py
  models/
    user.py
  routers/
    auth.py
    health.py
    users.py
  schemas/
    auth.py
    user.py
  services/
    auth.py
    user.py
  security.py
  main.py

alembic/
  versions/
tests/
  conftest.py
  test_main.py
  test_users.py
  test_auth.py
~~~

## Run locally

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
~~~

The API is available at http://127.0.0.1:8000 (version 0.5.0).

### Endpoints

- GET / — basic status
- GET /health — health check
- GET /users — list users, optionally filter with ?name=...
- GET /users/{user_id} — get a user
- POST /users — create a user
- POST /auth/register — register an authenticated user
- POST /auth/login — obtain a JWT
- GET /auth/me — get the authenticated user
- /docs — interactive Swagger UI

## Authentication

Register:

~~~json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "password": "correct-horse-battery"
}
~~~

Login with the same credentials at POST /auth/login, then send the returned token as:

~~~text
Authorization: Bearer <access_token>
~~~

Set a strong JWT_SECRET_KEY in .env for anything beyond local development.

## Database migrations

Create a new migration after changing SQLAlchemy models:

~~~bash
alembic revision --autogenerate -m "describe the change"
alembic upgrade head
~~~

Rollback one migration:

~~~bash
alembic downgrade -1
~~~

## Test

~~~bash
pytest
~~~

Tests use an isolated in-memory SQLite database and do not write to the application's app.db.

## Docker

~~~bash
docker compose up --build
~~~

The container runs database migrations before starting Uvicorn.
