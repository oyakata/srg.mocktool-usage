# -*- coding:utf-8 -*-
import unittest
import minimock

import mydatetime


class UsingMinimockTest(unittest.TestCase):
    def setUp(self):
        minimock.mock("mydatetime.now", returns=10)

    def tearDown(self):
        minimock.restore()

    def test(self):
        self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
