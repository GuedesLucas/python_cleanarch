# domain/interfaces/repositories.py
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.account import Account

class IAccountRepository(ABC):
    @abstractmethod
    def find_by_id(self, account_id: int) -> Optional[Account]: ...
    @abstractmethod
    def list_all(self) -> List[Account]: ...