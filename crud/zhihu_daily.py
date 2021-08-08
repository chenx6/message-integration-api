from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas
from schemas.zone import Zones

from .utils import insert_items, count_items


def get_zhihu_daily(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获取知乎日报推送
    """
    filter_ = Item.zone_id == Zones.ZhihuDaily.value
    if count_items(db, start, filter_):
        return []
    return (
        db.query(Item)
        .filter(filter_)
        .order_by(Item.update_time.desc())
        .slice(start, start + limit)
        .all()
    )


def update_zhihu_daily(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中知乎日报推送
    """
    insert_items(db, items)
