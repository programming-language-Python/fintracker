from datetime import datetime

from pydantic import BaseModel

from enums import TransactionType


class TransactionCreateSchema(BaseModel):
    type: TransactionType
    sum: float
    description: str | None
    occurred_on: datetime
    category_id: int


class TransactionSchema(TransactionCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TransactionRelSchema(TransactionCreateSchema):
    category: list["CategorySchema"]
