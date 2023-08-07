import time

from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.contract.store_benefit_contract import StoreBenefitContract
from crawler_benefit.exceptions.steps.etl_exception import EtlException


class Load:
    def __init__(
        self,
        index_database_repository: StoreBenefitContract,
        memory_repository: StoreBenefitContract,
        etl_data: EtlContract,
    ):
        self.memory_repository = memory_repository
        self.index_database_repository = index_database_repository
        self.etl_data = etl_data

    def charge_database(self):
        try:
            init = time.time()
            if self.etl_data.data["benefit_number"] is not None:
                self.memory_repository.store(self.etl_data.data["benefit_number"])
                self.index_database_repository.store(self.etl_data.data)
            final = time.time()
            time_function_duration = final - init
            return EtlContract(self.etl_data.data, "Load", time_function_duration)
        except:
            message = "error when running load data in etl"
            raise EtlException(stage="Load", data=self.etl_data.data, message=message)
