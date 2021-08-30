from celery.schedules import crontab

# 设置时区
timezone = "Asia/Shanghai"
enable_utc = False
# 定时任务，用来更新数据
beat_schedule = {
    "Update epic free game": {
        "task": "celery_app.worker.update_epic_free_game_worker",
        "schedule": crontab(day_of_week="4", hour="8", minute="0"),
        "args": (),
    },
    "Update bili hot anime": {
        "task": "celery_app.worker.update_bili_hot_anime_worker",
        "schedule": crontab(hour="*/3", minute="0"),
        "args": (),
    },
    "Update zhihu daily": {
        "task": "celery_app.worker.update_zhihu_daily_worker",
        "schedule": crontab(hour="6", minute="0"),
        "args": (),
    },
    "Update zhihu hot": {
        "task": "celery_app.worker.update_zhihu_hot_worker",
        "schedule": crontab(hour="*/2", minute="0"),
        "args": (),
    },
    "Update rss feed": {
        "task": "celery_app.worker.update_rss_feed_worker",
        "schedule": crontab(hour="*/1", minute="0"),
        "args": (),
    },
    "Update weixin public": {
        "task": "celery_app.worker.update_weixin_public_worker",
        "schedule": crontab(hour="*/1", minute="0"),
        "args": (),
    },
}
"""
"Execution test": {"task": "celery_app.worker.period_test", "schedule": 60, "args": ()},
"""
