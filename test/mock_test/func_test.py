# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""rm test
"""

__authors__ = ['"sue.chain" <sue.chain@gmail.com>']

import os
import sys
import mock
from nose.tools import assert_raises, raises, set_trace, nottest

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from sample.test.mock_test.func import rm


class TestFunc(object):
    """
    func test
    """

    @mock.patch('sample.test.mock_test.func.os.path')
    @mock.patch('sample.test.mock_test.func.os')
    def test_rm_1(self, mock_os, mock_path):
        """
        装饰器从下往上执行，依次赋值给mock_os, mock_path
        """
        mock_path.isfile.return_value = True
        rm("any file")
        assert mock_os.remove.called == True
        assert mock_os.remove.call_args[0][0] == "any file"
        rm("any file")
        assert mock_os.remove.call_args_list

        mock_os.reset_mock()
        mock_path.reset_mock()
        mock_path.isfile.return_value = False
        result = rm("any file")
        assert result == "error"
        assert mock_os.remove.called == False

