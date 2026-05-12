from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    async def upload_file(
        self,
        file_name: str,
        content: bytes,
    ) -> str:
        pass

    @abstractmethod
    async def delete_file(
        self,
        file_path: str,
    ) -> None:
        pass