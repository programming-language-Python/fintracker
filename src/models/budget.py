from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from models.base import intpk, created_at, updated_at
from schemas import BudgetSchema


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

    def to_read_model(self) -> BudgetSchema:
        return BudgetSchema(
            id=self.id,
            limit_amount=self.limit_amount,
            period_month=self.period_month,
            created_at=self.created_at,
            updated_at=self.updated_at,
            category_id=self.category_id
        )
