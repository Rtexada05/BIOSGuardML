# app/schemas/predict.py

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    firmware_entropy: float
    suspicious_syscalls: int
    boot_time_ms: int
    firmware_version: str


class PredictionResponse(BaseModel):
    anomaly: bool
    score: float
    firmware_version: str
    explanation: str