from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from typing import List
from time import time

from app.db.database import get_db
from app import models, schema

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/all", response_model=List[schema.ProductRead])
async def read_all_items(limit: int = 100, db: AsyncSession = Depends(get_db)):
    items = (await db.execute(
        select(models.Product).
        limit(limit)
    )
             ).scalars().all()
    return items


@router.get('/random', response_model=List[schema.ProductRead])
async def read_random_items(limit: int = 100, db: AsyncSession = Depends(get_db)):
    items = (await db.execute(
        select(models.Product).
        order_by(func.random()).
        limit(limit)
                              )
             ).scalars().all()
    return items


@router.post('/action', status_code=status.HTTP_201_CREATED)
async def create_action(data: schema.Action, db: AsyncSession = Depends(get_db)):
    user = (await db.execute(
        select(models.User).
        filter(models.User.token == data.user_token)
    )
            ).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user token")
    product = (await db.execute(
        select(models.Product).
        filter(models.Product.uid == data.product_uid)
    )
               ).scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid product token")

    new_action = models.Action(
        user_token=data.user_token,
        product_uid=data.product_uid,
        action=data.action,
        timestamp=time()
    )
    db.add(new_action)
    await db.commit()
    return Response(status_code=status.HTTP_201_CREATED)


@router.get('/random_recs', status_code=200)
async def get_random_recommendations(token: str, limit: int = 5, db: AsyncSession = Depends(get_db)):
    user_actions = (await db.execute(
                    select(models.Action)
                    .filter(models.Action.user_token == token)
                    )).scalars().all()
    user_views = [i.product_uid for i in user_actions]
    recs = (await db.execute(
            select(models.Product)
            .filter(~models.Product.uid.in_(user_views))
            .order_by(func.random())
            .limit(limit)
            )).scalars().all()
    return recs
