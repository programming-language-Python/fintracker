from datetime import date

from pydantic import BaseModel


class ReportCategoryFilterSchema(BaseModel):
    from_: date
    to: date


class ReportCategorySchema(BaseModel):
    id: int
    name: str
    sum: float
