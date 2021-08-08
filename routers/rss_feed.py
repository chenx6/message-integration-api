from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from crud.rss_feed import get_rss_feed
from utils import get_db
from datasources.rss_feed import Subscription, subs


router = APIRouter(prefix="/api", tags=["rss_feed"])


def gene_rss_route(sub: Subscription):
    def rss_route(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        items = get_rss_feed(db, sub.identify_url, start, limit)
        return ItemsResp(status="success", items=items)

    return rss_route


for sub in subs:
    rss_route = gene_rss_route(sub)
    router.add_api_route(sub.api_url, rss_route)
