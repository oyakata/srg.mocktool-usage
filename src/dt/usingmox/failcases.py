# -*- coding:utf-8 -*-
import unittest
import mox
import datetime

import mydatetime


class UsingMockDatetimeFailTest(mox.MoxTestBase):
    def test_builtin_extension1(self):
        """datetime.nowをモックに置き換えようとするとエラーになる。

        nowではなくdatetimeの方を置き換えるのが正解。
        """
        # TypeError: can't set attributes of
        #            built-in/extension type 'datetime.datetime'
        self.mox.StubOutWithMock(datetime.datetime, "now")
        datetime.datetime.now().AndReturn(77)
        self.mox.ReplayAll()
        self.assertEqual(mydatetime.now(), 77)

    def test_builtin_extension2(self):
        """datetime.nowをモックに置き換えようとするとエラーになる。

        mydatetimeに所属するdatetime.nowでも
        結局のところ組み込みのdatetime.nowを指すのでやはりエラーになる。
        """
        # TypeError: can't set attributes
        #            of built-in/extension type 'datetime.datetime'
        self.mox.StubOutWithMock(mydatetime.datetime, "now")
        mydatetime.datetime.now().AndReturn(77)
        self.mox.ReplayAll()
        self.assertEqual(mydatetime.now(), 77)


if __name__ == "__main__":
    unittest.main()
