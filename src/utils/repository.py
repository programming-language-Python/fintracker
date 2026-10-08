from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db import get_session



class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create(self, data: dict) -> int:
        session = await get_session()
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await session.execute(stmt)
        await session.commit()
        return res.scalar_one()

    async def get(self):
        session = await get_session()
        stmt = select(self.model)
        res = await session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
