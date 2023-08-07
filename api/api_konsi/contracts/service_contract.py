from abc import ABC, abstractmethod
from typing import Dict


class ServiceContract(ABC):

    @abstractmethod
    def handle(self, data: Dict) -> Dict | None:
        return {}
