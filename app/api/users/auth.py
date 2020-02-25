"""Endpoints for auth user API"""
from fastapi import Body, APIRouter
from starlette.status import HTTP_200_OK


auth_routes = APIRouter()


@auth_routes.post(
    '/password_reset/{reset_token}',
    status_code=HTTP_200_OK
)
def password_reset(
        *,
        reset_token: str,
        # Not working with password `embed=True` and uvicorn --reload
        password: str = Body(
            ..., title='New password', embed=True, min_length=3, max_length=20
        )
):
    """Recovery account (reset password) by reset token"""
    pass
