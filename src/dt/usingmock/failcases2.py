# -*- coding:utf-8 -*-
import unittest
import mock


class UsingMockDatetimeFailTest2(unittest.TestCase):
    def test_import_timing(self):
        """インポートのタイミングによって結果が変わることを示す例。

        前提: mydatetimeがdatetimeをインポートする。

        1. mydatetimeをインポートする。
        2. mydatetimeの中でdatetimeがインポートされる。
        3. datetime.datetimeをモックと置き換える。
        4. 2のdatetimeと3のdatetimeは別扱いなので
           mydatetime.datetimeを利用するmydatetime.nowはモックを見ない。
        5. モックに置き換えられる前のdatetime.nowを使うのでテストが失敗する。

        NOTE: 正解はインポートのタイミングを変えることではなくて、
              mydatetime.datetimeにモックを適用することなので注意。
              (datetime.datetimeを対象にしない)
        """
        # ここでmydatetimeをインポートすると失敗する。
        # AssertionError:
        #   datetime.datetime(2012, 9, 5, 10, 42, 3, 984193) != 10
        import mydatetime
        with mock.patch("datetime.datetime") as M:
            M.now.return_value = 10
            self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
