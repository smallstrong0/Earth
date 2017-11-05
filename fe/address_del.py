#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import dap.address as d_address


def go():
    keys = {
        'address_id': None,
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        result = d_address.remove_address(params)
        if result:
            dic.update(params)
        else:
            error = '删除地址失败'

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
