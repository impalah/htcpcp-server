import enum


class PotStatusEnum(enum.Enum):
    """Pot statuses

    Args:
        enum (_type_): _description_
    """

    READY = "ready"
    BREWING = "brewing"
    BREWED = "brewed"
    CLEANING = "cleaning"
    EMPTY = "empty"
    ERROR = "error"

    def __str__(self):
        return self.value
