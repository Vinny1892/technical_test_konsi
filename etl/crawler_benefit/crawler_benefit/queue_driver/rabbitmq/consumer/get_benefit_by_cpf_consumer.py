from typing import Any, Dict

from crawler_benefit.queue_driver.rabbitmq.consumer.base_consumer import BaseConsumer
from crawler_benefit.repository.database.store_benefit_index_database import (
    StoreBenefitIndexDatabase,
)
from crawler_benefit.repository.database.store_benefit_memory_cached_repository import (
    StoreBenefitMemoryCachedRepository,
)
from crawler_benefit.steps.pipeline_benefit import PipelineBenefit


class GetBenefitByCpfConsumer(BaseConsumer):
    def consume(self, message: Dict) -> None:
        print("INICIANDO PIPELINE")
        memory_repository = StoreBenefitMemoryCachedRepository()
        index_database_repository = StoreBenefitIndexDatabase()
        pipeline = PipelineBenefit(
            memory_repository=memory_repository, index_database_repository=index_database_repository
        )
        pipeline.main(message)
        print(f"Recebido: {message}")
