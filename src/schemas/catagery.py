from datetime import datetime

from pydantic import BaseModel


class CategoryCreateSchema(BaseModel):
    name: str


class CategorySchema(CategoryCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CategoryRelSchema(CategoryCreateSchema):
    budget: list["BudgetSchema"]
    transaction: list["TransactionSchema"]
