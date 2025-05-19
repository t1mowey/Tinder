from .database import get_db
from app import models, schema

def get_product(db: get_db, product_id: int):
    return (db.query(models.Product)
            .filter(models.Product.id == product_id)
            .first())

def get_products(db: get_db, skip: int = 0, limit: int = 100):
    return (db.query(models.Product)
            .offset(skip).
            limit(limit)
            .all())

def create_product(db: get_db, product: schema.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: get_db, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
