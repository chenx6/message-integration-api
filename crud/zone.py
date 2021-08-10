from sqlalchemy.orm import Session

from models.zone import Zone


def get_zones(db: Session):
    """
    获取 API 路由
    """
    return db.query(Zone).all()


def get_zone_by_type(db: Session, type: int):
    return db.query(Zone).filter(Zone.type == type).all()
