from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import relationship, mapped_column

from app.core.database import Base
from app.infrastructure.db.models.base import BaseModel


class UserPreference(Base, BaseModel):

    __tablename__ = "user_preferences"

    user_id = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    preferred_genres = mapped_column(
        JSON,
        nullable=True,
    )

    favorite_authors = mapped_column(
        JSON,
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="preferences",
    )