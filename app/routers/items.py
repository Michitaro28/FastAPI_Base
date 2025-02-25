"""
items.pyは、itemsに関するAPIを定義するためのファイルです。
"""
from fastapi import APIRouter


"""
APIRouterを使ってルーターを作成
- prefixはURLの接頭辞
- tagsはSwagger UIに表示されるタグ
    - この場合は「items」タグ
    - Swagger UIはタグごとにAPIをグループ化する
"""
router = APIRouter(prefix="/items", tags=["items"])

"""
/items/ にアクセスしたときの処理
- ダミーのアイテム情報を返す
"""
@router.get("/")
async def read_items():
    return [{"item_id": 1, "name": "Item A"}, {"item_id": 2, "name": "Item B"}]
