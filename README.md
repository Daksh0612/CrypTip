# Cryptip — SIH Demo Project

This repository contains a demo implementation of **Cryptip**: a web-based system to collect, verify, categorize, and manage cryptocurrency wallet addresses for analysis and research.

## Structure
- backend/ : FastAPI backend (SQLAlchemy). Default DB: sqlite (cryptip.db)
- frontend/ : React + Vite SPA
- To run locally: see backend/README.md and frontend instructions below.

## Quick start (demo)
1. Backend:
   - cd backend
   - python -m venv venv
   - source venv/bin/activate   (or venv\\Scripts\\activate on Windows)
   - pip install -r requirements.txt
   - cd app
   - uvicorn main:app --reload --port 8000
   - Optional: POST /sample/seed_demo to create admin and sample addresses
2. Frontend:
   - cd frontend
   - npm install
   - npm run dev (Vite runs on port 3000)
   - Open http://localhost:3000
3. Default API base in frontend .env is http://localhost:8000