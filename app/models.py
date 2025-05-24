from sqlalchemy import Column, Integer, String, CheckConstraint, TIMESTAMP
from app.db.database import Base

class Product(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    uid = Column(String(64), unique=True, nullable=True, index=True)
    photo = Column(String)
    link = Column(String)
    brand = Column(String)
    name = Column(String)
    price = Column(String)
    details = Column(String)


    def __repr__(self):
        return (
            f"<Product(id={self.id}, "
            f"uid='{self.uid}', "
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


class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_token = Column(String, nullable=False)
    product_uid = Column(String, nullable=False)
    action = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP)
    __table_args__ = (
        CheckConstraint('action IN (0,1)', name='chk_action_flag'),
    )
