

from fastapi import FastAPI
from app.apis.api import api_router
from app import models


app = FastAPI()

app.include_router(api_router)