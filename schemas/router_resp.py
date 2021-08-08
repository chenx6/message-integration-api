from typing import Optional

from pydantic import BaseModel


class Router(BaseModel):
    """API 的路由"""

    name: str  # 路由名字
    icon: Optional[str] = None  # 图标
    path: str  # 路由路径
