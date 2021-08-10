from datasources.epic_free_game import epic_free_game
from datasources.bili_hot_anime import bili_hot_anime
from datasources.rss_feed import rss_feed
from datasources.zhihu_daily import zhihu_daily
from datasources.zhihu_hot import zhihu_hot

from crud.epic_free_game import update_epic_free_game
from crud.bilibili_hot_anime import update_bili_hot_anime
from crud.rss_feed import update_rss_feed
from crud.zhihu_daily import update_zhihu_daily
from crud.zhihu_hot import update_zhihu_hot
from crud.zone import get_zone_by_type

from database import SessionLocal
from .celery_app import celery_app

# 更新数据的 Celery Worker
@celery_app.task()
def update_epic_free_game_worker():
    items = epic_free_game()
    db = SessionLocal()
    update_epic_free_game(db, items)
    print("Update Epic free game success!")


@celery_app.task()
def update_bili_hot_anime_worker():
    items = bili_hot_anime()
    db = SessionLocal()
    update_bili_hot_anime(db, items)
    print("Update bili_hot_anime success!")


@celery_app.task()
def update_rss_feed_worker():
    db = SessionLocal()
    zones = get_zone_by_type(db, 2)
    for zone in zones:
        items = rss_feed(zone.sub_url, zone.id)
        update_rss_feed(db, items)
        print(f"Update rss feed from {zone.sub_url} success!")


@celery_app.task()
def update_zhihu_daily_worker():
    items = zhihu_daily()
    db = SessionLocal()
    update_zhihu_daily(db, items)
    print(f"Update zhihu daily success!")


@celery_app.task()
def update_zhihu_hot_worker():
    items = zhihu_hot()
    db = SessionLocal()
    update_zhihu_hot(db, items)
    print(f"Update zhihu hot success!")


@celery_app.task()
def period_test():
    print("Working!")
