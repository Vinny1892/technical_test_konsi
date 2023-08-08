from logging import basicConfig, DEBUG, INFO, StreamHandler

from decouple import config
from pythonjsonlogger import jsonlogger


class LoggerConfig:

    def init(self):
        log_level = DEBUG
        stream_handler = StreamHandler()
        stream_handler.setFormatter(jsonlogger.JsonFormatter())
        if config("APP_ENV", "PRODUCTION"):
            log_level = INFO
        basicConfig(
            level=log_level,
            handlers=[stream_handler]
        )
