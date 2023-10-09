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
