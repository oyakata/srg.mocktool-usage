==============================
テスト実行結果
==============================

$ python test_with_mox.py

.F
======================================================================
FAIL: test2 (__main__.UsingMoxDatetimeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "build/bdist.linux-i686/egg/mox.py", line 1868, in new_method
    func(self, *args, **kwargs)
  File "test_with_mox.py", line 26, in test2
    self.assertEqual(self._callFUT(), 10)
AssertionError: <mox.MockMethod object at 0x9cf170c> != 10

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (failures=1)


$ python test_with_mox2.py

..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK


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
  File "build/bdist.linux-i686/egg/mox.py", line 1871, in new_method
    mox_obj.UnsetStubs()
  File "build/bdist.linux-i686/egg/mox.py", line 375, in UnsetStubs
    self.stubs.UnsetAll()
  File "build/bdist.linux-i686/egg/stubout.py", line 141, in UnsetAll
    setattr(parent, child_name, old_child)
TypeError: can't set attributes of built-in/extension type 'datetime.datetime'

======================================================================
ERROR: test_builtin_extension2 (__main__.UsingMockDatetimeFailTest)
datetime.nowをモックに置き換えようとするとエラーになる。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "build/bdist.linux-i686/egg/mox.py", line 1871, in new_method
    mox_obj.UnsetStubs()
  File "build/bdist.linux-i686/egg/mox.py", line 375, in UnsetStubs
    self.stubs.UnsetAll()
  File "build/bdist.linux-i686/egg/stubout.py", line 141, in UnsetAll
    setattr(parent, child_name, old_child)
TypeError: can't set attributes of built-in/extension type 'datetime.datetime'

----------------------------------------------------------------------
Ran 2 tests in 0.007s

FAILED (errors=2)
Exception TypeError: "can't set attributes of built-in/extension type 'datetime.datetime'" in <bound method StubOutForTesting.__del__ of <stubout.StubOutForTesting instance at 0xb74232cc>> ignored
Exception TypeError: "can't set attributes of built-in/extension type 'datetime.datetime'" in <bound method StubOutForTesting.__del__ of <stubout.StubOutForTesting instance at 0xb74234ec>> ignored


$ python failcases2.py

F
======================================================================
FAIL: test_import_timing (__main__.UsingMockDatetimeFailTest2)
インポートのタイミングによって結果が変わることを示す例。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "build/bdist.linux-i686/egg/mox.py", line 1868, in new_method
    func(self, *args, **kwargs)
  File "failcases2.py", line 29, in test_import_timing
    self.assertEqual(mydatetime.now(), 10)
AssertionError: datetime.datetime(2012, 9, 6, 14, 3, 6, 526753) != 10

----------------------------------------------------------------------
Ran 1 test in 0.005s

FAILED (failures=1)


$ python failcases3.py

.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
