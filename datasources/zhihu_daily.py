from datetime import datetime

from requests import get
from arrow import get as get_time

from schemas.item import Item
from .utils import HEADERS


def zhihu_daily():
    """
    知乎日报数据源
    """
    resp = get("https://news-at.zhihu.com/api/4/news/latest", headers=HEADERS)
    data = resp.json()
    return [
        Item(
            title=story["title"],
            message=story["hint"],
            img=story["images"][0],
            update_time=get_time(data["date"], "YYYYMMDD").datetime,
            fetch_time=datetime.now(),
            url=story["url"],
            zone_id=3,
        )
        for story in data["stories"]
    ]
