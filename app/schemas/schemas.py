from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    user_email: str
    user_firstname: str
    user_lastname: str
    user_status: str
    user_city: str
    user_phone: str
    user_links: str
    user_avatar: str
    hashed_password: str
    is_superuser: bool


class SignInRequest(BaseModel):
    user_email: str
    hashed_password: str


class SignUpRequest(UserSchema):
    pass


class UserUpdateRequest(UserSchema):
    pass


class User(UserSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class UsersListResponse(BaseModel):
    users: list[User]
    total_count: int


class UserDetailResponse(BaseModel):
    user: User
