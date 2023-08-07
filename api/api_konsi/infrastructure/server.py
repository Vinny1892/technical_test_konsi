import logging

from uvicorn import run
from config.environment_variable.config import config

def start_server():
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
