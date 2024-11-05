import asyncio
import random

from htcpcp.core.logging import logger
from htcpcp.core.settings import settings
from htcpcp.domain.entities.coffee_order import CoffeeOrder
from htcpcp.domain.entities.pickup_order import PickupOrder
from htcpcp.domain.entities.pot_status import PotStatus
from htcpcp.domain.exceptions.im_a_teapot_exception import ImATeapotException
from htcpcp.domain.exceptions.pickup_order_not_found_exception import (
    PickupOrderNotFoundException,
)
from htcpcp.domain.exceptions.pot_not_available_exception import (
    PotNotAvailableException,
)
from htcpcp.domain.types.pot_status_enum import PotStatusEnum


class CoffeePotSimulator:
    """Coffe pot simulator as singleton.

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """

    _water_level: int = 0
    _bean_level: int = 0
    _temperature: int = 0
    _teapot: bool = False
    _current_order: CoffeeOrder | None = None

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger.debug("Creating CoffeePotSimulator instance")
            cls._instance = super(CoffeePotSimulator, cls).__new__(cls)
            cls._instance._teapot = settings.COFFEE_POT_TEAPOT
            cls._instance.state = PotStatusEnum.READY
            cls._instance.lock = asyncio.Lock()  # To prevent race conditions
        return cls._instance

    async def brew(self, order: CoffeeOrder) -> bool:
        logger.debug("Entering. Brewing")
        async with self.lock:

            if self._teapot:
                logger.error("I'm a teapot")
                raise ImATeapotException()

            # Check if the pot is available
            if self.state != PotStatusEnum.READY:
                logger.error("Coffee pot is busy")
                raise PotNotAvailableException(id="1234")

            logger.debug("Coffee pot is available")
            self._current_order = order
            self.state = PotStatusEnum.BREWING

            # Start brewing
            asyncio.create_task(self._finish_brewing())
            return True

    async def _finish_brewing(self):
        # TODO: timer as setting
        logger.debug("Brewing coffee (timer)")
        await asyncio.sleep(20)
        logger.debug("Coffee pot is ready")
        self.state = PotStatusEnum.BREWED

    async def pickup(self, pickup_order: PickupOrder) -> CoffeeOrder | None:
        logger.debug("Entering. Pickup")
        async with self.lock:

            # Check if the pot is available
            if self.state != PotStatusEnum.BREWED:
                logger.error("No order to pickup")
                raise PotNotAvailableException(id=settings.COFFEE_POT_ID)

            order: CoffeeOrder = self._current_order
            logger.debug(f"Order to pickup: {order}")

            if order.id != pickup_order.id:
                logger.error("Order not found")
                raise PickupOrderNotFoundException(id=pickup_order.id)

            self._current_order = None
            self.state = PotStatusEnum.CLEANING

            asyncio.create_task(self._finish_cleaning())
            return order

    async def _finish_cleaning(self):
        # TODO: timer as setting
        logger.debug("Cleaning coffee (timer)")
        await asyncio.sleep(10)
        logger.debug("Coffee pot is ready")
        self.state = PotStatusEnum.READY

    def _simulate_failure(self, true_weight: int = 75) -> bool:
        """Simulate a failure in the coffee Pot, in general.

        Args:
            true_weight (int, optional): percent of probabilities to get a failure. Defaults to 75.

        Raises:
            ValueError: _description_

        Returns:
            bool: _description_
        """
        if true_weight < 0 or true_weight > 100:
            raise ValueError("True weight must be between 0 and 100")

        return random.choices(
            [True, False], weights=[true_weight, 100 - true_weight], k=1
        )[0]

    async def get_status(self) -> PotStatus:

        result: PotStatus = PotStatus(
            id=settings.COFFEE_POT_ID,
            name=settings.COFFEE_POT_NAME,
            location=settings.COFFEE_POT_LOCATION,
            status=self.state,
            water_level=self._water_level,
            bean_level=self._bean_level,
            temperature=self._temperature,
        )
        return result


# Create an instance of the simulator
coffee_pot_simulator = CoffeePotSimulator()

# Specify what is exported when the module is imported
__all__ = ["coffee_pot_simulator"]
