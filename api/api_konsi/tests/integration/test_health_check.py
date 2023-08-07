from starlette.testclient import TestClient

from api_konsi.infrastructure.config.fastapi.config_fastapi import app


def test_health_check_route():
    client = TestClient(app)
    response = client.get("health-check")
    assert response.status_code == 200
