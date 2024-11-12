import json
from typing import Any, Dict, List

from starlette.config import Config

config = Config()


class Settings:
    """Settings for the application"""

    PROJECT_NAME: str = config("PROJECT_NAME", cast=str, default="HTCPCP API")
    PROJECT_VERSION: str = config("PROJECT_VERSION", cast=str, default="1.0.0")

    LOG_LEVEL: str = config("LOG_LEVEL", cast=str, default="INFO").upper()
    LOG_FORMAT: str = config(
        "LOG_FORMAT",
        cast=str,
        default="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | trace_id={extra[trace_id]} | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )

    LOGGER_NAME: str = config("LOGGER_NAME", cast=str, default="")

    # Enqueue the logs using multiprocessing
    LOGGER_ENQUEUE: bool = config("LOGGER_ENQUEUE", cast=bool, default=False)

    # CORS Related configurations
    CORS_ALLOWED_ORIGINS: List[str] = json.loads(
        config("CORS_ALLOWED_ORIGINS", cast=str, default="[]")
    )
    CORS_ALLOWED_METHODS: List[str] = json.loads(
        config("CORS_ALLOWED_METHODS", cast=str, default='["*"]')
    )
    CORS_ALLOWED_HEADERS: List[str] = json.loads(
        config("CORS_ALLOWED_HEADERS", cast=str, default='["*"]')
    )

    # Open telemetry settings
    OTEL_ENABLED = config("OTEL_ENABLED", cast=bool, default=False)
    OTEL_SERVICE_NAME: str = config(
        "OTEL_SERVICE_NAME", cast=str, default="htcpcp-service"
    )
    OTEL_EXPORTER_OTLP_ENDPOINT: str = config(
        "OTEL_EXPORTER_OTLP_ENDPOINT", cast=str, default="http://otel-collector:4317"
    )

    # Coffee Pot settings
    COFFEE_POT_ID = config("COFFEE_POT_ID", cast=str, default="1234")
    COFFEE_POT_NAME = config("COFFEE_POT_NAME", cast=str, default="Coffee Pot")
    COFFEE_POT_LOCATION = config("COFFEE_POT_LOCATION", cast=str, default="Kitchen")
    COFFEE_POT_TEAPOT = config("COFFEE_POT_TEAPOT", cast=bool, default=False)


settings = Settings()
