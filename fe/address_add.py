#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import dap.address as d_address


def go():
    keys = {
        'user_id': None,
        'name': None,
        'phone': None,
        'qq': None,
        'we_chat': '',
        'address': None,
        'place': None,
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        result = d_address.add_address(params)
        print result
        if result:
            dic['status'] = 'ok'
        else:
            error = '添加地址失败'

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
