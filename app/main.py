from fastapi import FastAPI
from app.routes import items  # импорт роутера

app = FastAPI()

app.include_router(items.router)  # подключаем роуты

@app.get("/")
async def root():
    return {"message": "Hello, Tinder!"}
