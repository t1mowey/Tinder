from fastapi import FastAPI
from app.routes import items, authorization  # импорт роутера

app = FastAPI()

app.include_router(items.router)
app.include_router(authorization.auth)# подключаем роуты

@app.get("/")
async def root():
    return {"message": "Hello, Tinder!"}
