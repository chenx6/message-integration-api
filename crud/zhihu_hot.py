from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas

from .utils import insert_items, count_items


def get_zhihu_hot(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获取知乎热榜推送
    """
    filter_ = Item.zone_id == 4
    if count_items(db, start, filter_):
        return []
    return (
        db.query(Item)
        .filter(filter_)
        .order_by(Item.update_time.asc())
        .slice(start, start + limit)
        .all()
    )


def update_zhihu_hot(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中知乎热榜推送。作为热榜会，会删除旧数据
    """
    db.query(Item).filter(Item.zone_id == 4).delete()
    db.commit()
    insert_items(db, items)
