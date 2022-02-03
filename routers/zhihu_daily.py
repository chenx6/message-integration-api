from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from datasources.zhihu_daily import get_zhihu_daily
from utils import get_db


router = APIRouter(prefix="/api", tags=["zhihu_daily"])


@router.get("/zhihu_daily")
def zhihu_daily(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_zhihu_daily(db, start, limit)
    return ItemsResp(status="success", items=items)
