# tests/test_predict.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_basic_contract():
    """
    Verify that /predict:
      - accepts a valid JSON payload
      - returns 200
      - returns the expected fields and types
    """

    payload = {
        "firmware_entropy": 0.92,
        "suspicious_syscalls": 4,
        "boot_time_ms": 5100,
        "firmware_version": "1.0.8",
    }

    response = client.post("/predict/", json=payload)
    assert response.status_code == 200

    data = response.json()

    # Check required keys exist
    assert "anomaly" in data
    assert "score" in data
    assert "firmware_version" in data
    assert "explanation" in data

    # Type checks
    assert isinstance(data["anomaly"], bool)
    assert isinstance(data["score"], (float, int))
    assert isinstance(data["firmware_version"], str)
    assert isinstance(data["explanation"], str)

    # The firmware_version should round-trip correctly
    assert data["firmware_version"] == payload["firmware_version"]