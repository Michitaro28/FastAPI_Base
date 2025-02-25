"""
users.pyはユーザー情報に関するAPIを定義するためのファイルです。
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserCreate, UserRead
from app.crud import create_user, get_users

"""
APIRouterを使ってルーターを作成
- prefixはURLの接頭辞
- tagsはSwagger UIに表示されるタグ
    - この場合は「users」タグ
    - Swagger UIはタグごとにAPIをグループ化する
"""
router = APIRouter(prefix="/users", tags=["users"])

"""
/users/ にアクセスしたときの処理
- response_modelはレスポンスのスキーマを指定
- ユーザー情報を取得して返す
"""
@router.get("/", response_model=list[UserRead])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


"""
/users/ にPOSTリクエストがあったときの処理
- response_modelはレスポンスのスキーマを指定
- ユーザー情報を追加して返す
"""

@router.post("/", response_model=UserRead)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
