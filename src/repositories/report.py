from sqlalchemy import select, and_, func
from sqlalchemy.orm import aliased

from db.db import async_session_maker
from models import Transaction, Category
from schemas import ReportCategoryFilterSchema
from schemas.report import ReportCategorySchema


class ReportRepository:
    async def get_categories(self, report_category: ReportCategoryFilterSchema) -> list[ReportCategorySchema]:
        async with async_session_maker() as session:
            t = aliased(Transaction)
            c = aliased(Category)
            query = (
                select(
                    c.id,
                    c.name,
                    func.sum(t.sum)
                )
                .select_from(t)
                .join(c, t.category_id == c.id)
                .filter(and_(
                    t.occurred_on >= report_category.from_,
                    t.occurred_on <= report_category.to
                ))
                .group_by(c.id, c.name)
            )
            res = await session.execute(query)
            return [
                ReportCategorySchema(id=r.id, name=r.name, sum=r.sum)
                for r in res.all()
            ]

    async def get_timeseries(self):
        pass
