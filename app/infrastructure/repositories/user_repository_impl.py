from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.user import User

from app.domain.repositories.user_repository import (
    UserRepository,
)


class UserRepositoryImpl(UserRepository):

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def get_by_email(
        self,
        email: str,
    ) -> User | None:

        result = await self.db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    async def create_user(
        self,
        email: str,
        hashed_password: str,
        full_name: str,
    ) -> User:

        user = User(
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
        )

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user