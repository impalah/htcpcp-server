import enum


class OrderStatusEnum(enum.Enum):
    """Order statuses
        WAITING: The order is waiting to be processed
        VALIDATING: The order is being validated
        PROCESSING: The order is being processed
        READY: The order is ready to be delivered
        DELIVERED: The order has been delivered to the requester
        ERROR: The order has encountered an error
        UNKNOWN: The order status is unknown

    Args:
        enum (_type_): _description_
    """

    WAITING = "waiting"
    VALIDATING = "validating"
    PROCESSING = "processing"
    READY = "ready"
    DELIVERED = "delivered"
    ERROR = "error"
    UNKNOWN = "unknown"

    def __str__(self):
        return self.value
