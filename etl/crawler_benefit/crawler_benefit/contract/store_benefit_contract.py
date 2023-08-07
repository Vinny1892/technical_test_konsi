from abc import ABC, abstractmethod
from typing import Optional


class StoreBenefitContract(ABC):
    @abstractmethod
    def store(self, benefit_number: str) -> None:
        raise Exception("method not implemented")
