"""
    Startup and shutdown code for the whole application
"""

from contextlib import asynccontextmanager

# from aiocache import caches
from fastapi import FastAPI

from htcpcp.core.logging import logger

# from htcpcp.core.repository.manager.sqlalchemy.async_database import AsyncDatabase
from htcpcp.core.settings import settings


async def initialize_dynamodb():
    """Initialize the Dynamodb database"""

    logger.debug("Initializing DYNAMODB database ...")

    logger.debug("DYNAMODB database initialized ...")


async def initialize_sqlalchemy():
    """
    Initialize SQLALCHEMY database
    """
    logger.debug("Initializing SQLALCHEMY database ...")

    logger.debug("SQLALCHEMY database initialized")


async def initialize_cache():
    """
    Initialize aiocache cache
    """
    logger.debug("Initializing cache ...")

    logger.debug("Cache initialized")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous initilizations on startup/shutdown
    Substitute old app.on_event("startup")
    """

    # --------------------------------------------------------------
    # Startup section
    # --------------------------------------------------------------

    # if settings.INITIALIZE_DATABASE:

    #     # Initialize SQLALCHEMY database
    #     await initialize_sqlalchemy()

    #     # Initialize DynamoDB database
    #     await initialize_dynamodb()

    # if settings.CACHE_ENABLED:
    #     await initialize_cache()

    logger.info("Async startup completed ...")

    yield

    # --------------------------------------------------------------
    # Shutdown section
    # --------------------------------------------------------------

    logger.info("Async shutdown completed ...")
