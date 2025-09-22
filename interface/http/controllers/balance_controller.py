# interface/http/controllers/balance_controller.py
import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.get_balance import BalanceUseCase, AccountNotFoundError
from interface.http.di import get_balance_uc

router = APIRouter()

@router.get("/balance/{account_id}", summary="Balance from account")
def get_balance(
    account_id: int,
    uc: Annotated[BalanceUseCase, Depends(get_balance_uc)],
):
    try:
        value = uc.balance(account_id)
        return {"value": value}
    except AccountNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal error")