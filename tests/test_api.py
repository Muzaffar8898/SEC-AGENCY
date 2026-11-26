
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_order():
    response = client.post(
        "/orders",
        json={
            "customer_name": "Test User",
            "description": "Test request"
        }
    )

    assert response.status_code == 201
    assert response.json()["status"] == "PENDING"


def test_get_missing_order():
    response = client.get("/orders/not-found")

    assert response.status_code == 404
