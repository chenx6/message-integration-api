from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from crud.search import get_search_items
from utils import get_db

router = APIRouter(prefix="/api", tags=["search"])


@router.get("/items", response_model=ItemsResp)
def search_items(text: str, db: Session = Depends(get_db)):
    items = get_search_items(db, text)
    return ItemsResp(status="success", items=items)
