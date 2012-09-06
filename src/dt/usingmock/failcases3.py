# -*- coding:utf-8 -*-
import unittest
import mock


class UsingMockDatetimeFailTest3(unittest.TestCase):
    def test_import_timing(self):
        """インポートのタイミングによって結果が変わることを示す例。

        こちらはモックがうまく適用される。

        前提: mydatetimeがdatetimeをインポートする。

        1. datetime.datetimeをモックと置き換える。
        2. mydatetimeをインポートする。
        3. mydatetimeの中でdatetimeがインポートされる。
           (この時点で既にdatetime.datetimeはモックに置き換わっている。)
        4. モックに置き換えられたのdatetime.nowを使うのでテストは成功する。

        NOTE: 正解はインポートのタイミングを変えることではなくて、
              mydatetime.datetimeにモックを適用することなので注意。
              (datetime.datetimeを対象にしない)
        """
        with mock.patch("datetime.datetime") as M:
            M.now.return_value = 10
            import mydatetime
            self.assertEqual(mydatetime.now(), 10)


if __name__ == "__main__":
    unittest.main()
