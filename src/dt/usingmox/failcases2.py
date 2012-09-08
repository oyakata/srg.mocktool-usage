# -*- coding:utf-8 -*-
import unittest
import mox


class UsingMockDatetimeFailTest2(mox.MoxTestBase):
    def test_import_timing(self):
        """インポートのタイミングによって結果が変わることを示す例。

        前提: mydatetimeがdatetimeをインポートする。

        1. datetimeをインポートする。
        2. mydatetimeをインポートする。
        3. mydatetimeの中でdatetimeがインポートされる。
        4. datetime.datetimeをモックと置き換える。
        5. 2のdatetimeと3のdatetimeは別扱いなので
           mydatetime.datetimeを利用するmydatetime.nowはモックを見ない。
        6. モックに置き換えられる前のdatetime.nowを使うのでテストが失敗する。

        NOTE: 正解はインポートのタイミングを変えることではなくて、
              mydatetime.datetimeにモックを適用することなので注意。
              (datetime.datetimeを対象にしない)
        """
        import datetime
        import mydatetime
        self.mox.StubOutWithMock(datetime, "datetime")
        datetime.datetime.now().AndReturn(10)
        self.mox.ReplayAll()
        self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
