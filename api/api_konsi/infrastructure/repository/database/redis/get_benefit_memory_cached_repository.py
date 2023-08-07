from typing import Optional

import redis

from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.infrastructure.config.environment_variable.config import config


class GetBenefitMemoryCachedRepository(GetBenefitContract):
    def get(self, cpf: Optional[str]) -> str:
        port = config('REDIS_PORT', 6379, cast=int)
        host = config('REDIS_HOST', 'localhost')
        redis_client = redis.StrictRedis(host=host, port=port, decode_responses=True)
        value = redis_client.get('last_benefit')
        return value
        #redis_client.set('mykey', 'myvalue')
