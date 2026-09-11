import datetime

from pydantic import BaseModel


class BudgetAddDTO(BaseModel):
    limit_amount: float
    period_month: datetime.date


class BudgetDTO(BudgetAddDTO):
    id: int
