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
    logger.debug("Data is: \n{}", data)
    logger.debug("Content-type is: {}", content_type)

    order: CoffeeOrder = parse_order(content_type, data)
    # Set the order id based on the transaction id
    logger.debug("Order value: {}", order)

    coffee_response: CoffeeOrder = await CoffeeHubService().brew(
        order=order,
    )

    return coffee_response


@api_router.get(
    "/orders/{id}",
    response_model=CoffeeOrderResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "description": "Internal Server Error",
        },
    },
)
async def get_order_status(
    request: Request,
    response: Response,
    id: str,
) -> CoffeeOrderResponse:
    """Get the status of the Coffee Order

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        PotStatus: the pot status
    """

    # # TODO: Connect with service and get real status
    # status = await CoffeeHubService().get_order_status()

    result: CoffeeOrderResponse = CoffeeOrderResponse(
        id=str(Ksuid()),
        coffee_type="Latte",
        sugar=random.randint(0, 9),
        milk=random.choices([True, False], weights=[75, 25], k=1)[0],
        status=random.choice(list(OrderStatusEnum)),
    )
    return result


@api_router.patch(
    "/orders/{order_id}/pickup",
    response_model=CoffeeOrderResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ProblemDetail,
            "description": "Internal Server Error",
        },
    },
)
async def pickup_order(
    request: Request,
    response: Response,
    order_id: int,
) -> CoffeeOrderResponse:
    """Pickup the order

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        CoffeeOrderResponse: the coffeorder
    """

    # TODO: check if order exists

    # TODO: Check if order is ready to be picked up

    result: CoffeeOrderResponse = CoffeeOrderResponse(
        id=str(Ksuid()),
        coffee_type="Latte",
        sugar=random.randint(0, 9),
        milk=random.choices([True, False], weights=[75, 25], k=1)[0],
        status=random.choice(list(OrderStatusEnum)),
    )
    return result


# @api_router.api_route(
#     "/{id}",
#     methods=["WHEN"],
#     status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
#     responses={
#         status.HTTP_403_FORBIDDEN: {
#             "model": ApiMessage,
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             "model": ApiMessage,
#         },
#         status.HTTP_405_METHOD_NOT_ALLOWED: {
#             "model": ApiMessage,
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ApiMessage,
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer", "administrator"])),
#         Depends(require_user()),
#     ],
# )
# async def when_coffee(
#     id: str = Path(..., description="The ID of the coffee pot"),
# ):
#     return JSONResponse(
#         status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
#         content="Method not allowed",
#     )


# @api_router.api_route(
#     "/{id}",
#     methods=["PROPFIND"],
#     status_code=status.HTTP_200_OK,
#     response_model=PotInfo,
#     responses={
#         status.HTTP_403_FORBIDDEN: {
#             "model": ApiMessage,
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             "model": ApiMessage,
#         },
#         status.HTTP_415_UNSUPPORTED_MEDIA_TYPE: {
#             "model": ApiMessage,
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ApiMessage,
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer", "administrator"])),
#         Depends(require_user()),
#     ],
# )
# async def propfind(
#     request: Request,
#     response: Response,
#     id: str = Path(..., description="The ID of the coffee pot"),
#     content_type: str = Header(None),
#     data: str = Body(..., media_type="text/plain"),
# ):
#     """Retrieves information about the brewed resource

#     If a cup of coffee is data, metadata about the brewed resource is
#     discovered using the PROPFIND method [WEBDAV].


#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         id (UUID, optional): _description_. Defaults to Path(..., description="The ID of the coffee pot").
#         content_type (str, optional): _description_. Defaults to Header(None).
#         data (str, optional): _description_. Defaults to Body(..., media_type="text/plain").

#     Returns:
#         _type_: _description_
#     """
#     logger.debug("Data is: \n{}", data)
#     logger.debug("Content-type is: {}", content_type)

#     order: CoffeeOrder = parse_order(content_type, data)
#     logger.debug("Order value: {}", order)

#     try:
#         coffee_response: PotInfo = await CoffeeService().brew(
#             id=id,
#             order=order,
#         )
#         return coffee_response
#     # except PotModificationNotAlloweddException as e:
#     #     logger.exception("Not allowed exception")
#     #     status_code = status.HTTP_403_FORBIDDEN
#     #     error_message = {"message": str(e)}
#     except PotNotFoundException as e:
#         logger.exception("Controlled exception")
#         status_code = status.HTTP_404_NOT_FOUND
#         error_message = {"message": str(e)}
#     except ImATeapotException as e:
#         logger.exception("I am a tepot exception")
#         status_code = status.HTTP_418_IM_A_TEAPOT
#         error_message = {"message": str(e)}
#     except Exception as e:
#         logger.exception("Not controlled exception")
#         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         error_message = {"message": f"Something went wrong: {str(e)}"}

#     return JSONResponse(
#         status_code=status_code,
#         content=error_message,
#     )


# @api_router.get(
#     "/{id}/orders",
#     response_model=List[CoffeeOrder],
#     status_code=status.HTTP_200_OK,
#     responses={
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ApiMessage,
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer", "administrator"])),
#         Depends(require_user()),
#     ],
# )
# async def get_orders_by_pot(
#     request: Request,
#     response: Response,
#     id: str = Path(..., description="The ID of the coffee pot"),
# ) -> List[CoffeeOrder] | JSONResponse:
#     """Get list of all orders for the given pot.

#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         id (str, optional): _description_. Defaults to Path(..., description="The ID of the coffee pot").

#     Returns:
#         List[CoffeeOrder] | JSONResponse: _description_
#     """

#     # TODO: Filter by status

#     status_code: int
#     error_message: dict

#     logger.debug("Pot id: {}", id)

#     try:
#         # TODO: generalize filter
#         result: List[CoffeeOrder] = await OrderReadService().get_list_by_pot_id(id=id)
#         return result

#     except Exception as e:
#         logger.exception("Not controlled exception")
#         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         error_message = {"message": f"Something went wrong: {str(e)}"}

#     return JSONResponse(
#         status_code=status_code,
#         content=error_message,
#     )


# @api_router.get(
#     "/{id}",
#     response_model=Person,
#     status_code=status.HTTP_200_OK,
#     responses={
#         status.HTTP_404_NOT_FOUND: {
#             "model": ProblemDetail,
#             "description": "Person not found",
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ProblemDetail,
#             "description": "Internal Server Error",
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer"])),
#         Depends(ksuid_path_validator),
#     ],
# )
# async def get_by_id(
#     request: Request,
#     response: Response,
#     id: str,
# ) -> Person:
#     """Get a person by id

#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         id (str): _description_

#     Returns:
#         Person: _description_
#     """

#     entity: Person = await ReadService().get_by_id(id=id)
#     return entity


# @api_router.delete(
#     "/{id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     responses={
#         status.HTTP_403_FORBIDDEN: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_404_NOT_FOUND: {
#             "model": ProblemDetail,
#             "description": "Person not found",
#         },
#         status.HTTP_409_CONFLICT: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ProblemDetail,
#             "description": "Internal Server Error",
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer"])),
#         Depends(ksuid_path_validator),
#     ],
# )
# async def delete_by_id(
#     request: Request,
#     response: Response,
#     id: str,
# ):
#     """Deletes a person with the specific id.
#     - Person should not have any active policies associated with it.

#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         id (str): _description_

#     Returns:
#         _type_: _description_
#     """

#     await WriteService().delete_by_id(id=id)
#     return


# @api_router.put(
#     "/{id}",
#     response_model=Person,
#     status_code=status.HTTP_200_OK,
#     responses={
#         status.HTTP_409_CONFLICT: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_404_NOT_FOUND: {
#             "model": ProblemDetail,
#             "description": "Person not found",
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ProblemDetail,
#             "description": "Internal Server Error",
#         },
#     },
#     dependencies=[
#         # Depends(require_groups(["customer"])),
#         Depends(require_user()),
#         Depends(ksuid_path_validator),
#     ],
# )
# async def update(
#     request: Request,
#     response: Response,
#     id: str,
#     person: PersonCreate,
# ) -> Person:
#     """Update the person with the given information.
#     - Do not allow to dissasociate any active polcies from the person.

#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         id (str): _description_
#         person (PersonCreate): _description_

#     Returns:
#         Person: _description_
#     """

#     logger.debug("update request: {}", person)

#     entity: Person = await WriteService().update(
#         id=id,
#         # current_user=current_user,
#         request=person,
#     )

#     return entity


# @api_router.post(
#     "/",
#     response_model=Person,
#     status_code=status.HTTP_201_CREATED,
#     responses={
#         status.HTTP_400_BAD_REQUEST: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_403_FORBIDDEN: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_409_CONFLICT: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_422_UNPROCESSABLE_ENTITY: {
#             "model": ProblemDetail,
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#             "model": ProblemDetail,
#             "description": "Internal Server Error",
#         },
#     },
#     dependencies=[
#         Depends(require_groups(["customer"])),
#     ],
# )
# async def create(
#     request: Request,
#     response: Response,
#     person: PersonCreate,
# ) -> Person:
#     """Create a new person with the given information.
#     - Check for existence of addresses and policies.

#     Args:
#         request (Request): _description_
#         response (Response): _description_
#         person (PersonCreate): _description_

#     Returns:
#         Person: _description_
#     """

#     entity: Person = await WriteService().create(
#         # current_user=current_user,
#         request=person,
#     )

#     return entity
