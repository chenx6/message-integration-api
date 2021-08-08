from typing import Optional, List
from enum import Enum

from pydantic import BaseModel

from .item import Item


class Zones(Enum):
    EpicFreeGame = 0
    BgmCal = 1
    BiliHotAnime = 2
    RSS = 3
    ZhihuDaily = 4
    ZhihuHot = 5


class Zone(BaseModel):
    name: str
    icon: Optional[str] = None
    items: List[Item] = []

    class Config:
        orm_mode = True
