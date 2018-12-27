#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 16:13
# @Author  : SmallStrong
# @Des     : 
# @File    : random_list.py
# @Software: PyCharm


import wte_api.common._redis as redis_go
import tool.c_utils as c_tool

redis_cli = redis_go.cli()


def get_random_list():
    _list = []
    for i in range(10):
        key = redis_cli.randomkey()

        data = redis_cli.hgetall(key.split('xcf:')[1])
        data['key'] = key
        data['step_urls'] = eval(data.get('step_urls', '[]'))

        data['materials'] = data.get('materials', '[]').decode('raw_unicode_escape').encode('utf8')
        data['steps_texts'] = data.get('steps_texts', '[]').decode('raw_unicode_escape').encode('utf8')

        _list.append(data)
    return _list
