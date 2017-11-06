#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import dap.order as dap_order


def go():
    keys = {
        'user_id': None,
        'address_id': None,
        'address': None,
        'place': None,
        'name': None,
        'phone': None,
        'qq': None,
        'category': None,
        'way': None,
        'time_stamp': None,
        'page_num': None,
        'coin': None,

        'we_chat': '',
        'remark': '',
    }
    error, params = check.go(keys)
    if error is None:
        if dap_order.check_order(params):
            dap_order.add_order(params)
        else:
            error = '创建订单失败'
    if error is None:
        print c_tool.check_sort_serialize(data=params)
        return c_tool.check_sort_serialize(data=params)
    else:
        print c_tool.check_sort_serialize(msg=error)
        return c_tool.check_sort_serialize(msg=error)
