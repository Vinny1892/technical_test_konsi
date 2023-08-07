from abc import ABC, abstractmethod
from typing import Optional


class GetBenefitContract(ABC):

    @abstractmethod
    def get(self, cpf: Optional[str]) -> str | None:
        raise Exception("method not implemented")