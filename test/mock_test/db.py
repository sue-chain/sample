# -*- coding: utf-8 -*-
# pylint: disable=no-name-in-module

"""
db func
"""
import arrow
from peewee import fn
from model.db.book import Book
from model.db.stat_data import StatData
from service.thirdparty import spider_conf as ConfService
from conf.settings import STAT_TYPE
from conf.init_settings import AttrDict

STAT_TYPE = AttrDict(STAT_TYPE)

def stat_month_sign():
    """统计各cp月签约量
    签约量：有签约标识的
    统计某cp全部签约量减去之前全部签约量，得到当月签约量
    签约量需要记录两个，当月&累积量
    """
    site_list = ConfService.get_site_list()
    # 删除旧数据
    StatData.delete().where(StatData.type == STAT_TYPE.sign).execute()
    count_list = []
    for site in site_list:
        count_book = Book.select(fn.Count(1).alias('count')).where(
            Book.source == site["site_name"]
        )
        count_list.append({
            "val": count_book.count(),
            "type": STAT_TYPE.sign,
            "site_name": site["site_name"],
            "create_time": arrow.now()
        })

    StatData.insert_many(count_list).execute()
