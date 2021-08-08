from typing import List

from pydantic import BaseModel

from .item import Item


class ItemsResp(BaseModel):
    status: str  # 状态描述
    items: List[Item]
