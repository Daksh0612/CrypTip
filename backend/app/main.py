# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, schemas, utils
from .routes import auth, addresses, export_routes, sample
from sqlalchemy.orm import Session
import uvicorn
from app import models, database, schemas, utils
from app.routes import auth, addresses, export_routes, sample


# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(title="Cryptip API - Demo")

# -----------------------------
# CORS Middleware
# -----------------------------
# Allows your React frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local dev, you can restrict to "http://127.0.0.1:5173"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Create Database Tables
# -----------------------------
models.Base.metadata.create_all(bind=database.engine)

# -----------------------------
# Include Routers
# -----------------------------
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(addresses.router, prefix="/addresses", tags=["addresses"])
app.include_router(export_routes.router, prefix="/export", tags=["export"])
app.include_router(sample.router, prefix="/sample", tags=["sample"])

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status":"ok"}

# -----------------------------
# Run backend
# -----------------------------
if __name__ == '__main__':
    # Use 127.0.0.1 instead of 0.0.0.0 to avoid firewall issues on Windows
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
