# -*- coding:utf-8 -*-
import unittest
import datetime

import minimock

# ここでmydatetimeをインポートすると失敗する。
# AssertionError:
#   datetime.datetime(2012, 9, 9, 3, 14, 38, 434506) != 10
# import mydatetime


class UsingMinimockTest(unittest.TestCase):
    def setUp(self):
        datetime.datetime = minimock.Mock(
            "datetime.datetime",
            now=lambda: 10,
        )

    def tearDown(self):
        minimock.restore()

    def test(self):
        import mydatetime
        self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
