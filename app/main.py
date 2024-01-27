from fastapi import FastAPI
from app.routers import blacklist, number as apiRoutes

def application():

    application = FastAPI()

    application.include_router(apiRoutes.router, prefix="/api/v1")

    return application


app = application()