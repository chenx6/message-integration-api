from datetime import datetime
from typing import List

from feedparser import parse
from sqlalchemy.orm import Session

from schemas.item import Item as ItemModel
from schemas.item import Item as ItemSchemas
from crud.utils import insert_items, get_items


def fetch_rss_feed(url: str, zone_id: int):
    """
    RSS 数据源
    """
    d = parse(url)
    return [
        ItemModel(
            title=elem.title,
            message=elem.summary,
            update_time=datetime(*elem.published_parsed[:6]),  # type: ignore
            fetch_time=datetime.now(),
            url=elem.link,
            zone_id=zone_id,
        )
        for elem in d.entries
    ]


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
