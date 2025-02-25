"""
models.pyはデータベースのテーブルを定義するためのファイルです。
"""
from sqlalchemy import Column, Integer, String
from app.database import Base


"""
users テーブルの定義
- id: ユーザーID
- name: ユーザー名
- email: メールアドレス
- hashed_password: パスワードのハッシュ値
"""
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
