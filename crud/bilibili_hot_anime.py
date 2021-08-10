from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas

from .utils import count_items, insert_items


def get_bili_hot_anime(db: Session, start: int = 0, limit: int = 10):
    """
    从数据库中获得 Bilibili 番剧区热门
    """
    filter_ = Item.zone_id == 2
    # 查询起点是否超过数据库中数据数量时，返回空列表表示数据库中无多余数据
    if count_items(db, start, filter_):
        return []
    return db.query(Item).filter(filter_).slice(start, start + limit).all()


def update_bili_hot_anime(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中 Bilibili 番剧区热门
    需要注意的是只保存当前热门数据，得删除之前数据才插入更新数据
    """
    db.query(Item).filter(Item.zone_id == 2).delete()
    db.commit()
    insert_items(db, items)
