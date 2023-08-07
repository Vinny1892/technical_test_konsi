from api_konsi.contracts.get_benefit_contract import GetBenefitContract
from api_konsi.infrastructure.config.environment_variable.config import config
from elasticsearch import Elasticsearch


class GetBenefitRepository(GetBenefitContract):
    def get(self, cpf) -> str | None:
        elasticsearch_url = config('ELASTIC_SEARCH_URL', 'http://localhost:9200', cast=str)
        index_name = config("ELASTIC_SEARCH_INDEX", "benefit", cast=str)
        query = {
            "query": {
                "match": {
                    "cpf": cpf
                }
            }
        }
        es = Elasticsearch([elasticsearch_url])
        response = es.search(index=index_name, body=query)
        if response["hits"]["total"]['value'] > 0:
            hits = response["hits"]["hits"]
            for hit in hits:
                print(hit)
                return None
        else:
            return None
