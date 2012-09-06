# -*- coding:utf-8 -*-
import datetime
import unittest
import mox


class UsingMoxDatetimeTest(mox.MoxTestBase):
    def tearDown(self):
        self.mox.ResetAll()

    def _callFUT(self):
        import mydatetime
        return mydatetime.now()

    def test(self):
        self.mox.StubOutWithMock(datetime, "datetime")
        datetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        self.assertEqual(self._callFUT(), 10)

    def test2(self):
        self.mox.StubOutWithMock(datetime, "datetime")
        datetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        # AssertionError: <mox.MockMethod object at 0xb739676c> != 10
        self.assertEqual(self._callFUT(), 10)


if __name__ == "__main__":
    unittest.main()
