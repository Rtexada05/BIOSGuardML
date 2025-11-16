# app/core/config.py

from pydantic import BaseModel


class AppSettings(BaseModel):
    """
    Central place for application configuration.

    Later we can switch this to BaseSettings and pull values from
    environment variables, config files, or secrets managers.
    """

    name: str = "BIOSGuardML"
    version: str = "0.1.0"
    description: str = (
        "Firmware/boot anomaly detection service using FastAPI and machine learning."
    )


# A single global settings instance used across the app
settings = AppSettings()