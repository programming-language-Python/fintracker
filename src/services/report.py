from repositories import ReportRepository
from schemas import ReportCategoryFilterSchema
from schemas.report import ReportCategorySchema


class ReportService:
    def __init__(self, repo: ReportRepository):
        self.repo: ReportRepository = repo()

    async def get_categories(self, report_category: ReportCategoryFilterSchema) -> list[ReportCategorySchema]:
        categories = await self.repo.get_categories(report_category)
        return categories

    async def get_timeseries(self):
        pass
