from fastapi import FastAPI

from api.routers import task

app = FastAPI()

app.include_router(task.router)
# app.include_router(done.router)


# @app.get('/')
# async def index():  # 型指定でバリデーションができる
#     return {"message": "index!!"}
