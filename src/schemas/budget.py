import datetime

from pydantic import BaseModel


class BudgetCreateSchema(BaseModel):
    limit_amount: float
    period_month: datetime.date


class BudgetSchema(BudgetCreateSchema):
    id: int
