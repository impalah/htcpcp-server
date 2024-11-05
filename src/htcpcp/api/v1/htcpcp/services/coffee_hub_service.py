from htcpcp.api.v1.htcpcp.services.coffee_pot_simulator import coffee_pot_simulator
from htcpcp.core.logging import logger
from htcpcp.domain.entities.coffee_order import CoffeeOrder
from htcpcp.domain.entities.pickup_order import PickupOrder
from htcpcp.domain.entities.pot_status import PotStatus


class CoffeeHubService:
    """Connection with the pot."""

    async def brew(
        self,
        order: CoffeeOrder,
    ) -> CoffeeOrder:
        """
        Create a brew order for the given coffeepot.
        Coffe service is divided in two parts:
        - Pot service: handles the pot status and configuration before brewing
        - Task service: handles the task status and configuration, on the pot itself (brewing)

        Args:
            pot (Pot): The requested pot to create.
            order (CoffeeOrder): The order to brew

        Returns:
            PotInfo: The pot info with the new status
        """

        logger.debug(f"Entering. Brewing: {order}")

        # simulate brewing
        logger.debug("Brewing coffee")
        result = await coffee_pot_simulator.brew(order)

        return order

    async def get_coffee_pot_status(self) -> PotStatus:
        """Get the status of the coffee pot.

        Returns:
            Tuple[str, int]: The status of the pot
        """
        logger.debug("Entering. Getting status")
        return await coffee_pot_simulator.get_status()

    async def pickup(
        self,
        pickup_order: PickupOrder,
    ) -> CoffeeOrder:
        """
        Pickup the coffee order from the pot.

        Args:
            pot (Pot): The requested pot to create.
            order (CoffeeOrder): The order to brew

        Returns:
            PotInfo: The pot info with the new status
        """

        logger.debug(f"Entering. pick up: {pickup_order}")

        # TODO: check if the order is available.

        # simulate brewing
        logger.debug("Brewing coffee")
        result: CoffeeOrder | None = await coffee_pot_simulator.pickup(
            pickup_order=pickup_order
        )

        return result
