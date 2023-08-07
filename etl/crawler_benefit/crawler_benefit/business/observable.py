from abc import ABC
from typing import List, Optional

from crawler_benefit.business.observer import Observer


class Observable(ABC):
    def __init__(self, subscribers: Optional[List[Observer]] = []) -> None:
        self.subscribers = subscribers

    def add_subscribers(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscribers(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.notify()
