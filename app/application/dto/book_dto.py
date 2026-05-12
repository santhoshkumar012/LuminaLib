from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class BookResponse(BaseModel):

    id: UUID

    title: str

    author: str

    genre: str

    storage_path: str

    summary: str | None

    consensus_review: str | None

    created_at: datetime

    class Config:
        from_attributes = True