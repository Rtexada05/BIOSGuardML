# tests/test_status.py
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_status_endpoint_ok():
    response = client.get("/status")
    assert response.status_code == 200

    data = response.json()
    assert "service" in data
    assert "version" in data
    assert data["healthy"] is True