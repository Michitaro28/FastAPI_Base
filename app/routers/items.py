from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def read_items():
    return [{"item_id": 1, "name": "Item A"}, {"item_id": 2, "name": "Item B"}]
