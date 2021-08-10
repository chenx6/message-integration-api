from typing import List

from crud.zone import get_zone_by_type
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.zone import Zone
from schemas.item_resp import ItemsResp
from crud.utils import get_items
from utils import get_db


def gene_router_handler(zone: Zone):
    def rss_route(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        items = get_items(db, zone.id, start, limit)
        return ItemsResp(status="success", items=items)

    return rss_route


def gene_router(tags: List[str], type: int):
    router = APIRouter(tags=tags)
    session: Session = SessionLocal()
    zones = get_zone_by_type(session, type)
    for zone in zones:
        rss_route = gene_router_handler(zone)
        router.add_api_route(zone.api_path, rss_route, response_model=ItemsResp)
    return router
