from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

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
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db),
):

    repository = UserRepositoryImpl(db)

    service = AuthService(repository)

    return await service.login(
        email=payload.email,
        password=payload.password,
    )