# -*- coding:utf-8 -*-
import unittest
import mock


class UsingMockDatetimeTest(unittest.TestCase):
    def _callFUT(self):
        import mydatetime
        return mydatetime.now()

    def test(self):
        # ここでmydatetimeをインポートすると失敗する。
        # AssertionError: datetime.datetime(2012, 9, 5, 10, 42, 3, 984193) != 10
        # import mydatetime 
        with mock.patch("datetime.datetime") as M:
            M.now.return_value = 10
            self.assertEqual(self._callFUT(), 10)

    def test2(self):
        with mock.patch("datetime.datetime") as M:
            M.now.return_value = 11
            # これは結局test で付けたパッチが生きたままになって10を返す。
            self.assertEqual(self._callFUT(), 10)

        # mydatetime.datetimeを置き換えるのがどうやら正解のようだ。
        with mock.patch("mydatetime.datetime") as M:
            M.now.return_value = 11
            self.assertEqual(self._callFUT(), 11)


if __name__ == "__main__":
    unittest.main()
