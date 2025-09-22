# 🏦 Bank API — Clean Architecture com FastAPI + SQLAlchemy

Este projeto é um exemplo de aplicação **Clean Architecture / Hexagonal** usando **FastAPI** como camada de interface, **SQLAlchemy** como infraestrutura de persistência, e entidades + use cases isolados no domínio.

---

## 📂 Estrutura do Projeto

```
.
├── app/
│   └── main.py                # App factory + lifespan (startup/shutdown)
├── domain/
│   ├── entities/
│   │   └── account.py         # Entidade de domínio
│   └── interfaces/
│       └── repositories.py    # Interface (contrato) de repositório
├── application/
│   └── use_cases/
│       └── get_balance.py     # Caso de uso: obter saldo da conta
├── infrastructure/
│   ├── adapters/
│   │   └── repository/
│   │       └── account_repository_sa.py  # Implementação do repo (SQLAlchemy)
│   ├── persistence/
│   │   ├── db.py              # Engine + Session factory
│   │   └── bootstrap.py       # Schema + seed do banco
│   └── logging/
│       └── logging_config.py  # Configuração de logs
└── interface/
    └── http/
        ├── controllers/
        │   └── balance_controller.py     # Rota /accounts/balance/{id}
        └── deps.py                       # Wiring de dependências
```

---

## 🚀 Como rodar

### 1. Criar e ativar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Subir a aplicação

```bash
uvicorn app.main:app --reload
```

Aplicação sobe em: [http://localhost:8000](http://localhost:8000)

---

## 🔍 Endpoints

### Healthcheck
```http
GET /health
```
Retorna `{"status": "ok"}`

### Consultar saldo
```http
GET /accounts/balance/{account_id}
```

**Exemplo:**

```http
GET /accounts/balance/1
```

**Resposta:**
```json
{
  "value": 100.0
}
```

---

## 🛠 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — camada de interface HTTP
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/) — ORM e queries SQL
- [SQLite](https://www.sqlite.org/) — banco de dados local
- [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) — separação de domínios, casos de uso e infraestrutura

---

## 📖 Notas de Arquitetura

- **Domain** não conhece infra, só contratos (`IAccountRepository`).
- **Application** (use cases) depende apenas de interfaces do domínio.
- **Infrastructure** implementa detalhes: SQLAlchemy, DB, logging.
- **Interface/Delivery** (FastAPI) injeta dependências via `Depends`.

---

## 📜 Licença

Projeto de estudo / portfólio — livre para uso e modificação.
