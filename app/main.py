from fastapi import FastAPI
from app.routers import api as apiRouter

def application():

    application = FastAPI()

    application.include_router(apiRouter.router, prefix="/api/v1")

    return application


app = application()