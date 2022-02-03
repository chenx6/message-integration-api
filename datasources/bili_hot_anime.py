"""
API 文档: https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/ranking&dynamic/ranking.md
"""
from datetime import datetime
from typing import List

from requests import get
from arrow import get as get_time
from sqlalchemy.orm import Session

from models.item import Item as ItemModel
from schemas.item import Item as ItemSchemas
from crud.utils import count_items, insert_items


def fetch_bili_hot_anime():
    """
    Bilibili 番剧区热门视频数据源
    """
    resp = get("http://api.bilibili.com/x/web-interface/ranking/region?rid=13&day=7")
    data = resp.json()
    animes = data["data"]
    return [
        ItemSchemas(
            title=a["title"],
            message=a["description"],
            img=a["pic"],
            update_time=get_time(a["create"], "YYYY-MM-DD HH:mm").datetime,
            fetch_time=datetime.now(),
            url=f'https://www.bilibili.com/video/{a["bvid"]}',
            zone_id=2,
        )
        for a in animes
    ]


def get_bili_hot_anime(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获得 Bilibili 番剧区热门
    """
    filter_ = ItemModel.zone_id == 2
    # 查询起点是否超过数据库中数据数量时，返回空列表表示数据库中无多余数据
    if count_items(db, start, filter_):
        return []
    return db.query(ItemModel).filter(filter_).slice(start, start + limit).all()


def update_bili_hot_anime(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中 Bilibili 番剧区热门
    需要注意的是只保存当前热门数据，得删除之前数据才插入更新数据
    """
    db.query(ItemModel).filter(ItemModel.zone_id == 2).delete()
    db.commit()
    insert_items(db, items)
