from abc import ABC, abstractmethod
from typing import Any

from crawler_benefit.business.observable import Observable


class BaseConsumer(Observable, ABC):
    @abstractmethod
    def consume(self, body: Any):
        raise Exception("method not implemented")
