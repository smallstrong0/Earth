#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 10:45
# @Author  : SmallStrong
# @Des     : 
# @File    : ts.py
# @Software: PyCharm

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool


def go():
    keys = {
        'ts': None,
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        ts = int(params['ts'])
        if ts == -1:
            dic['date'] = t_tool.get_time()
        else:
            dic['date'] = t_tool.get_time(ts)

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
