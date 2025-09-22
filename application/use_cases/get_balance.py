from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from domain.exceptions import AccountNotFoundError
from domain.interfaces.repositories import IAccountRepository

class BalanceUseCase:
    def __init__(self, repo: IAccountRepository):
        self.repo = repo

    def balance(self, account_id: int) -> float:
        account = self.repo.find_by_id(account_id)
        if not account:
            raise AccountNotFoundError(f"Account {account_id} not found")
        return account.balance
