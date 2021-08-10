from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from routers import bili, epic, zhihu_daily, zhihu_hot, rss_feed
from crud.zone import get_zones
from utils import get_db
from schemas.zone import Zone

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


@app.get("/api/routers", response_model=List[Zone])
async def routers(db: Session = Depends(get_db)):
    """
    API 路由
    """
    routers = get_zones(db)
    return routers


"""
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
