from unittest.mock import Mock

from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.service.get_benefit_service import GetBenefitService


def test_get_benefit_service_when_correctly_data_in_redis():
    benefit = "21431241342"
    mock_repository = Mock(spec=GetBenefitContract)
    mock_repository.get.return_value = benefit

    service = GetBenefitService(memory_repository=mock_repository)
    result = service.handle({'cpf': '123213213123'})
    assert result['benefit'] == benefit
