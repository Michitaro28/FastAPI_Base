"""
test_main.pyは、main.pyのテストを行うためのファイルです。
"""
from fastapi.testclient import TestClient
from app.main import app

"""
TestClientを使ってFastAPIのテストを行う
- app: テスト対象のFastAPIインスタンス
"""
client = TestClient(app)


"""
test_read_root関数
- ルートパスにアクセスしたときのテスト
- レスポンスのステータスコードが200であること
- レスポンスのJSONが{"message": "Hello, FastAPI!"}であること
"""
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
