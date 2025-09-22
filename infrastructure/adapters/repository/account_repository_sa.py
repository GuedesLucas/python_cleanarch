# infrastructure/adapters/repository/account_repository_sa.py
from __future__ import annotations
from typing import Optional, List, Callable
from sqlalchemy import text
from sqlalchemy.orm import Session

from domain.entities.account import Account
from domain.interfaces.repositories import IAccountRepository

SessionFactory = Callable[[], Session]

class AccountRepositorySQLiteSA(IAccountRepository):
    def __init__(self, session_factory: SessionFactory):
        self._session_factory = session_factory

    def find_by_id(self, account_id: int) -> Optional[Account]:
        with self._session_factory() as session:
            row = session.execute(
                text("SELECT id, title, balance FROM accounts WHERE id = :id"),
                {"id": account_id},
            ).mappings().first()
            if not row:
                return None
            return Account(id=row["id"], title=row["title"], balance=row["balance"])

    def list_all(self) -> List[Account]:
        with self._session_factory() as session:
            rows = session.execute(
                text("SELECT id, title, balance FROM accounts ORDER BY id")
            ).mappings().all()
            return [Account(id=r["id"], title=r["title"], balance=r["balance"]) for r in rows]
