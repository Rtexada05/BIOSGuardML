# app/routers/status.py

from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
def get_status():
    return {
        "service": settings.name,
        "version": settings.version,
        "healthy": True,       # 👈 this is what the test is checking
    }