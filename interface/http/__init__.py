from fastapi import APIRouter
from interface.http.controllers.balance_controller import router as balance_router

def get_api_router() -> APIRouter:
    router = APIRouter()
    router.include_router(balance_router, prefix="/accounts", tags=["accounts"])
    return router