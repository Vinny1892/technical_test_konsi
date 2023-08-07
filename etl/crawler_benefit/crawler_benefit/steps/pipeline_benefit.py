from typing import Dict

from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.contract.store_benefit_contract import StoreBenefitContract
from crawler_benefit.steps.extract.extract import Extract
from crawler_benefit.steps.load.load import Load
from crawler_benefit.steps.pipeline_template import PipelineTemplate
from crawler_benefit.steps.transform.transform import Transform


class PipelineBenefit(PipelineTemplate):
    def __init__(self, memory_repository: StoreBenefitContract, index_database_repository: StoreBenefitContract):
        self.memory_repository = memory_repository
        self.index_repository = index_database_repository

    def _transform(self, etl_contract: EtlContract):
        return Transform(etl_contract=etl_contract).transform()

    def _load(self, etl_contract: EtlContract) -> EtlContract:
        return Load(
            etl_data=etl_contract,
            index_database_repository=self.index_repository,
            memory_repository=self.memory_repository,
        ).charge_database()

    def _extract(self, data: Dict) -> EtlContract:
        etl_data = Extract(data).extract()
        return etl_data
