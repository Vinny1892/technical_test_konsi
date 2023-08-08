import logging
from typing import Optional

import redis
from decouple import config

from crawler_benefit.contract.store_benefit_contract import StoreBenefitContract

logger = logging.getLogger(__file__)


class StoreBenefitMemoryCachedRepository(StoreBenefitContract):
    def store(self, benefit_number: str) -> None:
        port = config("REDIS_PORT", 6379, cast=int)
        host = config("REDIS_HOST", "localhost")
        redis_client = redis.StrictRedis(host=host, port=port, decode_responses=True)
        redis_client.set("last_benefit", benefit_number)
        logger.info("Salvando beneficio no redis")
