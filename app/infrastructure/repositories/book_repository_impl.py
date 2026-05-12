from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.book import Book

from app.domain.repositories.book_repository import (
    BookRepository,
)


class BookRepositoryImpl(BookRepository):

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create_book(
        self,
        title: str,
        author: str,
        genre: str,
        storage_path: str,
    ) -> Book:

        book = Book(
            title=title,
            author=author,
            genre=genre,
            storage_path=storage_path,
        )

        self.db.add(book)

        await self.db.commit()

        await self.db.refresh(book)

        return book