"""
FastAPIのメインファイル
"""
from fastapi import FastAPI
from app.routers import users, items

# FastAPIのインスタンスを作成
app = FastAPI()

# ルーターを追加
app.include_router(users.router)
app.include_router(items.router)

"""
ルートパスの処理
- app.get("/")はルートパスにアクセスしたときの処理を定義
- ルートパスにアクセスしたときに{"message": "Hello, FastAPI!"}というJSONを返す
- asyncは非同期処理を行うためのもの
"""
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
