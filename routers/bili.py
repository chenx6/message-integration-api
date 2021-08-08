from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from crud.bilibili_hot_anime import get_bili_hot_anime
from utils import get_db

router = APIRouter(prefix="/api", tags=["bili"])


@router.get("/bili", response_model=ItemsResp)
def bilibili_hot_anime(start: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    items = get_bili_hot_anime(db, start, limit)
    return ItemsResp(status="success", items=items)
