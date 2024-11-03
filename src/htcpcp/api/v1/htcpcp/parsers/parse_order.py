from typing import Dict

from fastapi import HTTPException, status

from htcpcp.core.api import MediaTypes
from htcpcp.core.logging import logger
from htcpcp.domain.entities.coffee_order import CoffeeOrder

from .parse_coffee_pot_command import parse_coffee_pot_command


def parse_order(content_type: str, data: CoffeeOrder | str) -> CoffeeOrder:
    """Parse order depending on content_type

    Args:
        data (str): _description_

    Returns:
        CoffeeOrder: _description_
    """
    match content_type:
        case MediaTypes.json:
            if isinstance(data, CoffeeOrder):
                return data
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid data type for JSON content type",
                )

        case MediaTypes.coffee_pot_command:
            if isinstance(data, str):
                return parse_coffee_pot_command(data)
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid data type for Coffee Pot Command content type",
                )

        case _:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail="Unsupported Media Type",
            )
