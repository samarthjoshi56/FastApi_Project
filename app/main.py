from fastapi import FastAPI

from app.routers.health import router as health_router

app = FastAPI(title="FastApi_Project", version="0.2.0")

app.include_router(health_router)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "FastAPI is running"}
