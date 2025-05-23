from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class ProductBase(BaseModel):
    uid: Optional[str]
    photo: Optional[str]
    link: Optional[str]
    brand: Optional[str]
    name: Optional[str]
    price: Optional[str]
    details: Optional[str]


class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    password: str


class Action(BaseModel):
    user_token:  str
    product_uid: str
    action: conint(ge=0, le=1)

    class Config:
        orm_mode = True



