"""Initialize application"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import init_routes

app: FastAPI = FastAPI(
    title='FastAPI Issue 548',
    version='0.1.0',
    docs_url='/docs',
    # Disable ReDoc documentation
    redoc_url=None
)


@app.on_event('startup')
def create_app():
    init_middlewares(app)
    init_routes(app)
    return app


def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
