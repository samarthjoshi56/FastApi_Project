from app.models.user import User
from app.schemas.user import UserCreate

_USERS: list[User] = []


def list_users() -> list[User]:
    return _USERS.copy()


def create_user(payload: UserCreate) -> User:
    user = User(
        id=len(_USERS) + 1,
        name=payload.name,
        email=str(payload.email),
    )
    _USERS.append(user)
    return user
