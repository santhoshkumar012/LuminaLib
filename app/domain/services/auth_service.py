from fastapi import HTTPException, status

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.domain.repositories.user_repository import (
    UserRepository,
)


class AuthService:

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    async def signup(
        self,
        email: str,
        password: str,
        full_name: str,
    ):

        existing_user = await self.user_repository.get_by_email(email)

        if existing_user:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        hashed = hash_password(password)

        user = await self.user_repository.create_user(
            email=email,
            hashed_password=hashed,
            full_name=full_name,
        )

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return {
            "access_token": token,
        }

    async def login(
        self,
        email: str,
        password: str,
    ):

        user = await self.user_repository.get_by_email(email)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return {
            "access_token": token,
        }