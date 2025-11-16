# app/routers/predict.py

from fastapi import APIRouter

from app.schemas.predict import PredictionRequest, PredictionResponse
from app.services.predict_service import run_prediction

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    return run_prediction(payload)