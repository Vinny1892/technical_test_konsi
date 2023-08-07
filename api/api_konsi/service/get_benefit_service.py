from typing import Dict

from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.contracts.service_contract import ServiceContract


class GetBenefitService(ServiceContract):

    def __init__(self, memory_repository: GetBenefitContract, index_repository: GetBenefitContract):
        self.index_repository = index_repository
        self.memory_repository = memory_repository

    def handle(self, data_request: Dict) -> Dict | None:
        data_redis = self.memory_repository.get(data_request['cpf'])
        if data_redis is not None:
            return {"benefit": data_redis}

        data_index_database = self.index_repository.get(data_request['cpf'])
        return data_index_database



