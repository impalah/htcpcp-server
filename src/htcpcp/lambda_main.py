from fastapi import FastAPI
from mangum import Mangum

from htcpcp.application import start_application
from htcpcp.core.settings import settings

app: FastAPI = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)
start_application(app)

# Configure as lambda handler
lambda_handler = Mangum(app)
