""" Api Routes
"""

from fastapi import APIRouter

from . import api_htcpcp

ROUTE_PREFIX: str = "/api/v1/htcpcp"

api_router = APIRouter()
api_router.include_router(api_htcpcp.api_router, prefix=ROUTE_PREFIX, tags=["HTCPCP"])
