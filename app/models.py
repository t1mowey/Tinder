from sqlalchemy import Column, Integer, String
from .database import Base

class Product(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    photo = Column(String)
    link = Column(String)
    brand = Column(String)
    name = Column(String)
    price = Column(String)
    details = Column(String)

    def __repr__(self):
        return (
            f"<Product(id={self.id}, "
            f"photo='{self.photo}', "
            f"link='{self.link}', "
            f"brand='{self.brand}', "
            f"name='{self.name}', "
            f"price='{self.price}', "
            f"details='{self.details}')>"
        )
