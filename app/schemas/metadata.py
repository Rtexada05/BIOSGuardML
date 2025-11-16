# app/schemas/metadata.py
from pydantic import BaseModel
from typing import List, Literal


class FeatureInfo(BaseModel):
    name: str
    dtype: Literal["float", "int", "string", "bool"]
    description: str


class ModelMetadata(BaseModel):
    model_name: str
    model_version: str
    task_type: Literal["anomaly_detection", "classification", "regression"]
    features: List[FeatureInfo]
    notes: str | None = None