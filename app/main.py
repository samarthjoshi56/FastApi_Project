from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.users import router as users_router

app = FastAPI(title="CargoFlow", version="0.6.0")

app.include_router(health_router)
app.include_router(users_router)
app.include_router(auth_router)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "CargoFlow API is running", "version": app.version}
