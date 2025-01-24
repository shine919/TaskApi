from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str
    user_email: EmailStr | None = None


class User(UserBase):
    id: int


class UserCreate(UserBase):
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserCreate):
    pass


class UserUpdatePatch(UserCreate):
    username: str | None = None
    password: str | None = None
    user_email: EmailStr | None = None
