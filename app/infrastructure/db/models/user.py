from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.infrastructure.db.models.base import BaseModel


class User(Base, BaseModel):

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    borrows = relationship("Borrow", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    preferences = relationship(
        "UserPreference",
        back_populates="user",
        uselist=False,
    )