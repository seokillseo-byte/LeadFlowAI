from fastapi.testclient import TestClient

from backend.app.main import app

def test_health_contract():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["ok"] is True

def test_scan_contract_is_preserved():
    client = TestClient(app)
    response = client.post("/api/scan")
    assert response.status_code == 200
    assert response.json()["message"] == "Scan job queued"
