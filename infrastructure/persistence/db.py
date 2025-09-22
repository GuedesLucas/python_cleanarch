# infrastructure/persistence/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def build_engine(db_url: str = "sqlite+pysqlite:///./dev.db", echo: bool = False):
    return create_engine(db_url, echo=echo, future=True)

def build_session_factory(engine):
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, expire_on_commit=False)
