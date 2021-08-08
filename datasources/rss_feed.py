from datetime import datetime
from typing import NamedTuple

from feedparser import parse

from schemas.item import Item
from schemas.zone import Zones


class Subscription(NamedTuple):
    name: str  # 订阅名字
    api_url: str  # API 路径名字，不带 `/api`
    sub_url: str  # 订阅 URL，用来获取 RSS 文章
    identify_url: str  # 识别网站链接，用于识别当前订阅的内容


subs = [
    Subscription(
        "cnBeta",
        "/cnbeta",
        "https://www.cnbeta.com/backend.php",
        "https://www.cnbeta.com",
    ),
    Subscription(
        "吾爱破解",
        "/52pojie",
        "https://www.52pojie.cn/forum.php?mod=guide&view=digest&rss=1",
        "https://www.52pojie.cn",
    ),
]


def rss_feed(url: str):
    """
    RSS 数据源
    """
    d = parse(url)
    return [
        Item(
            title=elem.title,
            message=elem.summary,
            update_time=datetime(*elem.published_parsed[:6]),  # type: ignore
            fetch_time=datetime.now(),
            url=elem.link,
            zone_id=Zones.RSS.value,
        )
        for elem in d.entries
    ]
