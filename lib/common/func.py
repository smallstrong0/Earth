#! /usr/bin/env python
# -*- coding: utf8 -*-

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
from flask import Flask, request


def decode_html(s):
    return HTMLParser.HTMLParser().unescape(s)


def serialize(data):
    try:
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    except Exception as e:
        return None


def deserialize(data):
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


def get_web_params(keys):
    """
    参数校验
    :param keys:
    :return:
    """
    params = {}
    params_list = eval(request.values.items().__str__())
    for param in params_list:
        params[param[0]] = param[1]

    for key in keys:
        if key not in params:
            if keys[key] is None:
                return {}, (-1, 'param <{}> is missing'.format(key))
            else:
                params[key] = keys[key]
    if params.has_key('user_id'):
        try:
            long(params['user_id'])
        except Exception as e:
            return {}, (-1, 'invalid user_id = {}'.format(params['user_id']))

    return params, None
