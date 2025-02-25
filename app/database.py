from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

"""
テスト用のデータベース URL
"""
DATABASE_URL = "sqlite:///./test.db"


"""
データベースのセッションを取得する関数
"""
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# database パッケージを使う
database = Database(DATABASE_URL)

# セッション取得関数
async def get_db():
    async with SessionLocal() as session:
        yield session
