# app/services/predict_service.py

from app.schemas.predict import PredictionRequest, PredictionResponse


def run_prediction(payload: PredictionRequest) -> PredictionResponse:
    # Simple dummy scoring logic (placeholder for real ML model)
    score_raw = (
        0.4 * payload.firmware_entropy
        + 0.2 * (payload.suspicious_syscalls / 10)
        + 0.4 * (payload.boot_time_ms / 10_000)
    )
    score = max(0.0, min(1.0, round(score_raw, 2)))
    anomaly = score > 0.5

    explanation = (
        "Firmware shows ANOMALOUS behavior based on entropy/telemetry."
        if anomaly
        else "Firmware looks normal based on current telemetry."
    )

    return PredictionResponse(
        anomaly=anomaly,
        score=score,
        firmware_version=payload.firmware_version,
        explanation=explanation,
    )