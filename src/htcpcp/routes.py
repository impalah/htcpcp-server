"""Module to include the API routers for the application
"""

from fastapi import FastAPI

# Healthcheck (do not touch)
from htcpcp.api.v1.healthcheck.router import api_router as healthcheck_v1_router
from htcpcp.api.v1.htcpcp.router import api_router as htcpcp_v1_router
from htcpcp.core.logging import logger


def include_routers(app: FastAPI):
    """Include routers for every application

    Args:
        app (_type_): _description_
    """
    logger.debug("Including routers")

    # Healthcheck route (do not touch)
    app.include_router(healthcheck_v1_router)
    app.include_router(htcpcp_v1_router)
