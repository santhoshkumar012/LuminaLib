from pathlib import Path

import aiofiles

from app.core.config import settings

from app.domain.interfaces.storage_interface import (
    StorageInterface,
)


class LocalStorage(StorageInterface):

    def __init__(self):

        self.base_path = Path(
            settings.LOCAL_STORAGE_PATH
        )

        self.base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def upload_file(
        self,
        file_name: str,
        content: bytes,
    ) -> str:

        file_path = self.base_path / file_name

        async with aiofiles.open(
            file_path,
            "wb",
        ) as f:

            await f.write(content)

        return str(file_path)

    async def delete_file(
        self,
        file_path: str,
    ) -> None:

        path = Path(file_path)

        if path.exists():
            path.unlink()