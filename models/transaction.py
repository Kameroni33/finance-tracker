from pydantic import BaseModel

from models import Account, Category


class Transaction(BaseModel):
    id: int
    account_id: Account
    category_if: Category
    date: str
    description: str
    amount: float

