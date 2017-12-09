#! /usr/bin/env python
# -*- coding: utf8 -*-

"""
commmon utils
"""

import time
import datetime
import json
import random
import hashlib
import math
import uuid
import HTMLParser
import calendar
import string


def decode_html(s):
    return HTMLParser.HTMLParser().unescape(s)


def guid():
    return str(uuid.uuid1())


def hash(plain):
    return hashlib.sha1(plain).hexdigest()


def md5(_str):
    msg = hashlib.md5()
    msg.update(_str)
    return msg.hexdigest()


def serialize(data):
    """
    序列化
    :param data:
    :return:
    """
    try:
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    except Exception as e:
        return None


def deserialize(data):
    """
    反序列化
    :param data:
    :return:
    """
    try:
        return json.loads(data)
    except Exception as e:
        return None


def sort_serialize(data):
    """
    对数据字典进行排序
    :param data:
    :return:
    """
    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def check_sort_serialize(data=None, msg=None):
    """
    data传一个字典过来, msg传错误信息。两者不兼容！！！，有data不传msg,有msg不传data
    :param data:
    :param msg:
    :return:
    """
    if msg is not None and len(msg) > 0:  # 说明有错误
        return sort_serialize({"data": {}, "code": -1, "message": msg})
    elif msg is None and data is not None:
        return sort_serialize({"data": data, "code": 200, "message": "ok"})
