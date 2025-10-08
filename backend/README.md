# Cryptip Backend (FastAPI)

- Uses SQLAlchemy. Default DB: sqlite file `cryptip.db` for demo.
- To use PostgreSQL, set environment variable `DATABASE_URL=postgresql://user:pass@host:5432/dbname`.
- Run:
  - python -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt
  - cd app
  - uvicorn main:app --reload --port 8000
- Seed demo data: POST /sample/seed_demo
- Auth endpoints: /auth/register, /auth/login (OAuth2 password form)
- Protected endpoints require Bearer token