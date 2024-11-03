import re
from typing import Optional

from ksuid import Ksuid
from pydantic import BaseModel, Field, field_validator
from htcpcp.domain.types import OrderStatusEnum


class CoffeeOrder(BaseModel):
    """
    Represents a coffee order

    Args:
        BaseModel (BaseModel): Inherited properties.
    """

    id: Optional[str] = Field(
        default_factory=lambda: str(Ksuid()),
        json_schema_extra={
            "description": "Unique order id",
            "example": "0ujsswThIGTUYm2K8FjOOfXtY1K",
        },
    )

    coffee_type: str = Field(
        ...,
        max_length=150,
        json_schema_extra={
            "description": "Coffee type",
            "example": "Latte Machiatto",
        },
    )

    sugar: Optional[int] = Field(
        default=0,
        json_schema_extra={
            "description": "How much sugar?",
            "example": "3",
        },
    )

    milk: Optional[bool] = Field(
        default=False,
        json_schema_extra={
            "description": "With milk?",
            "example": "false",
        },
    )

    # @field_validator("coffee_type")
    # def validate_slug(cls, v):
    #     if not re.match(r"^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*$", v):
    #         raise ValueError("Invalid coffee_type format")
    #     return v

    @field_validator("sugar")
    def parse_sugar(cls, v):
        # Verificar si el valor es una cadena y convertirlo a entero
        if isinstance(v, str):
            # Intentar convertir a entero
            try:
                return int(v)
            except ValueError:
                # Si no se puede convertir, dejar que Pydantic maneje el error
                raise ValueError("Invalid value for integer")
        return v

    @field_validator("milk")
    def parsear_bool(cls, v):
        if isinstance(v, str):
            if v.lower() == "true":
                return True
            elif v.lower() == "false":
                return False
            else:
                raise ValueError("Milk can only be 'true' or 'false'")
        return v
