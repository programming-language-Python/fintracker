from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)


class Base(DeclarativeBase):
    pass
