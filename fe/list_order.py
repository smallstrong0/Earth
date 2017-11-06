#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import dap.order as dap_order


def go():
    keys = {
        'user_id': None,
    }
    error, params = check.simple_go(keys)
    if error is None:
        order_list = dap_order.get_order_list(params)
        for order in order_list:
            order.pop('_id')
    if error is None:
        return c_tool.check_sort_serialize(data=order_list)
    else:
        return c_tool.check_sort_serialize(msg=error)
