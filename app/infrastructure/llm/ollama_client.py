import httpx

from app.core.config import settings

from app.domain.interfaces.llm_interface import (
    LLMInterface,
)


class OllamaClient(LLMInterface):

    async def generate_summary(
        self,
        text: str,
    ) -> str:

        prompt = f"""
        Summarize the following book content
        in 5 concise sentences.

        Content:
        {text[:4000]}
        """

        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": settings.OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=120,
            )

        data = response.json()

        return data["response"]