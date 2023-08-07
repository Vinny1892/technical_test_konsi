from unittest.mock import Mock

from starlette.testclient import TestClient

from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.infrastructure.config.fastapi.config_fastapi import app


def test_get_benefit_route_when_redis_have_correctly_data(mocker):
    client = TestClient(app)
    data_expected = {"benefit": "21431241342"}
    data = {"cpf": "3214324234", "login": "teste", "password": "teste"}
    mock_repository = mocker.patch("api_konsi.infrastructure.router.benefits_route.GetBenefitMemoryCachedRepository")
    mock_repository().get.return_value = data_expected['benefit']
    response = client.post('benefit', json=data)
    assert response.status_code == 200
    assert response.json() == data_expected
