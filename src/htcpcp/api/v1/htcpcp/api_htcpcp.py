""" Api definition
    All validations and mappings should be in the services
"""

import random
from typing import Annotated, Union

from fastapi import APIRouter, Body, Depends, status
from ksuid import Ksuid
from starlette.requests import Request
from starlette.responses import Response

from htcpcp.api.v1.htcpcp.parsers import parse_order
from htcpcp.api.v1.htcpcp.services.coffee_hub_service import CoffeeHubService
from htcpcp.core.api import ProblemDetail

# from htcpcp.core.auth.functions import require_permissions
from htcpcp.core.api.utils import get_content_type
from htcpcp.core.http.validators import ksuid_path_validator
from htcpcp.core.logging import logger
from htcpcp.domain.entities.coffee_order import CoffeeOrder
from htcpcp.domain.entities.coffee_order_response import CoffeeOrderResponse
from htcpcp.domain.entities.pickup_order import PickupOrder
from htcpcp.domain.entities.pot_status import PotStatus
from htcpcp.domain.types import OrderStatusEnum, PotStatusEnum

api_router = APIRouter()


@api_router.get(
    "/",
    response_model=PotStatus,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "description": "Internal Server Error",
        },
    },
)
async def get_status(
    request: Request,
    response: Response,
) -> PotStatus:
    """Get the status of the Pot

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        PotStatus: the pot status
    """

    # Connect with pot simulator and get real status
    return await CoffeeHubService().get_coffee_pot_status()


@api_router.api_route(
    "/",
    methods=["BREW", "POST"],
    status_code=status.HTTP_200_OK,
    response_model=CoffeeOrder,
    responses={
        status.HTTP_403_FORBIDDEN: {
            "model": ProblemDetail,
            "message": "Not allowed to brew coffee",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ProblemDetail,
            "message": "Bad request",
        },
        status.HTTP_409_CONFLICT: {
            "model": ProblemDetail,
            "message": "Pot is not available",
        },
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE: {
            "model": ProblemDetail,
            "message": "Unsupported media type",
        },
        status.HTTP_418_IM_A_TEAPOT: {
            "model": ProblemDetail,
            "message": "I am a Teapot",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "message": "Internal Server Error",
        },
    },
)
async def brew_coffee(
    request: Request,
    response: Response,
    data: Annotated[Union[CoffeeOrder, str], Body(...)],
    content_type: str = Depends(get_content_type),
) -> CoffeeOrder | ProblemDetail:
    """Brews a coffee order

    Args:
        request (Request): _description_
        response (Response): _description_
        data (Annotated[Union[CoffeeOrder, str], Body): _description_
        content_type (str, optional): _description_. Defaults to Depends(get_content_type).

    Returns:
        CoffeeOrder | ProblemDetail: _description_
    """

    logger.debug("Data is: \n{}", data)
    logger.debug("Content-type is: {}", content_type)

    order: CoffeeOrder = parse_order(content_type, data)
    # Set the order id based on the transaction id
    logger.debug("Order value: {}", order)

    coffee_response: CoffeeOrder = await CoffeeHubService().brew(
        order=order,
    )

    return coffee_response


@api_router.api_route(
    "/",
    methods=["PICKUP", "PATCH"],
    status_code=status.HTTP_200_OK,
    response_model=CoffeeOrder,
    responses={
        status.HTTP_403_FORBIDDEN: {
            "model": ProblemDetail,
            "message": "Not allowed to pickup coffee",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ProblemDetail,
            "message": "Bad request",
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ProblemDetail,
            "message": "Order not found",
        },
        status.HTTP_409_CONFLICT: {
            "model": ProblemDetail,
            "message": "Pot is not available",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "message": "Internal Server Error",
        },
    },
)
async def pickup_coffee(
    request: Request,
    response: Response,
    pickup_order: PickupOrder,
) -> CoffeeOrder | ProblemDetail:
    """Pickup a finished coffee order

    Args:
        request (Request): _description_
        response (Response): _description_
        data (Annotated[Union[CoffeeOrder, str], Body): _description_
        content_type (str, optional): _description_. Defaults to Depends(get_content_type).

    Returns:
        CoffeeOrder | ProblemDetail: _description_
    """

    logger.debug("Pickup Order value: {}", pickup_order)

    coffee_response: CoffeeOrder = await CoffeeHubService().pickup(
        pickup_order=pickup_order,
    )

    return coffee_response


@api_router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_403_FORBIDDEN: {
            "model": ProblemDetail,
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "description": "Internal Server Error",
        },
    },
)
async def reset_device(
    request: Request,
    response: Response,
):
    """Resets the device to ready, whatever its state may be.

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        _type_: _description_
    """

    logger.debug("Resetting the device")

    await CoffeeHubService().reset()
    return
