from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import report_service
from schemas import ReportCategoryFilterSchema
from schemas.report import ReportCategorySchema, ReportTimeseriesFilterSchema, ReportTimeseriesSchema
from services import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/categories")
async def get_categories(
        report_category: Annotated[ReportCategoryFilterSchema, Depends()],
        report_service: Annotated[ReportService, Depends(report_service)],
) -> list[ReportCategorySchema]:
    report_categories = await report_service.get_categories(report_category)
    return report_categories


@router.get("/timeseries")
async def get_timeseries(
        report_timeseries: Annotated[ReportTimeseriesFilterSchema, Depends()],
        report_service: Annotated[ReportService, Depends(report_service)],
) -> list[ReportTimeseriesSchema]:
    report_timeseries = await report_service.get_timeseries(report_timeseries)
    return report_timeseries
