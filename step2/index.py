from fastapi import FastAPI
from routes.index import app

fastApp = FastAPI()
fastApp.include_router(app)