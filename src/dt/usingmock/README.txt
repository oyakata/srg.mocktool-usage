==============================
テスト実行結果
==============================

単独でテストコードを実行するとOKになる。

$ python test_with_mock.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK


$ python test_with_mock2.py
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK


ところが、両方一度に実行すると失敗する。

$ python -m unittest discover
FF.
======================================================================
FAIL: test (test_with_mock.UsingMockDatetimeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/oyakata/srg.mocktool-usage/src/dt/usingmock/test_with_mock.py", line 14, in test
    self.assertEqual(self._callFUT(), 10)
AssertionError: datetime.datetime(2012, 9, 6, 11, 44, 18, 408965) != 10

======================================================================
FAIL: test2 (test_with_mock.UsingMockDatetimeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/oyakata/srg.mocktool-usage/src/dt/usingmock/test_with_mock.py", line 20, in test2
    self.assertEqual(self._callFUT(), 10)
AssertionError: datetime.datetime(2012, 9, 6, 11, 44, 18, 409808) != 10

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=2)


==============================
失敗例
==============================

$ python failcases.py

EE
======================================================================
ERROR: test_builtin_extension1 (__main__.UsingMockDatetimeFailTest)
datetime.nowをモックに置き換えようとするとエラーになる。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "failcases.py", line 16, in test_builtin_extension1
    with mock.patch("datetime.datetime.now") as M:
  File "build/bdist.linux-i686/egg/mock.py", line 1348, in __enter__
    setattr(self.target, self.attribute, new_attr)
TypeError: can't set attributes of built-in/extension type 'datetime.datetime'

======================================================================
ERROR: test_builtin_extension2 (__main__.UsingMockDatetimeFailTest)
datetime.nowをモックに置き換えようとするとエラーになる。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "failcases.py", line 28, in test_builtin_extension2
    with mock.patch("mydatetime.datetime.now") as M:
  File "build/bdist.linux-i686/egg/mock.py", line 1348, in __enter__
    setattr(self.target, self.attribute, new_attr)
TypeError: can't set attributes of built-in/extension type 'datetime.datetime'

----------------------------------------------------------------------
Ran 2 tests in 0.008s

FAILED (errors=2)


$ python failcases2.py

F
======================================================================
FAIL: test_import_timing (__main__.UsingMockDatetimeFailTest2)
インポートのタイミングによって結果が変わることを示す例。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "failcases2.py", line 29, in test_import_timing
    self.assertEqual(mydatetime.now(), 10)
AssertionError: datetime.datetime(2012, 9, 6, 14, 6, 21, 736866) != 10

----------------------------------------------------------------------
Ran 1 test in 0.018s

FAILED (failures=1)


$ python failcases3.py

.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
