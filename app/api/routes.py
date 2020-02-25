"""Routes for application API"""
from fastapi import FastAPI

from .users import auth


def init_routes(app: FastAPI) -> FastAPI:
    """Init application Routes"""
    app.include_router(auth.auth_routes, prefix='/users')

    return app
