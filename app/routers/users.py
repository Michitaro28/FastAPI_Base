from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserCreate, UserRead
from app.crud import create_user, get_users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

@router.post("/", response_model=UserRead)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
