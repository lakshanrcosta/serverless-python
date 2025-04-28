# File: app/main.py

from fastapi import FastAPI
from app.api import todo
from app.database import Base, engine

# Create all database tables (only first-time or dev mode)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Todo API",
    description="A FastAPI backend using clean architecture and MySQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Include all routers
app.include_router(todo.router, prefix="/todos", tags=["Todos"])
