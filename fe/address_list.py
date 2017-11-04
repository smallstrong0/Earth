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
        print result
        print type(result)
        if len(result) >= 0:
            pass
        else:
            error = -2, '取地址失败'

    if error is None:
        print 'test'
        print c_tool.check_sort_serialize(data=result)
        return c_tool.check_sort_serialize(data=str(result))
    else:
        return c_tool.check_sort_serialize(msg=error)
