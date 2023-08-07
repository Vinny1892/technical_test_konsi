from abc import ABC, abstractmethod
from typing import Dict

from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.contract.store_benefit_contract import StoreBenefitContract


class PipelineTemplate(ABC):
    def main(self, data: Dict) -> None:
        product_extract = self._extract(data)
        product_transform = self._transform(product_extract)
        self._load(product_transform)

    @abstractmethod
    def _extract(self, data: Dict) -> EtlContract:
        raise Exception("method not implemented")

    @abstractmethod
    def _transform(self, etl_contract: EtlContract) -> EtlContract:
        raise Exception("method not implemented")

    @abstractmethod
    def _load(self, etl_contract: EtlContract) -> EtlContract:
        raise Exception("method not implemented")
