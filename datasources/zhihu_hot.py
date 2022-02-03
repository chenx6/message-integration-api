from datetime import datetime
from json import loads
from typing import List

from requests import get
from arrow import get as get_time
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from .utils import HEADERS
from models.item import Item as ItemModel
from schemas.item import Item as ItemSchemas
from crud.utils import insert_items, count_items


def fetch_zhihu_hot():
    """
    知乎热榜数据源
    """
    resp = get("https://www.zhihu.com/billboard", headers=HEADERS)
    soup = BeautifulSoup(resp.text, features="html.parser")
    script = soup.find("script", id="js-initialData")
    data = loads(script.string)  # type: ignore
    hot_list = data["initialState"]["topstory"]["hotList"]
    return [
        ItemSchemas(
            title=item["titleArea"]["text"],
            message=item["excerptArea"]["text"],
            img=item["imageArea"]["url"],
            update_time=datetime.now(),
            fetch_time=datetime.now(),
            url=item["link"]["url"],
            zone_id=4,
        )
        for item in map(lambda x: x["target"], hot_list)
    ]


def get_zhihu_hot(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获取知乎热榜推送
    """
    filter_ = ItemModel.zone_id == 4
    if count_items(db, start, filter_):
        return []
    return (
        db.query(ItemModel)
        .filter(filter_)
        .order_by(ItemModel.update_time.asc())
        .slice(start, start + limit)
        .all()
    )


def update_zhihu_hot(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中知乎热榜推送。作为热榜会，会删除旧数据
    """
    db.query(ItemModel).filter(ItemModel.zone_id == 4).delete()
    db.commit()
    insert_items(db, items)
