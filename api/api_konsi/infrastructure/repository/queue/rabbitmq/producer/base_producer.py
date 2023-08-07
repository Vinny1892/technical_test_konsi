from abc import ABC, abstractmethod

from api_konsi.business.observable import Observable


class BaseProducer(Observable, ABC):

    @abstractmethod
    def publish(self, message):
        raise Exception("method not implemented")
