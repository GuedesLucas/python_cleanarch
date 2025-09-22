from fastapi import HTTPException
from domain.exceptions import AccountNotFoundError, DomainError

def present_balance(value: float):
    return {"value": value}

def map_exception(e: Exception) -> HTTPException:
    if isinstance(e, AccountNotFoundError):
        return HTTPException(status_code=404, detail=str(e))
    if isinstance(e, DomainError):
        return HTTPException(status_code=422, detail=str(e))
    return HTTPException(status_code=500, detail="Internal error")