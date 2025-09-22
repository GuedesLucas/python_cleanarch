# infrastructure/persistence/bootstrap.py
from sqlalchemy import text
from sqlalchemy.orm import Session

DDL_ACCOUNTS = """
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    balance REAL NOT NULL
)
"""

SEED_ACCOUNTS = """
INSERT INTO accounts (id, title, balance) VALUES
(1, 'Conta Seu Raul', 100.00),
(2, 'Conta Dona Rita', 2500.50),
(3, 'Conta John', 750.25),
(4, 'Conta Ferumbras', 15000.00),
(5, 'Conta Loranlor', 42.42)
"""

def init_schema_and_seed(session_factory) -> None:
    # roda uma transação única
    with session_factory() as session:  # type: Session
        session.execute(text(DDL_ACCOUNTS))
        # seed idempotente
        count = session.execute(text("SELECT COUNT(*) FROM accounts")).scalar_one()
        if count == 0:
            session.execute(text(SEED_ACCOUNTS))
        session.commit()
