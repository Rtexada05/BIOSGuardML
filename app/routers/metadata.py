# app/routers/metadata.py
from fastapi import APIRouter

router = APIRouter(prefix="/metadata", tags=["Metadata"])

@router.get("/")
def get_metadata():
    return {
        "model_name": "biosguardml_baseline",
        "task_type": "anomaly_detection",
        "features": [
            {"name": "firmware_entropy"},
            {"name": "feature2"},
            {"name": "feature3"}
        ]
    }