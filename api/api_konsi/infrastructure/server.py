from uvicorn import run

from api_konsi.infrastructure.config.logger.logger_config import LoggerConfig
from config.environment_variable.config import config


def start_server():
    LoggerConfig().init()
    host = config("HOST", "localhost")
    port = config("PORT", 8080, cast=int)
    run(
        "api_konsi.infrastructure.config.fastapi.config_fastapi:app",
        host=host,
        port=port,
        reload=True,
    )


if __name__ == '__main__':
    start_server()
