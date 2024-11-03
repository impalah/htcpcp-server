from fastapi import HTTPException


class PotNotAvailableException(HTTPException):
    """Domain exception for a pot not available

    Args:
        HTTPException (HTTPException): inherits from base http exception
    """

    def __init__(self, id: str):
        super().__init__(
            status_code=409,
            detail=f"Pot with id {id} is not available",
            headers={"X-Error": "PotNotAvailable"},
        )
