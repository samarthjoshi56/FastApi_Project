from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user, get_user, list_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return list_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int) -> UserResponse:
    user = get_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def add_user(payload: UserCreate) -> UserResponse:
    return create_user(payload)
