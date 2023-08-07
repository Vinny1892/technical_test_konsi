from datetime import datetime

from decouple import config
from elasticsearch import Elasticsearch

from crawler_benefit.contract.store_benefit_contract import StoreBenefitContract


class StoreBenefitIndexDatabase(StoreBenefitContract):
    def store(self, data: dict) -> str:
        data["created_at"] = datetime.now()
        elasticsearch_url = config("ELASTIC_SEARCH_URL", "http://localhost:9200", cast=str)
        index_name = config("ELASTIC_SEARCH_INDEX", "benefit", cast=str)
        es = Elasticsearch([elasticsearch_url])
        response = es.index(index=index_name, body=data)
        if response["result"] == "created":
            return data["benefit_number"]
        else:
            raise Exception("Falha ao inserir o documento.")
