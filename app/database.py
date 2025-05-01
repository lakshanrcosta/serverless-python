# File: app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.env import get_config

# Load and cache config
config = get_config()

# Extract database credentials
DB_USER = config("DB_USER", default="root")
DB_PASSWORD = config("DB_PASSWORD", default="root")
DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="3306")
DB_NAME = config("DB_NAME", default="todo_db")

# Construct full DB URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy engine setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
