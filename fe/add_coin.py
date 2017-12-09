#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import requests
import dap.add_coin
import key


def go():
    keys = {
        'user_id': None,
        'money': None,
        'openid': None
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        data = dap.add_coin.get_data(params)
        r = requests.post(
            'https://api.mch.weixin.qq.com/pay/unifiedorder', data)
        print r.content

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
