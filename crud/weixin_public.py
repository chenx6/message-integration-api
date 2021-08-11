from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas

from .utils import get_items


def get_weixin_public(db: Session, zone_id: int, start: int = 0, limit: int = 10):
    """
    从数据库中获取微信公众号文章
    """
    return get_items(db, zone_id, start, limit)


def update_weixin_public(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中微信公众号文章
    """
    db_items = []
    for item in items:
        query = db.query(Item).filter(
            Item.title == item.title, Item.zone_id == item.zone_id
        )
        if query.count() != 0:
            query.delete()
        db_items.append(Item(**item.dict()))
    db.add_all(db_items)
    db.commit()
