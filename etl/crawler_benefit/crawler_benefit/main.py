import logging

from crawler_benefit.contract.consumer_driver_contract import ConsumerDriverContract
from crawler_benefit.logger import LoggerConfigure
from crawler_benefit.queue_driver.rabbitmq.consumer.handle_consumer import (
    HandleConsumer
)

logger = logging.getLogger(__file__)


def start(consumer_driver: ConsumerDriverContract) -> None:
    consumer_driver.init()


if __name__ == "__main__":
    LoggerConfigure().init()
    logger.info("Iniciando o ETL")
    consumer = HandleConsumer()
    start(consumer)
