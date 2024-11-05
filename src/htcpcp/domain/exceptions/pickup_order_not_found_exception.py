from fastapi import HTTPException


class PickupOrderNotFoundException(HTTPException):
    """Domain exception for a non existent order

    Args:
        HTTPException (HTTPException): inherits from base http exception
    """

    def __init__(self, id: str):
        super().__init__(
            status_code=404,
            detail=f"Order with id {id} does not exists",
            headers={"X-Error": "PickupOrderNotFound"},
        )
