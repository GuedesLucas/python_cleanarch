# interface/http/deps.py
from typing import Annotated
from fastapi import Depends, Request
from application.use_cases.get_balance import BalanceUseCase
from domain.interfaces.repositories import IAccountRepository

def get_account_repo(request: Request) -> IAccountRepository:
    return request.app.state.account_repo

def get_balance_uc(
    repo: Annotated[IAccountRepository, Depends(get_account_repo)]
) -> BalanceUseCase:
    return BalanceUseCase(repo)