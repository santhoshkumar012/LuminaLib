from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.infrastructure.db.models.base import BaseModel


class Borrow(Base, BaseModel):

    __tablename__ = "borrows"

    user_id = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    book_id = mapped_column(
        ForeignKey("books.id"),
        nullable=False,
    )

    borrowed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    returned_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="borrows",
    )

    book = relationship(
        "Book",
        back_populates="borrows",
    )