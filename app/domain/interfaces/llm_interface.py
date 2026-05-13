from abc import ABC, abstractmethod


class LLMInterface(ABC):

    @abstractmethod
    async def generate_summary(
        self,
        text: str,
    ) -> str:
        pass