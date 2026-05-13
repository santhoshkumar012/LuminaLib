from abc import ABC, abstractmethod

from app.infrastructure.db.models.book import Book


class BookRepository(ABC):

    @abstractmethod
    async def create_book(
        self,
        title: str,
        author: str,
        genre: str,
        storage_path: str,
    ) -> Book:
        pass

    @abstractmethod
    async def update_summary(
        self,
        book_id,
        summary: str,
    ):
        pass