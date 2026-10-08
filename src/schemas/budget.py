from datetime import datetime, date

from pydantic import BaseModel


class BudgetCreateSchema(BaseModel):
    limit_amount: float
    period_month: date
    category_id: int | None


class BudgetSchema(BudgetCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
