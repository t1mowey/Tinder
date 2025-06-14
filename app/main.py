from fastapi import FastAPI
from app.routes import items, authorization  # импорт роутера

app = FastAPI(root_path="/api")

app.include_router(items.router)
app.include_router(authorization.auth)# подключаем роуты

@app.get("/")
async def root():
    return {"message": "Hello, check /docs to see all the routes."}


@app.get("/deploy_ok")
async def test_deploy():
    return {'message': 'OK'}
