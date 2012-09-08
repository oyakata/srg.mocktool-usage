# -*- coding:utf-8 -*-
import unittest
import mox

import mydatetime


class UsingMoxDatetimeTest2(mox.MoxTestBase):
    def tearDown(self):
        self.mox.ResetAll()

    def _callFUT(self):
        return mydatetime.now()

    def test(self):
        self.mox.StubOutWithMock(mydatetime, "datetime")
        mydatetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        self.assertEqual(self._callFUT(), 10)

    def test2(self):
        """mydatetime.datetimeをモックに置き換えると問題が起きないことを示す例。

        test_with_mox.pyと同じ内容のメソッドが2つあるのに、
        こちらの方法では結果がOKになる。
        """
        self.mox.StubOutWithMock(mydatetime, "datetime")
        mydatetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        self.assertEqual(self._callFUT(), 10)


if __name__ == "__main__":
    unittest.main()
