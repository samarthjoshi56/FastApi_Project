from datetime import datetime, timezone

from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/time", tags=["health"])
def health_time() -> dict[str, str]:
    return {"utc": datetime.now(timezone.utc).isoformat()}
