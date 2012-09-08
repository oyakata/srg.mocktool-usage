# -*- coding:utf-8 -*-
import unittest
import mox


class UsingMockDatetimeFailTest3(mox.MoxTestBase):
    def test_import_timing(self):
        """インポートのタイミングによって結果が変わることを示す例。

        こちらはモックがうまく適用される。

        前提: mydatetimeがdatetimeをインポートする。

        1. datetimeをインポートする。
        2. datetime.datetimeをモックと置き換える。
        3. mydatetimeをインポートする。
        4. mydatetimeの中でdatetimeがインポートされる。
           (この時点で既にdatetime.datetimeはモックに置き換わっている。)
        5. モックに置き換えられたのdatetime.nowを使うのでテストは成功する。

        NOTE: 正解はインポートのタイミングを変えることではなくて、
              mydatetime.datetimeにモックを適用することなので注意。
              (datetime.datetimeを対象にしない)
        """
        import datetime
        self.mox.StubOutWithMock(datetime, "datetime")
        import mydatetime  # StubOutWithMockの前にインポートするとモックが当たらない。
        datetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
