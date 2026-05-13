from pathlib import Path

from app.infrastructure.llm.ollama_client import (
    OllamaClient,
)

from app.infrastructure.storage.local_storage import (
    LocalStorage,
)

from app.infrastructure.repositories.book_repository_impl import (
    BookRepositoryImpl,
)

from app.core.database import AsyncSessionLocal


async def generate_book_summary(
    book_id,
    file_path: str,
):

    path = Path(file_path)

    if not path.exists():
        return

    text = path.read_text(
        encoding="utf-8",
        errors="ignore",
    )

    llm = OllamaClient()

    summary = await llm.generate_summary(text)

    async with AsyncSessionLocal() as db:

        repository = BookRepositoryImpl(db)

        await repository.update_summary(
            book_id,
            summary,
        )