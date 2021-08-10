from crud.zone import get_zone_by_type
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.zone import Zone
from schemas.item_resp import ItemsResp
from crud.rss_feed import get_rss_feed
from utils import get_db


router = APIRouter(tags=["rss_feed"])


def gene_rss_route(zone: Zone):
    def rss_route(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        items = get_rss_feed(db, zone.id, start, limit)
        return ItemsResp(status="success", items=items)

    return rss_route


session: Session = SessionLocal()
zones = get_zone_by_type(session, 2)
for zone in zones:
    rss_route = gene_rss_route(zone)
    router.add_api_route(zone.api_path, rss_route, response_model=ItemsResp)
