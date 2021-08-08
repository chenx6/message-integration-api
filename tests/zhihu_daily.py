from unittest import TestCase, main

from database import SessionLocal
from datasources import zhihu_daily
from crud.zhihu_daily import get_zhihu_daily


class ZhihuDaily(TestCase):
    def datasource_test(self):
        items = zhihu_daily()
        self.assertTrue(len(items) != 0)

    def crud_test(self):
        session = SessionLocal()
        items = get_zhihu_daily(session)
        self.assertIsInstance(items, list)


if __name__ == "__main__":
    main()
