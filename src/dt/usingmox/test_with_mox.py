# -*- coding:utf-8 -*-
import unittest
from datetime import datetime
import mox


"""
moxとmockだったらmockの方が良さそうだ。

理由は

1. moxは必ずReplayAll(, VerifyAll)を要求される。
   mockはわざわざリプレイモードに切り替える必要がない。
   また、Verifyは必要だと思ったときだけ利用可能。
2. デコレータやコンテキストマネージャの方が
   Replay/Verifyを明示的に切り替えるよりもわかりやすい。
"""

class UsingMoxTest(unittest.TestCase):
    def setUp(self):
        now = datetime(2000, 1, 18, 16, 33, 28)
        def fake():
            return now
        self.now = now

        self.mox = mox.Mox()
        # self.mox.stubs.Set(datetime, "now", fake)
        import datetime as dt
        self.mox.StubOutWithMock(dt, "datetime")
        self.datetime = dt

    def test(self):
        import fut
        self.datetime.datetime.now().AndReturn(self.now)
        self.mox.ReplayAll()
        self.assertEqual(fut.now(), self.now)
        self.mox.VerifyAll()
