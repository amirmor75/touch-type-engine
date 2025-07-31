import os
from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL")  # .env is loaded in main.py

engine = create_engine(
    DATABASE_URL,
    connect_args={}
)
class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    actual_tables = inspector.get_table_names()
    print(f"Actual tables in DB: {actual_tables}")

    required = {"drills", "sessions"}
    missing = required - set(actual_tables)
    if missing:
        raise RuntimeError(f"Missing DB tables: {missing}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
