from typing import Dict

from htcpcp.core.logging import logger
from htcpcp.domain.entities.coffee_order import CoffeeOrder


def parse_coffee_pot_command(data: str) -> CoffeeOrder:
    """Parse coffee pot command

    Args:
        data (str): _description_

    Returns:
        CoffeeOrder: _description_
    """
    parsed_data: Dict = {}

    for line in data.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts: list[str] = line.split(":")
        if len(parts) == 2:
            key, value = parts
            parsed_data[key.strip().replace("-", "_")] = value.strip()

    logger.debug("Parsed data: {}", parsed_data)

    return CoffeeOrder(**parsed_data)
