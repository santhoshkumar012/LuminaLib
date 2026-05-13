from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
)
from fastapi import BackgroundTasks

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.book_dto import (
    BookResponse,
)

from app.core.database import get_db

from app.core.dependencies import get_current_user

from app.infrastructure.db.models.user import User

from app.infrastructure.storage.local_storage import (
    LocalStorage,
)

from app.infrastructure.repositories.book_repository_impl import (
    BookRepositoryImpl,
)

from app.domain.services.book_service import (
    BookService,
)

from app.application.tasks.book_tasks import (
    generate_book_summary,
)


router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.post(
    "/upload",
    response_model=BookResponse,
)
async def upload_book(
    background_tasks: BackgroundTasks,
    title: str = Form(...),
    author: str = Form(...),
    genre: str = Form(...),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    storage = LocalStorage()

    repository = BookRepositoryImpl(db)

    service = BookService(
        storage=storage,
        repository=repository,
    )

    book = await service.upload_book(
        title=title,
        author=author,
        genre=genre,
        file=file,
    )

    background_tasks.add_task(
        generate_book_summary,
        book.id,
        book.storage_path,
    )

    return book