import re
from typing import Optional

from ksuid import Ksuid
from pydantic import BaseModel, Field, field_validator

from htcpcp.domain.types import OrderStatusEnum


class PickupOrder(BaseModel):
    """
    Represents a coffee order to pickup

    Args:
        BaseModel (BaseModel): Inherited properties.
    """

    id: str = Field(
        ...,
        json_schema_extra={
            "description": "Unique order id",
            "example": "0ujsswThIGTUYm2K8FjOOfXtY1K",
        },
    )
