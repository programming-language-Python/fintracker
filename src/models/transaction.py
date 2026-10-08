from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from enums import TransactionType
from models.base import intpk, created_at, updated_at
from schemas import TransactionSchema


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

    def to_read_model(self) -> TransactionSchema:
        return TransactionSchema(
            id=self.id,
            type=self.type,
            sum=self.sum,
            description=self.description,
            occurred_on=self.occurred_on,
            created_at=self.created_at,
            updated_at=self.updated_at,
            category_id=self.category_id
        )
