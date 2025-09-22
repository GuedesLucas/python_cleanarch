from pydantic import BaseModel

class BalanceResponse(BaseModel):
    value: float