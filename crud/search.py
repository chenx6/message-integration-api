from sqlalchemy.orm import Session

from models.item import Item


def get_search_items(db: Session, text: str):
    """
    搜索内容
    """
    return (
        db.query(Item)
        .filter(Item.title.like(f"%{text}%"), Item.message.like(f"%{text}%"))
        .all()
    )
