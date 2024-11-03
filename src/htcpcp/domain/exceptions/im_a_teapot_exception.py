from fastapi import HTTPException


class ImATeapotException(HTTPException):
    """Domain exception for a coffee pot not being a coffepot

    Args:
        HTTPException (HTTPException): inherits from base http exception
    """

    def __init__(self):
        super().__init__(
            status_code=418,
            detail=f"I am a Teapot",
            headers={"X-Error": "IAmATeapot"},
        )
