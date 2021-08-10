from typing import Optional, List
from enum import Enum

from pydantic import BaseModel

from .item import Item


class Zone(BaseModel):
    name: str
    type: int
    api_path: str
    sub_url: str
    icon: Optional[str] = None

    class Config:
        orm_mode = True
