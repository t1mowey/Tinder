from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.db.database import get_db
from app import schema
from app.models import User
from pydantic import EmailStr, ValidationError
from passlib.hash import bcrypt
import secrets

def generate_token() -> str:
    return secrets.token_hex(32)


def hash_pass(password: str):
    hashed = bcrypt.hash(password)
    return hashed


auth = APIRouter(tags=["auth"])

@auth.post('/register')
def reg_user(data: schema.User, db = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    hashed_pass = hash_pass(data.password)
    token = generate_token()
    new_user = User(email=data.email,
                    password=hashed_pass,
                    token=token)
    db.add(new_user)
    db.commit()
    return JSONResponse(
        content={"token": token},
        status_code=201
    )


# @auth.post("/login")
# def authorization(auth: schema.User, db = Depends(get_db)):
#     user = db.query(models.User).filter(User.email == auth.email) ###TODO
#     pass

