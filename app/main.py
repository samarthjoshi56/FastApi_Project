from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.users import router as users_router

app = FastAPI(title="FastApi_Project", version="0.3.0")

app.include_router(health_router)
app.include_router(users_router)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "FastAPI is running", "version": app.version}
