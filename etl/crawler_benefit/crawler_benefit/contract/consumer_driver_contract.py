from abc import ABC, abstractmethod


class ConsumerDriverContract(ABC):
    @abstractmethod
    def init(self):
        raise Exception("method not implemented")

    @abstractmethod
    def callback(self, **kwargs):
        raise Exception("method not implemented")
