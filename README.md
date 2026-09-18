# FastApi_Project

A small FastAPI project foundation with a health endpoint and tests.

## Project structure

```text
app/
  __init__.py
  main.py
tests/
  test_main.py
requirements.txt
requirements-dev.txt
.env.example
.gitignore
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

- `GET /` — basic status message
- `GET /health` — health check
- `/docs` — interactive Swagger UI

## Test

```bash
pytest
```
