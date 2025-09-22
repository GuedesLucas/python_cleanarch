from fastapi import APIRouter
from .controllers.balance_controller import router as balance_router

def get_api_router() -> APIRouter:
    api = APIRouter()
    api.include_router(balance_router)
    return api