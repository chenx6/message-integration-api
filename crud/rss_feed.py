from typing import List

from sqlalchemy.orm import Session

from schemas.item import Item as ItemSchemas

from .utils import insert_items, get_items


def get_rss_feed(db: Session, zone_id: int, start: int = 0, limit: int = 10):
    """
    从数据库中获取 RSS 推送
    """
    return get_items(db, zone_id, start, limit)


def update_rss_feed(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中 RSS 推送
    """
    insert_items(db, items)
