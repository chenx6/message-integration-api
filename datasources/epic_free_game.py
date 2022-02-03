from datetime import datetime
from typing import List

from requests import get
from arrow import get as get_time
from sqlalchemy.orm import Session

from models.item import Item as ItemModel
from schemas.item import Item as ItemSchemas
from crud.utils import insert_items


def filter_free_game(elem):
    """
    根据价格来过滤出真正免费的作品
    """
    total_price = elem["price"]["totalPrice"]
    return total_price["discountPrice"] == 0 and total_price["originalPrice"] != 0


def gene_info(elem):
    """
    生成 Item 数据
    """
    title = f"{elem['title']} 可以白嫖"
    prom_data = elem["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]
    message = f"开始于 {prom_data['startDate']}，结束于 {prom_data['endDate']}"
    return ItemSchemas(
        title=title,
        message=message,
        img=elem["keyImages"][0]["url"],
        update_time=get_time(elem["effectiveDate"]).datetime,
        fetch_time=datetime.now(),
        url=f'https://www.epicgames.com/store/zh-CN/p/{elem["productSlug"]}',
        zone_id=1,
    )


def fetch_epic_free_game():
    """
    获取 Epic game 免费游戏
    """
    resp = get(
        "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN,JP"
    )
    data = resp.json()
    elem = data["data"]["Catalog"]["searchStore"]["elements"]
    selected = filter(filter_free_game, elem)
    gened = map(gene_info, selected)
    return list(gened)


def get_epic_free_game(db: Session):
    """
    从数据库中获取 Epic 家的免费游戏
    TODO: distinct 不干活...
    """
    return (
        db.query(ItemModel)
        .filter(ItemModel.zone_id == 1)
        .distinct(ItemModel.title)
        .order_by(ItemModel.update_time.desc())
        .limit(10)
        .all()
    )


def update_epic_free_game(db: Session, items: List[ItemSchemas]):
    """
    更新数据库中 Epic game 免费游戏数据
    """
    insert_items(db, items)
