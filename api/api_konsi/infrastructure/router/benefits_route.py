import re
from typing import Annotated

from fastapi import APIRouter, Path

from api_konsi.infrastructure.repository.database.elasticsearch.get_benefit_repository import GetBenefitRepository
from api_konsi.infrastructure.repository.database.redis.get_benefit_memory_cached_repository import \
    GetBenefitMemoryCachedRepository
from api_konsi.infrastructure.repository.queue.rabbitmq.producer.get_benefit_by_cpf_producer import \
    GetBenefitByCPFProducer
from api_konsi.infrastructure.router.model_request.benefit_model_request \
    import BenefitModelRequest
from api_konsi.service.get_benefit_service import GetBenefitService
from api_konsi.service.scrapping_benefit_service import ScrappingBenefitService

router = APIRouter()


@router.post("/benefit", status_code=204)
async def scraping_benefit(benefit_model: BenefitModelRequest):
    memory_repository = GetBenefitMemoryCachedRepository()
    rabbitmq_producer = GetBenefitByCPFProducer()
    service = ScrappingBenefitService(
        memory_repository=memory_repository,
        producer=rabbitmq_producer
    )
    cpf_without_special_character = re.sub(r'[^a-zA-Z0-9]', '', benefit_model.cpf)
    data = {
        "login": benefit_model.login,
        "password": benefit_model.password,
        "cpf": cpf_without_special_character
    }

    return service.handle(data)


@router.get("/benefit/{cpf}")
async def get_benefit(cpf: Annotated[str, Path('cpf do usuario a ser consultado o beneficio')]):
    memory_repository = GetBenefitMemoryCachedRepository()
    index_repository = GetBenefitRepository()
    service = GetBenefitService(
        index_repository=index_repository,
        memory_repository=memory_repository
    )
    cpf_without_special_character = re.sub(r'[^a-zA-Z0-9]', '', cpf)

    data = service.handle({'cpf': cpf_without_special_character})
    if data is None:
        return {"message": "beneficio não encontrado"}
