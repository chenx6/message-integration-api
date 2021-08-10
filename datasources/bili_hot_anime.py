"""
API 文档: https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/ranking&dynamic/ranking.md
"""
from datetime import datetime

from requests import get
from arrow import get as get_time

from schemas.item import Item


def bili_hot_anime():
    """
    Bilibili 番剧区热门视频数据源
    """
    resp = get("http://api.bilibili.com/x/web-interface/ranking/region?rid=13&day=7")
    data = resp.json()
    animes = data["data"]
    return [
        Item(
            title=a["title"],
            message=a["description"],
            img=a["pic"],
            update_time=get_time(a["create"], "YYYY-MM-DD HH:mm").datetime,
            fetch_time=datetime.now(),
            url=f'https://www.bilibili.com/video/{a["bvid"]}',
            zone_id=2,
        )
        for a in animes
    ]
