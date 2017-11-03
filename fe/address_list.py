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

    dic = {
        'addr_list': []
    }

    if error is None:
        result = d_address.get_address_list(params)
        print result
        print type(result)
        if result:
            dic['addr_list'] = result
        else:
            error = -2, '获取地址失败'

    if error is None:
        print c_tool.check_sort_serialize(data=dic)
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
