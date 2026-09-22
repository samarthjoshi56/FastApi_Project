from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine
from app.models import User  # noqa: F401 - registers the model with SQLAlchemy
from app.routers.health import router as health_router
from app.routers.users import router as users_router

app = FastAPI(title="FastApi_Project", version="0.3.0")


@app.on_event("startup")
def create_tables() -> None:
    """Create database tables when the application starts."""
    Base.metadata.create_all(bind=engine)


app.include_router(health_router)
app.include_router(users_router)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "FastAPI is running", "version": app.version}
