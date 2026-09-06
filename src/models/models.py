import datetime
import enum
from typing import Annotated

from sqlalchemy import text, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base

metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_defaults=text("TIMEZONE('utc', now())"),
)]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_defaults=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow,
)]


class BudgetOrm(Base):
    __tablename__ = "budget"

    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    category_id: Mapped[int | None] = mapped_column(ForeignKey("category.id", ondelete="SET NULL"))
    category: Mapped[list["CategoryOrm"]] = relationship(
        # конкретно указали ссылку на таблицу
        back_populates="budget"
    )


class CategoryType(enum.Enum):
    income = "income"
    expense = "expense"


class CategoryOrm(Base):
    __tablename__ = "category"

    id: Mapped[intpk]
    name: Mapped[str]
    type: Mapped[CategoryType]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    budget: Mapped[list["BudgetOrm"]] = relationship(
        back_populates="category"
    )


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[intpk]
    sum: Mapped[float]
    description: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
