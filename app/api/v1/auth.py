from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from app.application.dto.auth_dto import (
    SignupRequest,
    LoginRequest,
)

from app.core.database import get_db

from app.domain.services.auth_service import AuthService

from app.infrastructure.repositories.user_repository_impl import (
    UserRepositoryImpl,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup")
async def signup(
    payload: SignupRequest,
    db: AsyncSession = Depends(get_db),
):

    repository = UserRepositoryImpl(db)

    service = AuthService(repository)

    return await service.signup(
        email=payload.email,
        password=payload.password,
        full_name=payload.full_name,
    )


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):

    repository = UserRepositoryImpl(db)

    service = AuthService(repository)

    return await service.login(
        email=form_data.username,
        password=form_data.password,
    )