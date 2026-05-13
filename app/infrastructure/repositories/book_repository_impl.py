from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
    

    async def update_summary(
        self,
        book_id,
        summary: str,
    ):

        result = await self.db.execute(
            select(Book).where(Book.id == book_id)
        )

        book = result.scalar_one()

        book.summary = summary

        await self.db.commit()

        await self.db.refresh(book)

        return book