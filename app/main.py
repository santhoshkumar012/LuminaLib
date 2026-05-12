from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.books import router as books_router

from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(books_router)


@app.get("/")
async def root():
    return {
        "message": "LuminaLib API Running"
    }