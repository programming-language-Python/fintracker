from repositories import ReportRepository
from schemas import ReportCategoryFilterSchema
from schemas.report import ReportCategorySchema, ReportTimeseriesFilterSchema, ReportTimeseriesSchema


class ReportService:
    def __init__(self, repo: ReportRepository):
        self.repo: ReportRepository = repo()

    async def get_categories(self, report_category: ReportCategoryFilterSchema) -> list[ReportCategorySchema]:
        categories = await self.repo.get_categories(report_category)
        return categories

    async def get_timeseries(self, report_timeseries: ReportTimeseriesFilterSchema) -> list[ReportTimeseriesSchema]:
        categories = await self.repo.get_timeseries(report_timeseries)
        return categories
