from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from datasources.zhihu_hot import get_zhihu_hot
from utils import get_db


router = APIRouter(prefix="/api", tags=["zhihu_hot"])


@router.get("/zhihu_hot")
def zhihu_hot(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_zhihu_hot(db, start, limit)
    return ItemsResp(status="success", items=items)
