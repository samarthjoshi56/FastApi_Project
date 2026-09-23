from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


_USERS: list[User] = []


def list_users(db: Session, name: str | None = None) -> list[User]:
    statement = select(User)

    if name:
        search = name.strip()
        statement = statement.where(User.name.ilike(f"%{search}%"))

    return list(db.scalars(statement).all())


def get_user(user_id: int) -> User | None:
    return next((user for user in _USERS if user.id == user_id), None)


def create_user(payload: UserCreate) -> User:
    user = User(
        id=len(_USERS) + 1,
        name=payload.name,
        email=str(payload.email),
    )
    _USERS.append(user)
    return user
