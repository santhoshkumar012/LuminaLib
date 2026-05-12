from uuid import uuid4

from fastapi import UploadFile, HTTPException, status

from app.domain.interfaces.storage_interface import (
    StorageInterface,
)

from app.domain.repositories.book_repository import (
    BookRepository,
)


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
}


class BookService:

    def __init__(
        self,
        storage: StorageInterface,
        repository: BookRepository,
    ):
        self.storage = storage
        self.repository = repository

    async def upload_book(
        self,
        title: str,
        author: str,
        genre: str,
        file: UploadFile,
    ):

        extension = "." + file.filename.split(".")[-1]

        if extension.lower() not in ALLOWED_EXTENSIONS:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type",
            )

        unique_name = f"{uuid4()}{extension}"

        content = await file.read()

        storage_path = await self.storage.upload_file(
            unique_name,
            content,
        )

        return await self.repository.create_book(
            title=title,
            author=author,
            genre=genre,
            storage_path=storage_path,
        )