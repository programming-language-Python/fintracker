from datetime import datetime

from pydantic import BaseModel


class CategoryAddDTO(BaseModel):
    name: str


class CategoryDTO(CategoryAddDTO):
    id: int
    created_at: datetime
    updated_at: datetime


class CategoryRelDTO(CategoryAddDTO):
    budget: list["BudgetDTO"]
    transaction: list["TransactionDTO"]
