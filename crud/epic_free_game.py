from typing import List

from sqlalchemy.orm import Session

from models.item import Item
from schemas.item import Item as ItemSchemas

from .utils import insert_items


def get_epic_free_game(db: Session):
    """
    从数据库中获取 Epic 家的免费游戏
    TODO: distinct 不干活...
    """
    return (
        db.query(Item)
        .filter(Item.zone_id == 1)
        .distinct(Item.title)
        .order_by(Item.update_time.desc())
        .limit(10)
        .all()
    )


def update_epic_free_game(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中 Epic game 免费游戏数据
    """
    insert_items(db, items)
