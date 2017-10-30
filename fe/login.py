#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool


def go():
    keys = {
        'wechat_id': None,

    }
    error, params = check.simple_go(keys)
    if error is None:
        dic = {
            'user_id': 1
        }

    if error is None:
        print c_tool.check_sort_serialize(data=params)
        return c_tool.check_sort_serialize(data=params)
    else:
        print c_tool.check_sort_serialize(msg=error)
        return c_tool.check_sort_serialize(msg=error)
