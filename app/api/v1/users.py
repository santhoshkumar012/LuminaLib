from fastapi import APIRouter, Depends

from app.application.dto.user_dto import UserResponse

from app.core.dependencies import get_current_user

from app.infrastructure.db.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
async def get_profile(
    current_user: User = Depends(get_current_user),
):

    return current_user