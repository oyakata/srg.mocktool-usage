# -*- coding:utf-8 -*-
import unittest
import mock

import mydatetime


class UsingMockDatetimeFailTest(unittest.TestCase):
    def test_builtin_extension1(self):
        """datetime.nowをモックに置き換えようとするとエラーになる。

        nowではなくdatetimeの方を置き換えるのが正解。
        """
        # TypeError: can't set attributes of
        #            built-in/extension type 'datetime.datetime'
        with mock.patch("datetime.datetime.now") as M:
            M.return_value = 77
            self.assertEqual(mydatetime.now(), 77)

    def test_builtin_extension2(self):
        """datetime.nowをモックに置き換えようとするとエラーになる。

        mydatetimeに所属するdatetime.nowでも
        結局のところ組み込みのdatetime.nowを指すのでやはりエラーになる。
        """
        # TypeError: can't set attributes
        #            of built-in/extension type 'datetime.datetime'
        with mock.patch("mydatetime.datetime.now") as M:
            M.return_value = 77
            self.assertEqual(mydatetime.now(), 77)


if __name__ == "__main__":
    unittest.main()
