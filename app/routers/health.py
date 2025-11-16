# app/routers/health.py

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check():
    """
    Simple endpoint to verify that the service is running.

    Returns metadata that is useful for monitoring and debugging.
    """
    return {
        "status": "ok",
        "service": settings.name,
        "version": settings.version,
    }