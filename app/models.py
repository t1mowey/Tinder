from sqlalchemy import Column, Integer, String
from app.db.database import Base

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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    token = Column(String)

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"email='{self.email}', "
            f"password='{self.password}', "
            f"token='{self.token}')>"
        )