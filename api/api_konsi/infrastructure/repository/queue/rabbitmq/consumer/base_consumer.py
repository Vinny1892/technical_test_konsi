from abc import ABC, abstractmethod


class BaseConsumer(ABC):

    @abstractmethod
    def consume(self):
        raise Exception("method not implemented")