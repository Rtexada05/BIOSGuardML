# app/services/predictor.py

from typing import Dict

from ml.model import model_instance
from app.schemas.predict import FirmwareSample, PredictionResult


class PredictionService:
    """
    Orchestrates the steps from input -> features -> model -> output.

    In a real system, this might also:
      - log predictions
      - attach request IDs
      - talk to a database
      - enforce business rules
    """

    def __init__(self):
        self.model = model_instance

    def _build_features(self, sample: FirmwareSample) -> Dict:
        """
        Convert the FirmwareSample into a feature dict for the model.
        """
        return {
            "firmware_entropy": float(sample.firmware_entropy),
            # Simple engineered feature: normalized syscall count
            "normalized_syscalls": float(sample.suspicious_syscalls) / 10.0,
            # Could add more derived features here later
            "boot_time_ms": float(sample.boot_time_ms),
        }

    def predict(self, sample: FirmwareSample) -> PredictionResult:
        features = self._build_features(sample)
        raw_output = self.model.predict(features)

        anomaly = bool(raw_output["anomaly"])
        score = float(raw_output["score"])

        explanation = (
            "Firmware appears NORMAL."
            if not anomaly
            else "Firmware shows ANOMALOUS behavior based on entropy/telemetry."
        )

        return PredictionResult(
            anomaly=anomaly,
            score=score,
            firmware_version=sample.firmware_version,
            explanation=explanation,
        )


# Singleton service instance (can also be injected later if we add DI)
prediction_service = PredictionService()