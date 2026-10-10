from sqlalchemy import select

from db.db import async_session_maker
from models import Transaction
from schemas import TransactionFilterSchema, TransactionSchema
from utils.repository import SQLAlchemyRepository


class TransactionRepository(SQLAlchemyRepository):
    model = Transaction

    async def get(self, transaction_filter: TransactionFilterSchema) -> list[TransactionSchema]:
        filters = []
        if transaction_filter.type is not None:
            filters.append(self.model.type == transaction_filter.type)
        if transaction_filter.from_ is not None:
            filters.append(self.model.occurred_on >= transaction_filter.from_)
        if transaction_filter.to is not None:
            filters.append(self.model.occurred_on <= transaction_filter.to)
        if transaction_filter.category_id is not None:
            filters.append(self.model.category_id == transaction_filter.category_id)

        async with async_session_maker() as session:
            stmt = select(self.model).filter(*filters)
            res = await session.execute(stmt)
            return [row[0].to_read_model() for row in res.all()]

    async def update(self, transaction_id: int):
        pass
