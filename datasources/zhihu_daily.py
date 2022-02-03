from datetime import datetime
from typing import List

from requests import get
from arrow import get as get_time
from sqlalchemy.orm import Session

from .utils import HEADERS
from models.item import Item as ItemModel
from schemas.item import Item as ItemSchemas
from crud.utils import insert_items, count_items


def fetch_zhihu_daily():
    """
    知乎日报数据源
    """
    resp = get("https://news-at.zhihu.com/api/4/news/latest", headers=HEADERS)
    data = resp.json()
    return [
        ItemSchemas(
            title=story["title"],
            message=story["hint"],
            img=story["images"][0],
            update_time=get_time(data["date"], "YYYYMMDD").datetime,
            fetch_time=datetime.now(),
            url=story["url"],
            zone_id=3,
        )
        for story in data["stories"]
    ]


def get_zhihu_daily(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获取知乎日报推送
    """
    filter_ = ItemModel.zone_id == 3
    if count_items(db, start, filter_):
        return []
    return (
        db.query(ItemModel)
        .filter(filter_)
        .order_by(ItemModel.update_time.desc())
        .slice(start, start + limit)
        .all()
    )


def update_zhihu_daily(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中知乎日报推送
    """
    insert_items(db, items)
