from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.infrastructure.db.models.base import BaseModel


class Book(Base, BaseModel):

    __tablename__ = "books"

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    author: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    genre: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    storage_path: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    summary: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    consensus_review: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    borrows = relationship("Borrow", back_populates="book")
    reviews = relationship("Review", back_populates="book")