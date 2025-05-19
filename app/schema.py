from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    photo: Optional[str]
    link: Optional[str]
    brand: Optional[str]
    name: Optional[str]
    price: Optional[str]
    details: Optional[str]


class ProductCreate(ProductBase):
    pass  # если надо, можно добавить обязательные поля при создании

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True  # чтобы можно было возвращать ORM-модели напрямую
