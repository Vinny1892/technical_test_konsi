from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def notify(self):
        raise Exception("method not implemented")
