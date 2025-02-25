from fastapi import FastAPI
from app.routers import users, items

app = FastAPI()

# ルーターを追加
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
