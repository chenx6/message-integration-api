from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas


def insert_items(db: Session, items: List[ItemSchemas]):
    """
    插入表
    """
    # 当数据在数据库中无重复(URL不同)时才插入
    db_items = [
        Item(**item.dict())
        for item in items
        if db.query(Item).filter(Item.url == item.url).count() == 0
    ]
    db.add_all(db_items)
    db.commit()
    return db_items


def count_items(db: Session, start: int, *filter_):
    """
    通过 `filter_` 过滤，计算数据数量
    """
    cnt = db.query(Item).filter(*filter_).count()
    return start >= cnt
