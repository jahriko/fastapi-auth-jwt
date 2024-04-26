from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
