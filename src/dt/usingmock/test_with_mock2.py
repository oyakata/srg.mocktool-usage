# -*- coding:utf-8 -*-
import unittest
import mock

import mydatetime


class UsingMockDatetimeTest2(unittest.TestCase):
    def test(self):
        # mydatetime.datetimeにパッチを当てるなら
        # mydatetimeをトップレベルでインポートしても大丈夫。
        # やはりdatetime.datetimeに手を入れるのが間違いのようだ。
        with mock.patch("mydatetime.datetime") as M:
            M.now.return_value = 10
            self.assertEqual(mydatetime.now(), 10)

        # nowをモックに置き換えようとするとエラーになる。
        # nowではなくdatetimeの方を置き換えるのが正解。
        with self.assertRaises(TypeError):
            # TypeError:
            #   can't set attributes of
            #   built-in/extension type 'datetime.datetime'
            with mock.patch("datetime.datetime.now") as M2:
                M2.return_value = 77
                self.assertEqual(mydatetime.now(), 77)

        with self.assertRaises(TypeError):
            # TypeError:
            #   can't set attributes
            #   of built-in/extension type 'datetime.datetime'
            with mock.patch("mydatetime.datetime.now") as M3:
                M3.return_value = 77
                self.assertEqual(mydatetime.now(), 77)


if __name__ == "__main__":
    unittest.main()
