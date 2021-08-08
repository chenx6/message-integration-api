from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class Item(BaseModel):
    """返回数据项"""

    title: str  # 标题
    message: str  # 消息，描述
    img: Optional[str] = None  # 图片
    update_time: datetime  # 更新时间
    fetch_time: datetime  # 抓取时间
    url: str  # URL
    zone_id: int  # 分类

    class Config:
        orm_mode = True
