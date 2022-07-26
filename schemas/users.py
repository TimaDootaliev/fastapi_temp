from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    nickname: str
    email: str
    password: str


class UserSchema(BaseModel):
    nickname: str
    email: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
