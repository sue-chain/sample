#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""老式单元测试，更倾向集成测试
"""

import os
import sys
import tempfile

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from sample.test.mock_test.func import rm


class TestRm(object):


    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp_testfile")

    def setup(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")

    def test_rm(self):
        rm(self.tmpfilepath)
        assert os.path.isfile(self.tmpfilepath) == False
