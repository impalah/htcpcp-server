from typing import Any

import httpx
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from htcpcp.api.v1.healthcheck.api import api_router


@pytest.fixture(scope="session")
def app() -> FastAPI:

    app = FastAPI()
    app.include_router(api_router)

    return app


@pytest.fixture(scope="session")
def client(app: FastAPI) -> TestClient:
    with TestClient(app) as client:
        yield client


# @pytest.fixture(autouse=True)
# def disable_auth():
#     with patch("auth_middleware.settings.settings.AUTH_MIDDLEWARE_DISABLED", True):
#         yield


@pytest.mark.asyncio
async def test_healthcheck_basic_success(client: TestClient):

    # Act
    response: httpx.Response = client.get("/")

    # Assert
    assert response.status_code == 200

    data: Any = response.json()
    assert isinstance(data, dict)
    assert data["status"] == "Healthy"
