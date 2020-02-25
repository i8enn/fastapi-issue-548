"""Endpoints for auth user API"""
from fastapi import Body, Depends, APIRouter
from fastapi.openapi.models import EmailStr
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_200_OK

from .schemes.users import User

auth_routes = APIRouter()


@auth_routes.post(
    '/auth',
    name='auth_by_credentials',
    status_code=HTTP_200_OK,
    response_model=User
)
def auth(*, credentials: User):
    """
    Authorization user with username and password.

    Request:
    - **username** - User username
    - **password** - User password

    Response:
    - **access_token** - Token for authorization user
    - **refresh_token** - Token for get new access token and refresh token
    - **user** - User data

    For use access_token include following header for request:


    `Authorization: Bearer {token}`
    """
    return credentials


@auth_routes.post(
    '/auth/swagger',
    name='swagger_auth',
    status_code=HTTP_200_OK,
    response_model=User,
    deprecated=True
)
def auth_swagger(*, credentials: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint for swagger auth (Use form mime-type)
    Authorization user with username and password.

    Request:
    - **username** - User username
    - **password** - User password

    Response:
    - **access_token** - Token for authorization user
    - **refresh_token** - Token for get new access token and refresh token
    - **user** - User data

    For use access_token include following header for request:


    `Authorization: Bearer {token}`
    """
    return User(
        username=credentials.username,
        password=credentials.password
    )


@auth_routes.post(
    '/refresh_token',
    status_code=HTTP_200_OK,
    response_model=User,
)
def refresh_access_token(
        *,
        refresh_token: str = Body(..., title='Refresh token', embed=True)
):
    """Refresh access token by refresh token."""
    return User(
        username='test_username',
        password='test_password',
    )


@auth_routes.post(
    '/password_reset_request',
    status_code=HTTP_200_OK
)
def password_reset_request(
        *,
        email: EmailStr = Body(..., title='User email', embed=True)
):
    """Make password request by user email"""
    pass


@auth_routes.post(
    '/password_reset/{reset_token}',
    status_code=HTTP_200_OK
)
def password_reset(
        *,
        reset_token: str,
        password: str = Body(
            ..., title='New password', embed=True, min_length=3, max_length=20
        )
):
    """Recovery account (reset password) by reset token"""
    pass
