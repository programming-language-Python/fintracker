from sqlalchemy.orm import Mapped, relationship

from db.db import Base
from models.base import intpk, created_at, updated_at
from schemas import CategorySchema


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

    def to_read_model(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
