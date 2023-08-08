import json
import logging

import pika
from decouple import config

from crawler_benefit.contract.consumer_driver_contract import ConsumerDriverContract
from crawler_benefit.queue_driver.rabbitmq.consumer.get_benefit_by_cpf_consumer import (
    GetBenefitByCpfConsumer,
)
logger = logging.getLogger(__file__)

class HandleConsumer(ConsumerDriverContract):
    def callback(self, ch, method, properties, body):
        logger.info("consumindo mensagem no rabbitmq")
        consumer = GetBenefitByCpfConsumer()
        message = body.decode()
        data = json.loads(message)
        consumer.consume(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def init(self):
        rabbitmq_host = config("RABBITMQ_HOST", cast=str)
        rabbitmq_port = config("RABBITMQ_PORT", cast=int)
        rabbitmq_username = config("RABBITMQ_USERNAME", cast=str)
        rabbitmq_password = config("RABBITMQ_PASSWORD", cast=str)
        queue_name = config("RABBITMQ_QUEUE", cast=str)
        credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
        # Conexão com o servidor RabbitMQ
        connection_parameters = pika.ConnectionParameters(
            host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
        )
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        exchange_name = config("RABBITMQ_EXCHANGE", cast=str)
        routing_key = config("RABBITMQ_ROUTING_KEY", cast=str)
        exchange_type = config("RABBITMQ_EXCHANGE_TYPE", cast=str)

        channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)
        # channel.basic_qos(prefetch_count=1)
        # result = channel.queue_declare("", exclusive=True)
        # queue_name = result.method.queue
        # channel.queue_declare(queue=queue_name, durable=True)

        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=False)

        logger.info("Aguardando mensagens. Para sair pressione CTRL+C")
        channel.start_consuming()
