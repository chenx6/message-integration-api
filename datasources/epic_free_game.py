from datetime import datetime

from requests import get
from arrow import get as get_time

from schemas.item import Item


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
    return Item(
        title=title,
        message=message,
        img=elem["keyImages"][0]["url"],
        update_time=get_time(elem["effectiveDate"]).datetime,
        fetch_time=datetime.now(),
        url=f'https://www.epicgames.com/store/zh-CN/p/{elem["productSlug"]}',
        zone_id=1,
    )


def epic_free_game():
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
