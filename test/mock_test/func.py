#!/usr/bin/env python # -*- coding: utf-8 -*-

import os
import requests

"""
普通方法
"""

def rm(file_name):
    """rm file by name

    """
    if os.path.isfile(file_name):
        flag = os.remove(file_name)
    else:
        return "error"

def request(url):
    """网络连接
    """
    resp = requests.get(url)
    if resp.ok and resp.json()["msg"] == "Success":
        return resp.json()["body"]
    return []
