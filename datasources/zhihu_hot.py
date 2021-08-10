from datetime import datetime
from json import loads

from requests import get
from arrow import get as get_time
from bs4 import BeautifulSoup

from schemas.item import Item
from .utils import HEADERS


def zhihu_hot():
    """
    知乎热榜数据源
    """
    resp = get("https://www.zhihu.com/billboard", headers=HEADERS)
    soup = BeautifulSoup(resp.text, features="html.parser")
    script = soup.find("script", id="js-initialData")
    data = loads(script.string)  # type: ignore
    hot_list = data["initialState"]["topstory"]["hotList"]
    return [
        Item(
            title=item["titleArea"]["text"],
            message=item["excerptArea"]["text"],
            img=item["imageArea"]["url"],
            update_time=datetime.now(),
            fetch_time=datetime.now(),
            url=item["link"]["url"],
            zone_id=4,
        )
        for item in map(lambda x: x["target"], hot_list)
    ]
