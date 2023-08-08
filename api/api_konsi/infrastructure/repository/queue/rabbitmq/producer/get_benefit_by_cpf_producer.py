import logging
from typing import Optional, List

import pika

from api_konsi.business.observer import Observer
from api_konsi.infrastructure.config.environment_variable.config import config
from api_konsi.infrastructure.repository.queue.rabbitmq.producer.base_producer import BaseProducer

logger = logging.getLogger(__file__)

class GetBenefitByCPFProducer(BaseProducer):

    def __init__(self, subscribers: Optional[List[Observer]] = []):
        super().__init__(subscribers)

    def publish(self, message):
        print(f"Publicando mensagem {message} na fila")
        rabbitmq_host = config("RABBITMQ_HOST", "localhost", cast=str)
        rabbitmq_port = config("RABBITMQ_PORT", 5672, cast=int)
        rabbitmq_username = config("RABBITMQ_USERNAME", "guest", cast=str)
        rabbitmq_password = config("RABBITMQ_PASSWORD", "guest", cast=str)
        queue_name = config("RABBITMQ_QUEUE", "queue_test", cast=str)
        exchange_name = config("RABBITMQ_EXCHANGE", "exchange_test", cast=str)
        routing_key = config("RABBITMQ_ROUTING_KEY", "routing_key_test", cast=str)
        exchange_type = config("RABBITMQ_EXCHANGE_TYPE", "topic", cast=str)
        credentials = pika.PlainCredentials(username=rabbitmq_username, password=rabbitmq_password)
        connection_parameters = pika.ConnectionParameters(
            host=rabbitmq_host,
            port=rabbitmq_port,
            credentials=credentials
        )
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)
        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
        logger.info("publicando mensagem na fila")
        self.notify()
