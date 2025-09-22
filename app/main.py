from contextlib import asynccontextmanager
from fastapi import FastAPI
from interface.http import get_api_router
from infrastructure.logging.logging_config import setup_logging
from infrastructure.persistence.db import build_engine, build_session_factory
from infrastructure.persistence.bootstrap import init_schema_and_seed
from infrastructure.adapters.repository.account_repository_sa import AccountRepositorySQLiteSA

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = build_engine("sqlite+pysqlite:///./dev.db")
    session_factory = build_session_factory(engine)
    init_schema_and_seed(session_factory)
    app.state.account_repo = AccountRepositorySQLiteSA(session_factory)
    yield
    engine.dispose()

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title="Bank API", lifespan=lifespan)
    app.include_router(get_api_router())
    return app

app = create_app()