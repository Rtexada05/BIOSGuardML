# tests/test_metadata.py
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_metadata_endpoint_ok():
    response = client.get("/metadata")
    assert response.status_code == 200

    data = response.json()
    assert data["model_name"] == "biosguardml_baseline"
    assert data["task_type"] == "anomaly_detection"
    assert isinstance(data["features"], list)
    assert len(data["features"]) >= 3

    # Check one known feature name
    feature_names = {f["name"] for f in data["features"]}
    assert "firmware_entropy" in feature_names