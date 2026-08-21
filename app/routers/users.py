from fastapi import APIRouter, status

from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return list_users()


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def add_user(payload: UserCreate) -> UserResponse:
    return create_user(payload)
