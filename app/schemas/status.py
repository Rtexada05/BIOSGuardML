# app/schemas/status.py
from pydantic import BaseModel


class ServiceStatus(BaseModel):
    service: str
    version: str
    healthy: bool
    description: str | None = None