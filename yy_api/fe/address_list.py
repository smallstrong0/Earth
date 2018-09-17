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
    result = []
    if error is None:
        result = d_address.get_address_list(params)
        if len(result) >= 0:
            for addr in result:
                addr.pop('_id')
        else:
            error = -2, '取地址失败'

    if error is None:
        result.reverse()
        return c_tool.check_sort_serialize(data=result)
    else:
        return c_tool.check_sort_serialize(msg=error)
