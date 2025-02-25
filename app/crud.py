"""
crud.pyは、データベースの操作を行うためのファイルです。
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.schemas import UserCreate

"""
ユーザー情報を取得する関数
"""
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

"""
ユーザー情報を追加する関数
"""
async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
