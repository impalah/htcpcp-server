""" Api definition
    All validations and mappings should be in the services
"""

from fastapi import APIRouter, Depends, HTTPException, status
from starlette.requests import Request
from starlette.responses import Response

from htcpcp.core.api import ProblemDetail
from htcpcp.core.logging import logger
from htcpcp.core.settings import settings

from .response import HealthCheckResponse

api_router = APIRouter()


@api_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
        },
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "model": ProblemDetail,
        },
    },
)
async def get(
    request: Request,
) -> HealthCheckResponse:
    """
    Healthcheck endpoint for orchestrators
    Recommendation: Do not check database or external services as it could overload the servers

    Returns:
        HealthCheckResponse: health information
    """

    logger.debug("Healthcheck started")

    return HealthCheckResponse(status="Healthy", version=settings.PROJECT_VERSION)
