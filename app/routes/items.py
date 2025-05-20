from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db

from app import models, schema

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[schema.ProductRead])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(models.Product).limit(limit).all()
    return items



