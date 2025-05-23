from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.db.database import get_db, SessionLocal

from app import models, schema

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/all", response_model=List[schema.ProductRead])
def read_all_items(limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Product).limit(limit).all()
    return items


@router.get('/random', response_model=List[schema.ProductRead])
def read_random_items(limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Product).order_by(func.random()).limit(limit).all()
    return items


@router.post('/action', status_code=status.HTTP_201_CREATED)
def create_action(data: schema.Action, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.token == data.user_token).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user token")
    product = db.query(models.Product).filter(models.Product.uid == data.product_uid).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid product token")

    new_action = models.Action(
        user_token=data.user_token,
        product_uid=data.product_uid,
        action=data.action
    )
    db.add(new_action)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED)




