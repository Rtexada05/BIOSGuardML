# app/main.py

from fastapi import FastAPI

from app.core.config import settings
from app.routers import health, firmware, predict, status, metadata


def create_app() -> FastAPI:
    """
    Application factory for BIOSGuardML.
    """
    app = FastAPI(
        title=settings.name,
        version=settings.version,
        description=settings.description,
    )

    # Register routers
    app.include_router(health.router)
    app.include_router(firmware.router)
    app.include_router(predict.router)
    app.include_router(status.router)
    app.include_router(metadata.router)

    return app


app = create_app()