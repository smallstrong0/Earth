#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import requests
import yy_api.dap.mod_user_info as d_mod_user_info


def go():
    keys = {
        'user_id': None,
        'user_info': None,
    }
    error, params = check.simple_go(keys)

    dic = {
        'status': 'ok',
    }

    if error is None:
        bool = d_mod_user_info.set_user_info(params)
        if bool:
            dic['status'] = 'ok'
        else:
            dic['status'] = 'bad'
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
