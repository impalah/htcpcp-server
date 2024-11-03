from fastapi import FastAPI

from htcpcp.application import start_application
from htcpcp.core.settings import settings

app: FastAPI = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)
start_application(app)
