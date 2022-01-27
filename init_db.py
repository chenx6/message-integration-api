from sqlalchemy.orm.session import Session

from models.item import Item
from models.zone import Zone
from models.user import User
from database import engine, Base, SessionLocal


Base.metadata.create_all(bind=engine)
session: Session = SessionLocal()
zones = [
    Zone(id=1, type=1, name="Epic 白嫖游戏", api_path="/api/epic", sub_url=""),
    Zone(id=2, type=1, name="Bilibili 热门动漫", api_path="/api/bili", sub_url=""),
    Zone(id=3, type=1, name="知乎日报", api_path="/api/zhihu_daily", sub_url=""),
    Zone(id=4, type=1, name="知乎热榜", api_path="/api/zhihu_hot", sub_url=""),
    Zone(
        id=5,
        type=2,
        name="cnBeta",
        api_path="/api/cnbeta",
        sub_url="https://www.cnbeta.com/backend.php",
    ),
    Zone(
        id=6,
        type=2,
        name="吾爱破解",
        api_path="/api/52pojie",
        sub_url="https://www.52pojie.cn/forum.php?mod=guide&view=digest&rss=1",
    ),
    Zone(
        id=7,
        type=3,
        name="Linux News搬运工",
        api_path="/api/lwn_translated",
        sub_url="Linux News搬运工",
    ),
    Zone(
        id=8,
        type=2,
        name="InfoQ",
        api_path="/api/infoq",
        sub_url="https://feed.infoq.com/articles/"
    ),
]
session.add_all(zones)
session.commit()
