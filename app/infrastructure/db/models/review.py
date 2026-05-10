from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import mapped_column, relationship

from app.core.database import Base
from app.infrastructure.db.models.base import BaseModel


class Review(Base, BaseModel):

    __tablename__ = "reviews"

    user_id = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    book_id = mapped_column(
        ForeignKey("books.id"),
        nullable=False,
    )

    rating = mapped_column(
        Integer,
        nullable=False,
    )

    review_text = mapped_column(
        Text,
        nullable=False,
    )

    sentiment = mapped_column(
        Text,
        nullable=True,
    )

    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")