from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from ..database import get_db

from app import models, schema

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/all", response_model=List[schema.ProductRead])
def read_all_items(limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Product).limit(limit).all()
    print("🔥 Деплой сработал!")
    return items


@router.get('/random', response_model=List[schema.ProductRead])
def read_random_items(limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Product).order_by(func.random()).limit(limit).all()
    return items




