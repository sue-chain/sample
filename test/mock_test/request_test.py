# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""request test
"""

__authors__ = ['"sue.chain" <sue.chain@gmail.com>']

import os
import sys
import mock
from requests import Response
from mock import MagicMock, Mock
from nose.tools import assert_raises, raises, set_trace, nottest

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from sample.test.mock_test.func import request


class TestFunc(object):
    """
    func test
    """

    @mock.patch('sample.test.mock_test.func.requests')
    def test_request(self, mock_requests):
        """
        """
        url = "http://192.168.6.182:8100/api/site/list"
        mock_resp = MagicMock(spec=Response)
        mock_requests.get.return_value = mock_resp
        mock_resp.ok.return_value = True
        mock_resp.json.return_value= {"msg": "Success", "body": [{}]}
        result = request(url)
        # 结果检查
        assert len(result) > 0
        ## 调用检查
        ## 参数检查
        assert mock_requests.get.called
        assert mock_requests.get.call_count == 1
        assert mock_requests.get.call_args[0][0] == url
        assert len(mock_requests.get.call_args_list) == 1
        assert mock_requests.get.assert_called_with(call(url))
        result = request(url)
        assert len(mock_requests.get.call_args_list) == 2
        mock_requests.reset_mock()
        result = request(url)
        assert len(mock_requests.get.call_args_list) == 1 
