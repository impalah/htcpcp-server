from typing import Any
from unittest.mock import patch

import httpx
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from htcpcp.api.v1.htcpcp.api import api_router


@pytest.fixture(scope="session")
def app() -> FastAPI:

    app = FastAPI()
    app.include_router(api_router)

    return app


@pytest.fixture(scope="session")
def client(app: FastAPI) -> TestClient:
    with TestClient(app) as client:
        yield client


# Does not work :-(
# @pytest.fixture(autouse=True)
# async def reset_state(client: TestClient):

#     # Call reset endpoint before every execution
#     response = client.delete("/")
#     assert response.status_code == 204

#     yield

#     # Call reset endpoint after every execution
#     response = client.delete("/")
#     assert response.status_code == 204


async def reset_state(client: TestClient):

    # Call reset endpoint before every execution
    response = client.delete("/")
    assert response.status_code == 204


@pytest.fixture(autouse=True)
def disable_auth():
    with patch("auth_middleware.settings.settings.AUTH_MIDDLEWARE_DISABLED", True):
        yield


@pytest.mark.asyncio
async def test_get_status(client: TestClient):

    # Act
    response: httpx.Response = client.get("/")

    # Assert
    assert response.status_code == 200

    data: Any = response.json()
    assert isinstance(data, dict)

    assert data["status"] == "ready"


@pytest.mark.asyncio
async def test_brew_text(client: TestClient):

    # Arrange
    payload: str = """
      id:123456
      coffee_type:Latte Machiatto
      sugar:3
      milk:false
        """
    # Act
    response: httpx.Response = client.post(
        "/",
        headers={"Content-Type": "application/coffee-pot-command"},
        data=payload,
    )

    # Assert
    assert response.status_code == 200

    data: Any = response.json()
    assert isinstance(data, dict)

    assert data["id"] == "123456"

    # Call reset endpoint after every execution
    await reset_state(client)


@pytest.mark.asyncio
async def test_brew_json(client: TestClient):

    # Arrange
    payload: str = """
  {
    "id": "654321",
    "coffee_type": "Latte Machiatto",
    "sugar": 3,
    "milk": false
  }
        """
    # Act
    response: httpx.Response = client.post(
        "/",
        headers={"Content-Type": "application/json"},
        data=payload,
    )

    # Assert
    assert response.status_code == 200

    data: Any = response.json()
    assert isinstance(data, dict)

    assert data["id"] == "654321"

    # Call reset endpoint after every execution
    await reset_state(client)
