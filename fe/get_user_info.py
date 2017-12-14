#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dap.get_user_info
import key


def go():
    keys = {
        'user_id': None,
    }
    error, params = check.simple_go(keys)

    if error is None:
        info = dap.get_user_info.get_info(params)
        if info:
            info.pop('_id')
        else:
            info = {'coin': 0}

    if error is None:
        return c_tool.check_sort_serialize(data=info)
    else:
        return c_tool.check_sort_serialize(msg=error)
