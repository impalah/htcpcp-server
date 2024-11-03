import re
from typing import Optional

from ksuid import Ksuid
from pydantic import BaseModel, Field, field_validator
from htcpcp.domain.types import OrderStatusEnum
from htcpcp.domain.entities.coffee_order import CoffeeOrder


class CoffeeOrderResponse(CoffeeOrder):
    """
    Represents a coffee order

    Args:
        BaseModel (BaseModel): Inherited properties.
    """

    status: OrderStatusEnum = Field(
        default=OrderStatusEnum.VALIDATING,
        json_schema_extra={
            "description": "Order status",
            "example": "inactive",
        },
    )
