from pydantic import BaseModel, EmailStr, Field, field_validator

from htcpcp.domain.entities.pot_base import PotBase
from htcpcp.domain.types import PotStatusEnum


class PotStatus(PotBase):
    """
    Represents a data structure for a Pot Status when retrieving data.
    """

    status: PotStatusEnum = Field(
        default=PotStatusEnum.READY,
        json_schema_extra={
            "description": "Pot status",
            "example": "inactive",
        },
    )

    water_level: float = Field(
        default=0.0,
        json_schema_extra={
            "description": "Water level (in ml)",
            "example": "500",
        },
    )

    bean_level: float = Field(
        default=0.0,
        json_schema_extra={
            "description": "Bean level (in g)",
            "example": "100",
        },
    )

    temperature: float = Field(
        default=0.0,
        json_schema_extra={
            "description": "Temperature (in °C)",
            "example": "80",
        },
    )
