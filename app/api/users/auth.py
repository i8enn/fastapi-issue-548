"""Endpoints for auth user API"""
from fastapi import APIRouter, Form
from starlette.status import HTTP_200_OK


auth_routes = APIRouter()


@auth_routes.post(
    '/password_reset/{reset_token}',
    status_code=HTTP_200_OK
)
def password_reset(
        *,
        # Not working with password `embed=True` and uvicorn without --reload
        password: str = Form(...)
):
    """Recovery account (reset password) by reset token"""
    pass
