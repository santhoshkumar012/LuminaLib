from abc import ABC, abstractmethod

from app.infrastructure.db.models.user import User


class UserRepository(ABC):

    @abstractmethod
    async def get_by_email(
        self,
        email: str,
    ) -> User | None:
        pass

    @abstractmethod
    async def create_user(
        self,
        email: str,
        hashed_password: str,
        full_name: str,
    ) -> User:
        pass