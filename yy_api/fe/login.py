#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import requests
import dap.login as d_login
import key


def go():
    keys = {
        'code': None,
    }
    error, params = check.simple_go(keys)

    dic = {
        'openid': '',
        'session_key': '',
        'user_id': '',
        'time_stamps_zh': []
    }

    if error is None:
        r = requests.get(
            'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
                key.appId, key.AppSecret, params['code']))
        dic['openid'] = r.json()['openid']
        dic['session_key'] = r.json()['session_key']
        data = d_login.get_wx_user_id_and_coin(dic['openid'])
        dic['user_id'] = data['user_id']
        dic['coin'] = data['coin']
        dic['time_stamps_zh'] = get_time_stamps()

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)


def get_time_stamps():
    z_ts = t_tool.get_today_zero_time()
    first_stamp = z_ts + 3600 * 9
    time_stamps_zh = []
    for i in range(7):
        time_stamps_zh.append(t_tool.get_time(first_stamp + 3600 * i))
    return time_stamps_zh
