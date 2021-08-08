from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import bili, epic, zhihu_daily, zhihu_hot, rss_feed
from schemas.router_resp import Router
from datasources.rss_feed import subs

app = FastAPI()

# 路由配置
app.include_router(bili.router)
app.include_router(epic.router)
app.include_router(zhihu_daily.router)
app.include_router(zhihu_hot.router)
app.include_router(rss_feed.router)

# CORS 配置
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/status")
async def status():
    """
    在，看下后端崩了没有
    """
    return {"status": "working"}


@app.get("/api/routers", response_model=List[Router])
async def routers():
    """
    API 路由
    """
    basic = [
        Router(name="Epic 白嫖游戏", path="/api/epic"),
        Router(name="Bilibili 热门动漫", path="/api/bili"),
        Router(name="知乎日报", path="/api/zhihu_daily"),
        Router(name="知乎热榜", path="/api/zhihu_hot"),
    ]
    basic += [Router(name=sub.name, path=f"/api{sub.api_url}") for sub in subs]
    return basic


"""
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
