import json
import logging
from typing import Dict

from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.contracts.service_contract import ServiceContract
from api_konsi.infrastructure.repository.queue.rabbitmq.producer.base_producer import BaseProducer


class ScrappingBenefitService(ServiceContract):

    def __init__(self, memory_repository: GetBenefitContract, producer: BaseProducer):
        self.producer = producer
        self.memory_repository = memory_repository

    def handle(self, data_request: Dict) -> Dict:
        self.producer.publish(json.dumps(data_request))
