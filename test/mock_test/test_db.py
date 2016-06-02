# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""test db sample
"""

__authors__ = ['"sue.chain" <sue.chain@gmail.com>']

import os
import sys
import mock

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
from sample.test.mock_test.db import stat_month_sign


class TestStatData(object):
    """
    test stat data
    """
    def setup(self):
        """resource setup
        """
        self.site_list = [{
            "update_time": 1453824136,
            "create_time": 1450104346,
            "site_name": "纵横",
            "id": 1,
            "key": "zongheng"
        }]

        self.result = {
            'site_name': '纵横',
            'create_time': u'2016-05-01',
            'type': 1, 'val': 1
        }

    @mock.patch('sample.test.mock_test.db.Book.select')
    @mock.patch('sample.test.mock_test.db.StatData.insert_many')
    @mock.patch('sample.test.mock_test.db.StatData.delete')
    @mock.patch('sample.test.mock_test.db.ConfService')
    def test_stat_month_sign(self, mock_conf, mock_stat_del, mock_stat_insert, mock_book):
        """
        test_stat_month_sign
        """
        mock_conf.get_site_list.return_value = self.site_list
        mock_stat_del.where.return_value = True
        mock_book().where().count.return_value = 1

        stat_month_sign()

        assert mock_stat_del().where.call_args[0][0].lhs.name == "type"
        assert mock_stat_del().where.call_args[0][0].rhs == 1
        assert mock_stat_del().where.call_args[0][0].op == "="

        result = mock_stat_insert.call_args[0][0]
        for k, v in self.result.items():
            assert result[0][k] == v
