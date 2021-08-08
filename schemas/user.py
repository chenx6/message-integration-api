from typing import List

from pydantic import BaseModel

from .zone import Zone


class User(BaseModel):
    name: str
    password: str
    subscribe_zones: List[Zone]

    class Config:
        orm_mode = True
