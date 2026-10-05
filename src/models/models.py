from datetime import datetime, date
import enum
from typing import Annotated

from sqlalchemy import text, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base

metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
)]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.utcnow,
)]



class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[intpk]
    limit_amount: Mapped[float]
    period_month: Mapped[date]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    category_id: Mapped[int | None] = mapped_column(ForeignKey("category.id", ondelete="SET NULL"))
    category: Mapped[list["Category"]] = relationship(
        back_populates="budget"
    )


class Category(Base):
    __tablename__ = "category"

    id: Mapped[intpk]
    name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    budget: Mapped[list["Budget"]] = relationship(
        back_populates="category"
    )
    transaction: Mapped[list["Transaction"]] = relationship(
        back_populates="category"
    )


class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[intpk]
    type: Mapped[TransactionType]
    sum: Mapped[float]
    description: Mapped[str | None]
    occurred_on: Mapped[datetime]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"))
    category: Mapped[list["Category"]] = relationship(
        back_populates="transaction"
    )
