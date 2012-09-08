# -*- coding:utf-8 -*-
import unittest
import datetime
import minimock



class UsingMinimockTest(unittest.TestCase):
    def setUp(self):
        minimock.mock("datetime.datetime.now", returns=10)

    def tearDown(self):
        minimock.restore()

    def test(self):
        self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
