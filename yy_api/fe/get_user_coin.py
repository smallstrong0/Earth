#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import yy_api.dap.get_user_coin
import key


def go():
    keys = {
        'user_id': None,
    }
    error, params = check.simple_go(keys)
    info = {'coin_num': 0}
    if error is None:
        coin_num = yy_api.dap.get_user_coin.get_coin(params)
        info['coin_num'] = coin_num

    if error is None:
        return c_tool.check_sort_serialize(data=info)
    else:
        return c_tool.check_sort_serialize(msg=error)
