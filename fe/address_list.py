#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import dap.address as d_address


def go():
    keys = {
        'user_id': None,
    }
    error, params = check.simple_go(keys)

    if error is None:
        result = d_address.get_address_list(params)
        print result[0]
        if result:
            pass
        else:
            error = '获取地址失败'

    if error is None:
        return c_tool.check_sort_serialize(data=result[0])
    else:
        return c_tool.check_sort_serialize(msg=error)
