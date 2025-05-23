from pydantic import BaseModel, EmailStr
from typing import Optional

class ProductBase(BaseModel):
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
