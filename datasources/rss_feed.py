from datetime import datetime

from feedparser import parse

from schemas.item import Item


def rss_feed(url: str, zone_id: int):
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
            zone_id=zone_id,
        )
        for elem in d.entries
    ]
