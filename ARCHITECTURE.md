# 架构

## 文件架构

```plaintext
.
├── ARCHITECTURE.md  # 这个文档
├── celery_app       # Celery 相关，用来更新数据
├── celery_beat.sh   # Celery beat 启动脚本
├── celery_worker.sh # Celery worker 启动脚本
├── crud             # CRUD 封装
├── database.py      # 数据库配置
├── datasources      # 数据来源函数，一般是接口封装和爬虫
├── db               # TODO
├── fastapi_run.sh   # FastAPI 启动脚本
├── init_db.py       # 数据库初始化脚本
├── instance         # 数据库文件
├── main.py          # FastAPI 入口
├── models           # sqlalchemy 模型，和 schemas.py 配合
├── requirements.txt # 依赖
├── routers          # FastAPI 路由
├── schemas          # pydantic 模型，和 models.py 配合
└── utils.py         # 工具函数
```

## 逻辑

程序分为2个主进程，一个进程为 Celery 的进程，用于定时任务抓取文章。另一个进程则是 HTTP API，用于提供数据。

Celery 相关的文件在 celery_app 和 datasources 文件夹下，通过将 datasources 中的函数，在 celery_app.worker 中定时调用来存入数据库，更新数据。

HTTP API 相关则是在 routers 和根目录下，用于提供数据。

schemas 和 models 是 pydantic 模型，数据库模型，用于数据的表示，crud 则是 CRUD 数据库操作的封装。

## 添加新数据源

- 在 schemas 添加 Zones 类别
- 在 datasources 添加数据获取函数
- 在 crud 添加数据查询和更新函数
- 在 celery_app 添加定时抓取函数
- 在 routers 添加获取 API，并在 main.py 注册路由

## RSS

在 datasource/rss_feed 的 `subs` 列表中添加相关信息即可。
