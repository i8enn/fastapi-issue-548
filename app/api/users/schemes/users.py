"""Schemes for users/auth API"""
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    """User scheme (without id)"""
    username: str = Field(None, title='username', min_length=3, max_length=20)
    email: EmailStr = Field(None, title='email')
    first_name: str = Field(None, min_length=2, max_length=20)
    last_name: str = Field(None, min_length=2, max_length=20)
    is_active: bool = Field(None, title='is_active')
