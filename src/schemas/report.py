from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel


class ReportCategoryFilterSchema(BaseModel):
    from_: date
    to: date


class ReportCategorySchema(BaseModel):
    id: int
    name: str
    sum: float


class IntervalType(Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


class ReportTimeseriesFilterSchema(ReportCategoryFilterSchema):
    interval: IntervalType


class ReportTimeseriesSchema(BaseModel):
    bucket: datetime
    sum: float
