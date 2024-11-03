from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator

from htcpcp.core.domain.validators import ksuid_validator


class PotBase(BaseModel):
    """
    Represents a data structure for a person.
    """

    id: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "description": "Unique Pot ID (ksuid)",
            "example": "0ujsswThIGTUYm2K8FjOOfXtY1K",
        },
    )

    name: str = Field(
        ...,
        max_length=500,
        json_schema_extra={
            "description": "Pot name",
            "example": "T-800",
        },
    )

    location: str = Field(
        ...,
        max_length=500,
        json_schema_extra={
            "description": "Pot location",
            "example": "Kitchen area",
        },
    )

    # @field_validator("id")
    # def validate_ksuid(cls, value, values, **kwargs):
    #     return ksuid_validator(value)
