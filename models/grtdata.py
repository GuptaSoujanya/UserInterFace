from pydantic import BaseModel,EmailStr


class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr